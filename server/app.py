#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return (f'{parameter}')

@app.route('/count/<int:parameter>')
def count(parameter):
    nums = ''
    for num in range(parameter):
        nums += f'{num}\n'
    return nums

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1_int = int(num1)
    num2_int = int(num2)

    if operation == '+':
        return f'{num1_int + num2_int}'
    elif operation == "-":
        return f'{num1_int - num2_int}'
    elif operation == "*":
        return f'{num1_int * num2_int}'
    elif operation == "div":
        return f'{num1_int / num2_int}'
    else:
        return f'{num1_int % num2_int}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)