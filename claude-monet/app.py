from flask import Flask, render_template

app = Flask(__name__)

DESSERTS = [
    ("Mini snail with raisins", "4,2$", "https://avatars.mds.yandex.net/i?id=c559d07e38f0a285b0e2391ddc9005b5df9a311f-4823702&n=13"),
    ("Chocolate croissant", "4,9$", "https://avatars.mds.yandex.net/i?id=bfaebc6dc373d340730116111e63801728addbe6-5398918&n=13"),
    ("Almond croissant with frangipane", "4,9$", "https://avatars.mds.yandex.net/i?id=1c6d3ab44dfcd57b48b86c2b48dafb28ade2b3a6-4353501&n=13"),
    ("Chocolate éclair", "5,1$", "https://avatars.mds.yandex.net/i?id=c781f22e418d4c9da0028e78a72b94d4011ce578-10122172&n=13"),
    ("Raspberry profiterole", "5,2$", "https://avatars.mds.yandex.net/i?id=565c2d6234c821aad73e923a24d777a9244d89bb-5163423&n=13"),
    ("Lemon tart", "4,7$", "https://avatars.mds.yandex.net/i?id=2a00000179e80073575ae37c797a80d1e7c1-3689559&n=13"),
]
SALTY = [
    ("Asparagus with poached egg", "7,5$", "https://avatars.mds.yandex.net/i?id=16e111cf4b603c722bcba9fa10169b6cd41768db-16891649&n=13"),
    ("Salmon with greens", "11,8$", "https://avatars.mds.yandex.net/i?id=a2cb9b26f6464541f589199592151574e74f40fc-4453150&n=13"),
    ("Duck confit", "13,5$", "https://avatars.mds.yandex.net/i?id=08183a4601ad5e87b705e68ba3c11e1181347eac-5233284&n=13"),
    ("Niçoise salad", "9,2$", "https://avatars.mds.yandex.net/i?id=ddffba29084ae44737302048e377ccf688d499bd-5235006&n=13"),
    ("Ratatouille", "8,4$", "https://avatars.mds.yandex.net/i?id=b5b299a1cc58c4f284e976386a9af8c5b5b2d04e-5167445&n=13"),
    ("Quiche Lorraine", "7,9$", "https://avatars.mds.yandex.net/i?id=3189e6e6e5aef59a3a571e270d6e0d45158f1672-4834925&n=13"),
]
CHEFS = [
    ("The chef", "Victor Petrovich", "👨‍🍳"),
    ("Sous chef", "Lev Solovyov", "👨‍🍳"),
    ("Sous chef of molecular cuisine", "Ekaterina Semenovna", "👩‍🍳"),
    ("All-purpose cook, meat specialist", "Arseniy Chugunin", "🧑‍🍳"),
    ("A versatile cook, a specialist in fish", "Fyodor Yurchenko", "👨‍🍳"),
    ("Cook", "Maxim Lvov", "👨‍🍳"),
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", desserts=DESSERTS, salty=SALTY)


@app.route("/about")
def about():
    return render_template("about.html", chefs=CHEFS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
