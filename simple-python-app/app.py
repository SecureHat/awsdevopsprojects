from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, welcome to AWS Devops Projects'

if __name__ == '__main__':
    app.run()

