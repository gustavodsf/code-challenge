const { Component, VERSION } = ng.core;
const { FormGroup, FormControl } = ng.forms;

@Component({
  selector: '#app',
  template: `
  <div class="content-container">
    <h2>Add new book</h2>
    <form class="add-book-form" [formGroup]="bookForm" (ngSubmit)="addBook()">
      <input
        class="add-book-form__title-input"
        formControlName="bookTitle"
        placeholder="Book title"
        type="text"
      />
      <input type="submit" class="add-book-form__btn" value="Add Book" />
    </form>
    
    <h2>Your books</h2>
    <div class="book-list" *ngFor="let book of books">
      <div class="book-list__item">
        <span class="book-list__title">{{book.name}}</span>
        <button
          type="button"
          (click)="deleteBook(book.id)"
          class="book-list__delete-btn"
        >Delete</button>
      </div>
    </div>
   </div>
  `
})
class BookManagerComponent {
  nextId: number = 1;
  books = [{id: 1, name: 'First book'}];

  bookForm = new FormGroup({
    bookTitle: new FormControl('')
  });

  addBook() {
    const bookName = (this.bookForm.value.bookTitle as string);
    this.nextId = this.nextId + 1;
    this.books.push(
      {
        id: this.nextId,
        name: bookName
      }
    )
  }

  deleteBook(bookId) {
    this.books = this.books.filter( book => book.id != bookId );
  }
}


// main.js
const { BrowserModule } = ng.platformBrowser;
const { NgModule } = ng.core;
const { CommonModule } = ng.common;
const { ReactiveFormsModule } = ng.forms;

@NgModule({
  imports: [
    BrowserModule,
    CommonModule,
    ReactiveFormsModule
  ],
  declarations: [BookManagerComponent],
  bootstrap: [BookManagerComponent],
  providers: []
})
class BookManagerModule {}

const { platformBrowserDynamic } = ng.platformBrowserDynamic;

platformBrowserDynamic()
  .bootstrapModule(BookManagerModule)
  .catch(err => console.error(err));
