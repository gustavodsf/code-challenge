"""
Face Mask Detection - Deep Learning Model
==========================================
This script builds a CNN classifier to detect whether subjects are wearing face masks.

Dataset Structure:
- train.csv: Training data with file_name and label columns
- test.csv: Test data with file_name column
- train_images/: Folder containing training images
- test_images/: Folder containing test images

Output:
- submissions.csv: Predictions with file_name and label (0/1) columns
"""

import os
import random
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
from shutil import unpack_archive

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ============================================================================
# CONFIGURATION
# ============================================================================

SEED = 42
IMG_SIZE = 160          # Image size for training (smaller = faster on CPU)
BATCH_SIZE = 32         # Batch size (reduce to 16 if low on RAM)
EPOCHS = 8              # Number of training epochs
LR = 3e-4               # Learning rate
PATIENCE = 3            # Early stopping patience
TRAIN_DIR = "train_images/train_images"  # Adjust based on extraction structure
TEST_DIR = "test_images/test_images"      # Adjust based on extraction structure
SUBMISSION_FILE = "submissions.csv"
DEVICE = "cpu"          # Use "cuda" if GPU available

# ============================================================================
# REPRODUCIBILITY
# ============================================================================

def seed_everything(seed=SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

seed_everything()

# ============================================================================
# DATASET CLASS
# ============================================================================

class MaskDataset(Dataset):
    """Custom Dataset for loading face mask images"""
    
    def __init__(self, df, img_dir, transform=None, has_label=True):
        self.df = df.reset_index(drop=True)
        self.img_dir = img_dir
        self.transform = transform
        self.has_label = has_label

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        path = os.path.join(self.img_dir, row["file_name"])
        img = Image.open(path).convert("RGB")
        
        if self.transform:
            img = self.transform(img)
        
        if self.has_label:
            label = int(row["label"])
            return img, label
        return img, row["file_name"]

# ============================================================================
# DATA TRANSFORMS
# ============================================================================

train_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomApply([transforms.ColorJitter(0.2, 0.2, 0.2, 0.02)], p=0.3),
    transforms.RandomRotation(8),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

val_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# ============================================================================
# DOWNLOAD AND EXTRACT DATA (Optional - for HackerRank environment)
# ============================================================================

def download_and_extract_data():
    """Download and extract dataset from HackerRank"""
    print('Downloading train images...')
    os.system('wget https://hr-projects-assets-prod.s3.amazonaws.com/c6bmflg88c4/6824f2e62c3fb7777f00036600ee5127/train_images.zip')
    
    print('Downloading test images...')
    os.system('wget https://hr-projects-assets-prod.s3.amazonaws.com/c6bmflg88c4/6dc5e0adf309cf1ee9f070e55f1a21f5/test_images.zip')
    
    print('Extracting Train Dataset...')
    unpack_archive('train_images.zip', '')
    
    print('Extracting Test Dataset...')
    unpack_archive('test_images.zip', '')
    
    # Clean up zip files
    os.remove('train_images.zip')
    os.remove('test_images.zip')
    print('Data extraction complete!')

# ============================================================================
# LOAD DATA
# ============================================================================

def load_data():
    """Load train and test CSV files"""
    print("Loading data...")
    train_df = pd.read_csv("train.csv")
    test_df = pd.read_csv("test.csv")
    
    print(f"Train samples: {len(train_df)}")
    print(f"Test samples: {len(test_df)}")
    print(f"Label distribution:\n{train_df['label'].value_counts()}")
    
    return train_df, test_df

# ============================================================================
# CREATE DATALOADERS
# ============================================================================

def create_dataloaders(train_df, test_df):
    """Create train, validation, and test dataloaders"""
    
    # Split train into train/val
    trn_df, val_df = train_test_split(
        train_df, test_size=0.15, stratify=train_df["label"], random_state=SEED
    )
    
    print(f"Training samples: {len(trn_df)}")
    print(f"Validation samples: {len(val_df)}")
    
    # Create datasets
    train_ds = MaskDataset(trn_df, TRAIN_DIR, transform=train_transforms, has_label=True)
    val_ds = MaskDataset(val_df, TRAIN_DIR, transform=val_transforms, has_label=True)
    test_ds = MaskDataset(test_df, TEST_DIR, transform=val_transforms, has_label=False)
    
    # Create dataloaders
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)
    
    return train_loader, val_loader, test_loader

# ============================================================================
# MODEL CREATION
# ============================================================================

def create_model():
    """Create ResNet18 model with custom classifier head"""
    print("Creating ResNet18 model...")
    
    try:
        # Try loading pretrained weights (old torchvision API)
        model = models.resnet18(pretrained=True)
        print("✓ Loaded pretrained ResNet18")
    except Exception as e:
        print(f"Pretrained load failed: {e}")
        print("Training from scratch...")
        model = models.resnet18(pretrained=False)
    
    # Replace final layer for binary classification
    in_feats = model.fc.in_features
    model.fc = nn.Linear(in_feats, 2)
    model = model.to(DEVICE)
    
    return model

# ============================================================================
# TRAINING FUNCTIONS
# ============================================================================

