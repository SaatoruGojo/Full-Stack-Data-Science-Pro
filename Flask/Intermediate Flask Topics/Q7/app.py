#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # SQLite database file
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        item_name = request.form['item_name']
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item_to_delete = Item.query.get_or_404(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update(item_id):
    item_to_update = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        item_to_update.name = request.form['item_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item_to_update)



if __name__ == '__main__':
    app.run(host='0.0.0.0')