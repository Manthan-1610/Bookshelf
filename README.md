# Bookshelf App

Bookshelf App is a simple web application to manage your book collection. You can add new books with their title, author, and rating, view recently added books on the homepage, and see the full collection of books.

## Table of Contents

- [Bookshelf App](#bookshelf-app)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Setup Instructions](#setup-instructions)

## Features

- Add a new book with its title, author, and rating.
- View recently added books on the homepage.
- View the entire book collection.
- Real-time clock display on the homepage.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: MySQL

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL Server

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/bookshelf-app.git
   cd Bookshelf
   ```

2. **Install dependencies:**

   ```sh
   pip install flask mysql-connector-python
   ```

3. **Setup MySQL database:**
  
  ```sh
   CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5)
  );
  ```

4. **Run the application:**

   ```sh
   python app.py
