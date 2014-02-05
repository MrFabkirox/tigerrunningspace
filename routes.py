import os
from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = 'my precious'

@app.route('/')

@app.route('/home')
def home():
        return render_template('home.html')
    
@app.route('/page1')
def page1():
        return render_template('page1.html')
    
@app.route('/page2')
def page2():
        return render_template('page2.html')
    
# def login_required(test):
    

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect (url_for('log'))
    
@app.route('/hello')
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
        app.run(debug=True)
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
        

