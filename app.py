#flask app to print hello world
from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
<<<<<<< HEAD
    return 'Hello world from CI/CD'
=======
    return 'Hello world, this is CICD pipeline'
>>>>>>> 4dc0503 (Updated the message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
