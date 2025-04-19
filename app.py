from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection settings
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhanu@12345678",  # <- change this
    database="productdb"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search']
    cursor = db.cursor()

    # ❌ VULNERABLE QUERY
    sql = f"SELECT * FROM products WHERE name = '{query}'"
    print(f"Executing: {sql}")
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template('result.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
