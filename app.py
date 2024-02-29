from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM scores')
    scores = cur.fetchall()
    conn.close()
    return render_template('index.html', scores=scores)

@app.route('/add', methods=['POST'])
def add_score():
    name = request.form['name']
    points = request.form['points']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO scores (name, points) VALUES (?, ?)', (name, points))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_score(id):
    name = request.form['name']
    points = request.form['points']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE scores SET name = ?, points = ? WHERE id = ?', (name, points, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_score(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM scores WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
