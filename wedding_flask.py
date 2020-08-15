from flask import Flask, render_template

app = Flask(__name__)


items = {'Saree':50000, 'Gown':100000, 'Bangles': 15000, 'Shoes': 20000}

@app.route("/")
def home():
    return render_template("list.html", object=items)


if __name__ == "__main__":
    app.run(host='0.0.0.0')