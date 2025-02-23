from flask import Flask, url_for

app = Flask(__name__)


@app.route("/promotion")
def promo():
    with open("promo.html", "r", encoding="utf-8") as html_file:
        return html_file.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


