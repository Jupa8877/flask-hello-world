import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://database_2squ_user:YhEfYLVS0XJ9wf0IhgXyVOEnbbTrzDMw@dpg-cget4102qv2dpvbbku9g-a/database_2squ")
    conn.close()
    return "Database Connection Successful"
    