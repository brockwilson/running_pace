import sqlite3
from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
import datetime

# configuration
DATABASE = '/Users/brockwilson/code/python/running_pace/running_pace.db'
DATABASE_SCHEMA = '/Users/brockwilson/code/python/running_pace/schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
MINIMUM_DATE = datetime.datetime(1978, 11, 23)

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource(app.config['DATABASE_SCHEMA'], mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def date_validator(date_string):
    try:
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return (date>=MINIMUM_DATE) & (date<=datetime.datetime.today())
    except ValueError:
        # Make this more useful
        raise ValueError("Incorrect data format, should be YYYY-MM-DD.")
    

def duration_validator(duration_string):
    True

def distance_validator(distance_string):
    True

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select date, duration, distance from entries order by id desc')
    entries = [dict(date=row[0], duration=row[1], distance=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    # need to add some data validation here
    date = request.form['date']
    duration = request.form['duration']
    distance = request.form['distance']
    if date_validator(date):
        g.db.execute('insert into entries (date, duration, distance) values (?, ?, ?)', [date, duration, distance])
        g.db.commit()
        flash('New entry was successfully posted')
    else:
        flash('Not successful.')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
