This is a library management project.
# Library_management
# 📚 Django Library Management System

A simple Library Management System built with Django. This project demonstrates the implementation of Django Models, Views, Templates, Forms, URL Routing, and Database Operations.

## 🚀 Features

### Book Management

* View all books available in the library.
* Display detailed information for a specific book.
* Add new books to the database.
* Update existing book information.
* Store and retrieve data using Django ORM.

### Author Management (Bonus)

* Create and manage authors separately.
* Associate books with authors using database relationships.
* Validate author information before saving.
* Store additional author details such as age and number of published books.

## 🗄️ Database Models

### Book

| Field          | Description        |
| -------------- | ------------------ |
| title          | Book title         |
| author         | Author of the book |
| date_published | Publication date   |
| isbn           | ISBN number        |

### Author (Bonus)

| Field       | Description               |
| ----------- | ------------------------- |
| first_name  | Author's first name       |
| last_name   | Author's last name        |
| age         | Author's age              |
| books_count | Number of published books |

## 🖥️ Views

### Book List View (`list_book`)

Displays all books stored in the database.

### Book Detail View (`detail_book`)

Shows detailed information about a selected book.

### Create / Update Book View (`update_create_book`)

Handles both:

* Creating new books
* Updating existing books

### Add Author View (`add_author`)

Receives author information, validates it, and stores it in the database.

## 🎨 Templates

### `book_list.html`

Displays a list of all books with links to their detail pages.

### `book_detail.html`

Displays:

* Title
* Author
* Publication Date
* ISBN

### `book_form.html`

Form for creating and updating books.

### `author_add.html`

Form for adding a new author.

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite
* Django ORM

## 📂 Project Structure

```text
library_project/
│
├── library/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── book_list.html
│       ├── book_detail.html
│       ├── book_form.html
│       └── author_add.html
│
├── manage.py
└── db.sqlite3
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/library-management.git
```

Navigate to the project directory:

```bash
cd library-management
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🎯 Learning Objectives

This project was developed to practice:

* Django project structure
* Models and migrations
* CRUD operations
* Function-Based Views
* Form handling
* Template rendering
* URL configuration
* Database relationships

## 🔮 Future Improvements

* Delete books and authors
* Search functionality
* Pagination
* User authentication
* Django Admin customization

## 👨‍💻 Author

Developed as a Django practice project for learning web development and database management.