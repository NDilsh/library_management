# Library Manager

A simple web-based application to manage a list of books in a library. The application allows the user to perform the following basic tasks.
## Features

- View the list of books in a table/list.
- Adding a new book with details such as Title, Author, Genre, etc.
- Delete an existing book.
- Searching a book based on both the genre and the name

## Tech Stack

**Client:** HTML, CSS, Bootstrap

**Server:** Django

**Database:** MySQL
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_NAME`

`DB_USER`

`DB_PASS`
## Run Locally

Clone the project

```bash
  git clone https://github.com/NDilsh/library_management.git
```

Go to the project directory

```bash
  cd library_management
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run database migrations to create the necessary tables in db

```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Feedback

If you have any feedback, please reach out to me

