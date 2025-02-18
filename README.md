Live deployed link: https://danielkingori.pythonanywhere.com/api/  


# Library Management System API


A Library Management System API using Django and Django REST Framework. The API will serve as the backend for managing library resources, allowing users to interact with the system by borrowing, returning, and viewing books. 

## Features 
### 1. Books Management (CRUD)
The system provides full Create, Read, Update, and Delete (CRUD) operations for managing books. Each book contains the following attributes:
- Title
- Author
- ISBN (unique)
- Published Date
- Number of Copies Available

### 2. Users Management (CRUD)
CRUD operations to manage library users. Each user has the following attributes:
- Username (unique)
- Email
- Date of Membership
- Active Status

### 3. Check-Out and Return Books
**Check-Out Books:**

- Users can check out available books, reducing the number of available copies.
- Only one copy of a book can be checked out per user at a time.
- Users cannot check out books if there are no available copies.

**Return Books:**

- Users can return previously checked-out books, increasing the available copies.
- Track and log the dates when the book was checked out and returned.

### 4. View Available Books
The system allows users to:
- View a list of all books.
- Filter the list to show only books that are available (i.e., books with available copies).
- Search for books using optional query filters:
    - Title
    - Author
    - ISBN

**Additional Features**
- Filtering and Search: The API supports filtering and searching books based on various fields.

### Technologies Used
- Django: Core web framework.
- Django REST Framework (DRF): For building the RESTful API.
- SQLite: Database management system.

# Installation
Clone the repository:
`git clone https://github.com/danielkingori/Library-Management-System-API.git`
`cd LMS_API`

Install dependencies:
`pip install -r requirements.txt`

Apply migrations:
`python manage.py makemigrations`
`python manage.py migrate`

Run the development server:
`python manage.py runserver`

Access the localhost dev url:
http://127.0.0.1:8000/


## API Endpoints

Register as a library member : `/api/register/`

Login to get the Access & Refresh tokens : `/api/auth/`

List all books (supports filtering) : `/api/books/`

Retrieve, update, or delete a book : `/api/books/<pk>/`

List all Authors : `/api/authors/`

Retrieve, update, or delete an Author : `/api/authors/<pk>/`

Borrow a book : `/api/borrow/`

Return a book : `/api/return/<pk>/`

View borrowed and returned books history as a member or admin : `/api/history/`

Filter available books only : `/api/books/?Available=True`

Filter books by Author Name : `/api/books/?author_name=name`

Filter books by Title : `/api/books/?title=title`

Search book by ISBN (eg isbn = 9781101684843 ) : `/api/books/?isbn=9781101684843`

## Credits
Developed by Dan-King'ori the Jaba Scripter.
