# Face Mask Detection - Deep Learning Model

A PyTorch-based deep learning solution for detecting whether subjects in images are wearing face masks.

## 📋 Problem Statement

Build a deep neural network to identify which subjects are wearing face masks in a dataset of photos. The model should classify each image as either:
- **0**: Not wearing a face mask
- **1**: Wearing a face mask

## 🗂️ Dataset Structure

```
.
├── train.csv                    # Training labels (file_name, label)
├── test.csv                     # Test file names (file_name)
├── train_images/                # Training images folder
│   └── train_images/            # (nested structure after extraction)
│       ├── 0001.jpg
│       ├── 0002.jpg
│       └── ...
├── test_images/                 # Test images folder
│   └── test_images/             # (nested structure after extraction)
│       ├── 0001.jpg
│       ├── 0002.jpg
│       └── ...
└── submissions.csv              # Output predictions (generated)
```

### Schema

| Field     | Type | Description                                    |
|-----------|------|------------------------------------------------|
| file_name | str  | File path/name of the image                    |
| label     | int  | Whether subject is wearing mask (1) or not (0) |

## 🚀 Quick Start

### Prerequisites

```bash
# Required packages
- Python 3.9+
- PyTorch
- torchvision
- pandas
- numpy
- scikit-learn
- Pillow
- tqdm
```

### Installation

For HackerRank/Conda environment:
```bash
!mamba install -y torch torchvision pillow scikit-learn tqdm
```

For local environment:
```bash
pip install torch torchvision pandas numpy scikit-learn pillow tqdm
```

### Running the Model

#### Option 1: Run as Python Script
```bash
python face_mask_classifier.py
```

#### Option 2: Run in Jupyter Notebook
```python
# Import and run
from face_mask_classifier import main
main()
```

#### Option 3: Step-by-step execution
```python
from face_mask_classifier import *

# Load data
train_df, test_df = load_data()

# Create dataloaders
train_loader, val_loader, test_loader = create_dataloaders(train_df, test_df)

# Create and train model
model = create_model()
model, best_acc = train_model(model, train_loader, val_loader)

# Generate predictions
file_names, predictions = generate_predictions(model, test_loader)

# Create submission
submission_df = create_submission(file_names, predictions)
```

## 🏗️ Model Architecture

- **Base Model**: ResNet18 (pretrained on ImageNet)
- **Modification**: Custom binary classification head (2 classes)
- **Input Size**: 160x160 RGB images
- **Output**: Binary classification (0 or 1)

### Why ResNet18?

- Proven architecture for image classification
- Pretrained weights provide good feature extraction
- Efficient for CPU training
- Good balance between accuracy and speed

## 🎯 Training Configuration

| Parameter          | Value              | Description                           |
|--------------------|--------------------|---------------------------------------|
| Image Size         | 160x160            | Smaller for faster CPU training       |
| Batch Size         | 32                 | Reduce to 16 if low on RAM            |
| Epochs             | 8                  | With early stopping (patience=3)      |
| Learning Rate      | 3e-4               | AdamW optimizer                       |
| Weight Decay       | 1e-4               | L2 regularization                     |
| Train/Val Split    | 85/15              | Stratified split                      |
| Device             | CPU                | Change to "cuda" if GPU available     |

## 🔄 Data Augmentation

### Training Augmentations
- Random horizontal flip (p=0.5)
- Random color jitter (brightness, contrast, saturation)
- Random rotation (±8 degrees)
- Resize to 160x160
- Normalization (ImageNet stats)

### Validation/Test Augmentations
- Resize to 160x160
- Normalization only

## 📊 Model Evaluation

The model is evaluated using **Accuracy Score** on the validation set:

```
Accuracy = (Correct Predictions) / (Total Predictions)
```

Early stopping is implemented to prevent overfitting:
- Monitors validation accuracy
- Patience: 3 epochs
- Saves best model weights

## 📤 Submission Format

The output file `submissions.csv` contains exactly 2 columns:

```csv
file_name,label
0001.jpg,1
0002.jpg,0
0003.jpg,1
...
```

