from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (you can replace this with a database)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = {"id": len(books) + 1, "title": title, "author": author}
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        return redirect(url_for('index'))
    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
