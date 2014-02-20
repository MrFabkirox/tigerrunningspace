import os
from flask import *
from functools import wraps
import sqlite3

DATABASE = 'sales.db'

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'my precious'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def home():
        return render_template('home.html')
    
@app.route('/page1')
def page1():
        return render_template('page1.html')
    
@app.route('/page2')
def page2():
        g.db = connect_db()
        cur = g.db.execute('select rep_name, amount from reps')
        sales = [dict(rep_name=row[0], amount=row[1]) for row in cur.fetchall()]
        g.db.close()
        return render_template('page2.html', sales=sales)
    
def login_required(test):
        @wraps(test)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return test(*args, **kwargs)
            else:
                flash('You need to login first.')
                return redirect(url_for('log'))
        return wrap

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect (url_for('log'))
    
@app.route('/hello')
@login_required
def hello():
       
    return render_template('hello.html')
    
@app.route('/log', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))
    return render_template('log.html', error=error)
    
if __name__ == '__main__':
#Bind to PORT if defined, otherwise default to 5000
#         app.run(debug=True)
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
        

