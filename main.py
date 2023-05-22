from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

news_all = [
    {
        "header": "Заголовок Новини",
        "author": "Дмитро Б.",
        "context": "опис новини",
        "date": "20.05.2023",
    },
]

user = {
    "name": "Dmytro",
    "nikname": "dimas",
    "age": 22
}


@app.route("/")
def hello():
    return render_template("index.html", user=user)


@app.route("/profile")
def profile():
    return render_template("profile.html", user=user)


@app.route("/news/<index_post>")
def news_post(index_post):
    index_post = int(index_post)
    if index_post > len(news_all):
        return "<h1>Новина не знайдена</h1>"
    news = news_all[index_post]
    return render_template("post.html", news=news)


app.run()