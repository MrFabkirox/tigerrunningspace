import os
from flask import Flask, render_template

app = Flask(__name__)
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
    
if __name__ == '__main__':
	#Bind to PORT if defined, otherwise default to 5000
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
