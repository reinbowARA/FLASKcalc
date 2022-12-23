import math
from flask import render_template
from flask import request
from app import app

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        equ = '='
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            simbol = request.form['simbol']
        except ValueError:
            a = 0
            b = 0
            simbol = '%'
        if simbol =='+': 
            result = a + b 
        elif simbol == '-':
            result = a - b
        elif simbol == '*':
            result = a * b
        elif simbol == '/':
            try:
                result = a / b
            except ZeroDivisionError:
                result = "низя"
        elif simbol == 'gcd':
            result = math.gcd(a,b)
        elif simbol == '^':
            try:
                result = math.pow(a,b)
            except OverflowError:
                result= "оч жирно получается"
        else:
            result = "Error"
        return render_template("index.html", a=a,b=b,result=result,simbol=simbol,equ=equ )
    return render_template("index.html")
