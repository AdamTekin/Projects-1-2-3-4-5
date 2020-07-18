from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


# @app.route('/index')
# def index():
#     return render_template('index.html')


# @app.route('/index', methods=['POST', 'GET'])
# def index_post():
def index_post(number_decimal):
    mappings = {1000: "M", 900: 'CM', 500: "D", 400: 'CD', 100: "C",
                90: 'XC', 50: "L", 40: 'XL', 10: "X", 9: 'IX', 5: "V", 4: 'IV', 1: "I"}
    number = number_decimal  # 1994 "MCMXCIV"
    result = ""
    if int(number) >= 1 and int(number) <= 3999:
        number = int(number)
        for k, v in mappings.items():  # k =1000
            value = number // k  # 1
            result += v * value  # M *1
            number %= k  # 994
        # "MCMXCIV"
    return result


@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', not_valid=False, developer_name='Adam')


@app.route('/', methods=['POST'])
def main_post():
    number = request.form['number']
    if not number.isdigit():
        return render_template("index.html", not_valid=True, developer_name='Adam')

    if int(number) < 1 or int(number) > 3999:
        return render_template("index.html", not_valid=True, developer_name='Adam')

    return render_template('result.html', number_decimal=number, number_roman=index_post(number), developer_name='Adam')


# @app.route('/result', methods=['POST'])
# def result_get():
#     return (index_post())


if __name__ == '__main__':
    # app.run('localhost', port=5000, debug=True)
    # app.run(debug=True)
    app.run('0.0.0.0', port=80)
