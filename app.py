from flask import Flask
from flask import render_template
from flask import request
import requests
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        #Taking input
        symbol = request.form['symbol'].upper()

        #API CALL (fpm cloud api)
        datum = requests.get('https://fmpcloud.io/api/v3/quote/'+symbol+'?apikey=c94cc5b677a9c2c402a745e0aefeea64')
        result_data = json.loads(datum.text)

        #Error message, if any
        if len(result_data) < 1:
            ResData = {'msg' : "Invalid stock symbol found! Sorry, Please enter a valid symbol"}
            return render_template('index.html', **ResData)
        else:
            dateTimeNow = datetime.now()
            NameofStock = result_data[0]["name"]
            price = result_data[0]["price"]
            valueChange = result_data[0]["change"]
            perChange = result_data[0]["changesPercentage"]
            ResData = {'dateTimeNow': dateTimeNow, 'NameofStock': NameofStock, 'price': price, 'valueChange' : valueChange, 'perChange': perChange }
            return render_template('index.html', **ResData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')