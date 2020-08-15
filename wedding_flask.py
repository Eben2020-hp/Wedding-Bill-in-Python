from flask import Flask, render_template, request

app = Flask(__name__)


shop_list = {'Saree':50000, 'Gown':100000, 'Bangles': 15000, 'Shoes': 20000}
quantity = {}

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # print(request.form['Saree'])
        for key, value in shop_list.items():
            quantity[key] = request.form[key]
        print(quantity)
    else:
        return render_template("list.html", dict=shop_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')