# Library Management System API


A Library Management System API using Django and Django REST Framework. The API will serve as the backend for managing library resources, allowing users to interact with the system by borrowing, returning, and viewing books. You will be tasked with creating and deploying a fully functional API, simulating a real-world development environment, where backend logic, database management, and API design play crucial roles.

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

List all books (supports filtering) : `/api/books/`

Retrieve, update, or delete a book : `/api/books/<id>/`

List all users : `/api/users/`

Retrieve, update, or delete a user : `/api/users/<id>/`

Check out a book : `/api/checkout/`

Return a book : `/api/return/`

View available books only : `/api/books/available/`

## Credits
Developed by Dan-King'ori the Jaba Scripter.