from flask import Flask, render_template, request

app = Flask(__name__)


shop_list = {'Saree':50000, 'Gown':100000, 'Bangles': 15000, 'Shoes': 20000}
quantity = {}

def total_price(quantity):
    total_price = 0
    for key, value in quantity.items():
        total_price += int(value) * shop_list[key]
    return(total_price)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # print(request.form['Saree'])
        for key, value in shop_list.items():
            item_quantity = 0 if request.form[key] == '' else request.form[key]
            quantity[key] = item_quantity
        print(quantity)
        grand_total = total_price(quantity)
        grand_total_aed = 0 # call conversion function
        return render_template("receipt.html", shop_list=shop_list, quantity=quantity, grand_total=grand_total, grand_total_aed=grand_total_aed)
    else:
        return render_template("list.html", dict=shop_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
