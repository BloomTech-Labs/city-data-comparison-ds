from flask import Flask
application = app = Flask(__name__)

@app.route("/")
def hello():
    return 'test'

if __name__ == "__main__":
    app.run()
