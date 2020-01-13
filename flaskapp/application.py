from flask import Flask, render_template
application = app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test')

if __name__ == "__main__":
    app.run()