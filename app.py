
from flask import Flask, render_template, request, jsonify, Response
import mysql.connector
import time
from datetime import datetime

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'bookshelf_db'
}

@app.route('/time-feed')
def time_feed():
    def generate():
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield f"data: {current_time}\n\n"
            time.sleep(1)  # Wait for 1 second before sending the next update

    return Response(generate(), mimetype='text/event-stream')

# Function to create a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Route for the homepage
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', books=books, current_time=current_time)

# Route for the add book form page
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        
        if not title or not author or not rating:
            return jsonify({'status': 'error', 'message': 'All fields are required!'})
        elif not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            return jsonify({'status': 'error', 'message': 'Rating must be a number between 1 and 5'})
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, rating) VALUES (%s, %s, %s)",
                           (title, author, rating))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'status': 'success', 'message': 'Book added successfully!'})
    return render_template('add_book.html')

# Route for displaying the book collection
@app.route('/collection')
def collection():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('collection.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)