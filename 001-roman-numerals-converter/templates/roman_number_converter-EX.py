from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index-EX.html')


@app.route('/index', methods=['POST', 'GET'])
def rom_conv():

    mappings = {1000: "M", 900: 'CM', 500: "D", 400: 'CD', 100: "C",
                90: 'XC', 50: "L", 40: 'XL', 10: "X", 9: 'IX', 5: "V", 4: 'IV', 1: "I"}
    # number = input("enter a number :")  # 1994 "MCMXCIV"
    number = request.form['num1']
    result = ""
    if not number.isdigit():
        return "Not Valid! Please enter a number between 1 and 3999, inclusively."
    else:
        if int(number) < 1 or int(number) > 3999:
            return "Not Valid! Please enter a number between 1 and 3999, inclusively."
        elif int(number) >= 1 and int(number) <= 3999:
            number = int(number)
            for k, v in mappings.items():  # k =1000
                value = number // k  # 1
                result += v * value  # M *1
                number %= k  # 994
            # "MCMXCIV"

    return render_template('result-EX.html', number_decimal=request.form['num1'], number_roman=result)


@app.route('/result', methods=['POST'])
def result_get():
    return (rom_conv())


if __name__ == '__main__':
    # app.run('localhost', port=5000, debug=True)
    # app.run(debug=True)
    app.run('0.0.0.0', port=80)
