from flask import Flask, render_template, request
from processing import calculate

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        principal = int(request.form['principal'])
        returnRate = float(request.form['returnRate'])
        interestRate = float(request.form['interestRate'])
        tenure = int(request.form['tenure'])
        termination = int(request.form['termination'])


        maturity = calculate(principal,returnRate,interestRate,tenure,termination)
        maturity = str(round(maturity,2))
        maturity = "Maturity Value : RM " + maturity
        return render_template('app.html', sum = maturity)


if __name__ == ' __main__':
    app.debug = True
    app.run()
