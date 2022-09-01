from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo'
@app.route('/say/<name>')
def say_hi(name):
    return 'Hi ' + str(name)
@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    return str(word) * int(number)
if __name__ == "__main__":
    app.run(debug=True)