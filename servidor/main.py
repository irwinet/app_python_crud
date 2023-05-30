from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell_world():
    return "Hola Mundo Cruel"

if __name__ == '__main__':
    app.run()