from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h2><body bgcolor=black text=white><center>hello!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
            
