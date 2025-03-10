from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/promotion")
def promo():
    with open("promo.html", "r", encoding="utf-8") as html_file:
        return html_file.read()


@app.route("/image_mars")
def image_mars():
    with open("image_mars.html", "r", encoding="utf-8") as html_file:
        return html_file.read()


@app.route("/promotion_image")
def promotion_img():
    with open("promotion_img.html", "r", encoding="utf-8") as html_file:
        return html_file.read()


@app.route("/astronaut_selection")
def astronaut_selection():
    with open("astronaut_selection.html", "r", encoding="utf-8") as html_file:
        return html_file.read()


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return render_template("choice.html", planet_name=planet_name)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


