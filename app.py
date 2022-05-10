from pynubank import Nubank
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

@app.route('/dados')
def dados():
    nu = Nubank()
    nu.authenticate_with_cert('47919587808', 'samu2015', './cert.p12')

    print(nu.get_account_balance())

    # Lista de dicionários contendo todas as transações da conta
    account_statements = nu.get_account_statements()
    # print(account_statements)

    return jsonify(account_statements)
  
app.run(host='0.0.0.0')