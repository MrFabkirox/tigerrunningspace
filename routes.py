import os
from flask import *
from functools import wraps
import sqlite3

DATABASE = 'tiger.db'

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'my precious'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

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

@app.route('/page4', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('page4'))
    return render_template('log.html', error=error)

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
        flash('def page2')
        return render_template('page2.html', sales=sales)

@app.route('/page3')
def page3():    
        g.db = connect_db()
        cur = g.db.execute('select quote_id, quote from quotes where status = 1')
        new_quote = [dict (quote_id=row[0], quote=row[1]) for row in cur.fetchall()]
        cur = g.db.execute('select quote_id, quote from quotes')
        delete_quote = [dict (quote_id=row[0], quote=row[1]) for row in cur.fetchall()]
        g.db.close()
        return render_template('page3.html', new_quote=new_quote, delete_quote=delete_quote)
    
@app.route('/page4')
@login_required
def page4():
        return render_template('page4.html')

@app.route('/new_task', methods=['POST'])
def new_task():
        quote = request.form['quote']
        g.db = connect_db()
        g.db.execute('insert into quotes (quote, status) values (?, 1)',[request.form['quote']])
        g.db.commit()
        flash ('New entry was successfully posted')
        return redirect(url_for ('page3'))

@app.route('/delete/<int:quote_id>',)
def delete_entry(quote_id):
        g.db = connect_db()
        cur = g.db.execute('delete from quotes where quote_id='+str(quote_id))
        g.db.commit()
        g.db.close()
        flash('The new entry was deleted')
        return redirect(url_for('page3'))

@app.route('/complete/<int:quote_id>',)
def complete(quote_id):
        g.db = connect_db()
        cur = g.db.execute('update quotes set status = 0 where quote_id='+str(quote_id))
        g.db.commit()
        g.db.close()
        flash('The post was validated')
        return redirect(url_for('page3'))
    
@login_required
def hello():
       
    return render_template('hello.html')
    
if __name__ == '__main__':
#Bind to PORT if defined, otherwise default to 5000
#         app.run(debug=True)
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
        

