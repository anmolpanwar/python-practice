from flask import *
app = Flask(__name__)

@app.route('/home')
def func():
    return render_template('first.html')

if __name__=='__main__':
    app.run(host='http://127.0.0.1',port = 5000, debug=True)