def run_epoch(model, loader, criterion, optimizer=None, train=True):
    """Run one epoch of training or validation"""
    
    if train:
        model.train()
    else:
        model.eval()
    
    total_loss, correct, total = 0.0, 0, 0
    all_preds, all_labels = [], []
    
    for batch in tqdm(loader, leave=False, desc="Train" if train else "Val"):
        imgs, labels = batch
        imgs, labels = imgs.to(DEVICE), labels.long().to(DEVICE)
        
        if train:
            optimizer.zero_grad()
        
        with torch.set_grad_enabled(train):
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            
            if train:
                loss.backward()
                optimizer.step()
        
        total_loss += loss.item() * imgs.size(0)
        preds = outputs.argmax(1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)
        
        all_preds.extend(preds.cpu().numpy().tolist())
        all_labels.extend(labels.cpu().numpy().tolist())
    
    avg_loss = total_loss / max(total, 1)
    acc = correct / max(total, 1)
    
    return avg_loss, acc, np.array(all_preds), np.array(all_labels)

def train_model(model, train_loader, val_loader):
    """Train the model with early stopping"""
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(EPOCHS, 1))
    
    best_acc = 0.0
    best_state = None
    epochs_no_improve = 0
    
    print("\n" + "="*60)
    print("TRAINING START")
    print("="*60)
    
    for epoch in range(1, EPOCHS + 1):
        print(f"\nEpoch {epoch}/{EPOCHS}")
        print("-" * 40)
        
        # Train
        tr_loss, tr_acc, _, _ = run_epoch(
            model, train_loader, criterion, optimizer, train=True
        )
        
        # Validate
        val_loss, val_acc, _, _ = run_epoch(
            model, val_loader, criterion, train=False
        )
        
        scheduler.step()
        
        print(f"Train Loss: {tr_loss:.4f} | Train Acc: {tr_acc:.4f}")
        print(f"Val   Loss: {val_loss:.4f} | Val   Acc: {val_acc:.4f}")
        
        # Early stopping check
        if val_acc > best_acc:
            best_acc = val_acc
            best_state = {k: v.cpu() for k, v in model.state_dict().items()}
            epochs_no_improve = 0
            print(f"✓ New best validation accuracy: {best_acc:.4f}")
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= PATIENCE:
                print(f"\nEarly stopping triggered after {epoch} epochs")
                break
    
    print("\n" + "="*60)
    print(f"TRAINING COMPLETE - Best Val Accuracy: {best_acc:.4f}")
    print("="*60 + "\n")
    
    # Load best model
    if best_state is not None:
        model.load_state_dict({k: v.to(DEVICE) for k, v in best_state.items()})
    
    return model, best_acc

# ============================================================================
# INFERENCE
# ============================================================================

def generate_predictions(model, test_loader):
    """Generate predictions on test set"""
    
    print("Generating predictions on test set...")
    model.eval()
    
    file_names, preds_bin = [], []
    
    with torch.no_grad():
        for batch in tqdm(test_loader, desc="Inference"):
            imgs, fnames = batch
            imgs = imgs.to(DEVICE)
            outputs = model(imgs)
            preds = outputs.argmax(1).cpu().numpy().tolist()
            
            file_names.extend(list(fnames))
            preds_bin.extend(preds)
    
    print(f"✓ Generated {len(file_names)} predictions")
    
    return file_names, preds_bin

# ============================================================================
# SUBMISSION
# ============================================================================

def create_submission(file_names, predictions):
    """Create submission CSV file"""
    
    submission_df = pd.DataFrame({
        "file_name": file_names,
        "label": predictions
    })
    
    print("\nSubmission preview:")
    print(submission_df.head(10))
    print(f"\nShape: {submission_df.shape}")
    print(f"Label distribution:\n{submission_df['label'].value_counts()}")
    
    # Save to CSV
    submission_df.to_csv(SUBMISSION_FILE, index=False)
    print(f"\n✅ Saved {SUBMISSION_FILE}")
    print(f"File size: {os.path.getsize(SUBMISSION_FILE)} bytes")
    
    # Validate submission format
    validate_submission(submission_df)
    
    return submission_df

def validate_submission(submission_df):
    """Validate submission file format"""
    
    print("\nValidating submission format...")
    
    assert list(submission_df.columns) == ["file_name", "label"], \
        f"Wrong columns: {list(submission_df.columns)}"
    
    assert submission_df['label'].isin([0, 1]).all(), \
        "Labels must be 0 or 1"
    
    assert not submission_df.isnull().any().any(), \
        "Submission contains null values"
    
    print("✅ All validation checks passed!")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    
    print("="*60)
    print("FACE MASK DETECTION - DEEP LEARNING MODEL")
    print("="*60)
    
    # Uncomment if running in HackerRank environment
    # download_and_extract_data()
    
    # Load data
    train_df, test_df = load_data()
    
    # Create dataloaders
    train_loader, val_loader, test_loader = create_dataloaders(train_df, test_df)
    
    # Create model
    model = create_model()
    
    # Train model
    model, best_acc = train_model(model, train_loader, val_loader)
    
    # Generate predictions
    file_names, predictions = generate_predictions(model, test_loader)
    
    # Create submission
    submission_df = create_submission(file_names, predictions)
    
    print("\n" + "="*60)
    print("PROCESS COMPLETE!")
    print("="*60)
    print(f"Best validation accuracy: {best_acc:.4f}")
    print(f"Submission file: {SUBMISSION_FILE}")
    print("Ready to submit!")

if __name__ == "__main__":
    main()
