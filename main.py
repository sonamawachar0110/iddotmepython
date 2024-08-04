from flask import Flask, render_template, request, Response, redirect, url_for

from werkzeug.exceptions import abort

from . import sql

# This global variable is declared with a value of `None`, instead of calling
# `init_connection_engine()` immediately, to simplify testing. In general, it
# is safe to initialize your database connection pool when your script starts
# -- there is no need to wait for the first request.
db = None

app = Flask(__name__)

@app.before_first_request
def create_tables():
    global db
    db = db or sql.init_connection_engine()
    # Create tables (if they don't already exist)
    with db.connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS helloworld "
            "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, helloworld VARCHAR(100) NOT NULL);"
        )
@app.route('/')
def index():
    with db.connect() as conn:
        helloworld = conn.execute(
            'SELECT helloworld'
            ' FROM hellowworld hw'
        ).fetchall()
        return render_template('landingpage.html', helloworld=helloworld)

