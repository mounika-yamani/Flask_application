from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return ("This is a flask application")



if __name__ == '__main__':
    app.run()