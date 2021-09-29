from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, render_template
import os

app = Flask(__name__)
data = []

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.environ.get("X-CMC_PRO_API_KEY"),
}

session = Session()
session.headers.update(headers)


try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)["data"]
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


@app.route("/")
def hello_world():
    print(type(data))
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
