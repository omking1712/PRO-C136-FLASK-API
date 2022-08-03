from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)

@app.route('/')
def stardata():
    return jsonify({
        'data':data
    })


if(__name__=='__main__'):
    app.run()