### Validation Checks
- ✅ Exactly 2 columns: `file_name` and `label`
- ✅ Labels are binary: 0 or 1
- ✅ No null values
- ✅ Row count matches test set

## 🛠️ Customization

### Adjust for Better Performance

1. **Increase Training Time**
   ```python
   EPOCHS = 15
   PATIENCE = 5
   ```

2. **Use Larger Images** (if time permits)
   ```python
   IMG_SIZE = 224
   ```

3. **Try Different Model**
   ```python
   model = models.resnet50(pretrained=True)
   # or
   model = models.efficientnet_b0(pretrained=True)
   ```

4. **Adjust Learning Rate**
   ```python
   LR = 1e-4  # Lower for more stable training
   ```

5. **Enable GPU** (if available)
   ```python
   DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
   ```

### Adjust for Faster Training (CPU)

1. **Reduce Image Size**
   ```python
   IMG_SIZE = 128
   ```

2. **Reduce Batch Size**
   ```python
   BATCH_SIZE = 16
   ```

3. **Fewer Epochs**
   ```python
   EPOCHS = 5
   ```

## 📁 File Size Management

For HackerRank (20MB limit), add to `.gitignore`:

```
# Large files to exclude
train_images/
test_images/
*.zip
*.pt
*.pth
__pycache__/
.ipynb_checkpoints/
```

## 🐛 Troubleshooting

### Issue: `FileNotFoundError` for images

**Solution**: Check directory structure and adjust paths
```python
# Check actual structure
import os
print(os.listdir('train_images'))

# Adjust paths accordingly
TRAIN_DIR = "train_images/train_images"  # if nested
# or
TRAIN_DIR = "train_images"  # if flat
```

### Issue: `AttributeError: ResNet18_Weights`

**Solution**: Using old torchvision API (already handled in code)
```python
model = models.resnet18(pretrained=True)  # Old API
```

### Issue: Out of Memory

**Solution**: Reduce batch size and image size
```python
BATCH_SIZE = 16
IMG_SIZE = 128
```

### Issue: Training too slow on CPU

**Solution**: 
- Reduce `IMG_SIZE` to 128
- Reduce `EPOCHS` to 5
- Set `num_workers=0` in DataLoader

## 📈 Expected Results

- **Validation Accuracy**: 85-95% (depending on dataset quality)
- **Training Time**: 
  - CPU: ~10-20 minutes (8 epochs)
  - GPU: ~2-5 minutes (8 epochs)

## 🔍 Code Structure

```python
face_mask_classifier.py
│
├── Configuration (SEED, BATCH_SIZE, etc.)
├── MaskDataset (Custom Dataset class)
├── Data Transforms (Augmentations)
├── download_and_extract_data() (Optional)
├── load_data() (Load CSVs)
├── create_dataloaders() (Train/Val/Test loaders)
├── create_model() (ResNet18 setup)
├── run_epoch() (Training/validation loop)
├── train_model() (Full training with early stopping)
├── generate_predictions() (Inference)
├── create_submission() (Generate CSV)
├── validate_submission() (Format checks)
└── main() (Orchestrates everything)
```

## 📝 Notes

- Model uses **pretrained ResNet18** for transfer learning
- **Early stopping** prevents overfitting
- **Stratified split** maintains class balance
- **Data augmentation** improves generalization
- **CPU-optimized** for environments without GPU
- **Validation checks** ensure submission format compliance

## 🎓 Tips for Improvement

1. **Ensemble Methods**: Train multiple models and average predictions
2. **Test-Time Augmentation (TTA)**: Average predictions over multiple augmented versions
3. **Cross-Validation**: Use K-fold CV for more robust evaluation
4. **Hyperparameter Tuning**: Grid search for optimal LR, batch size, etc.
5. **Advanced Augmentations**: MixUp, CutMix, AutoAugment
6. **Larger Models**: ResNet50, EfficientNet, Vision Transformers

## 📧 Support

For issues or questions:
- Check the troubleshooting section
- Review HackerRank project guidelines
- Verify dataset structure and paths

## 📄 License

This code is provided as-is for educational and competition purposes.

---

**Good luck with your submission! 🎯**