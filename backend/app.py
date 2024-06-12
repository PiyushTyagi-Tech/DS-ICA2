from flask import Flask, jsonify, request, render_template
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="35.232.9.242",
        database="flask-db",
        user="piyush",
        password="piyush"
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return 'Submitted!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

