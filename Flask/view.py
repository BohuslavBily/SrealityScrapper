from flask import Flask, render_template
import os
import psycopg2

port = int(os.environ.get('PORT', 8080))
host = '0.0.0.0'
hostname = 'db'
username = 'postgres_dock'
password = 'postgres_dock'
database = 'postgres_dock'

app = Flask(__name__)

@app.route('/')
def home():
    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    
    cur = connection.cursor()
    cur.execute("""
    SELECT id, title, loc, img_url FROM sreality
    """)
    results = cur.fetchall()
    table = []
    for row in results:
        table.append({
            "title" : row[1],
            "loc" : row[2],
            "img_url" : row[3]
        })
    return render_template('index.html', table = table)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)