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
 
        maturity,payment = calculate(principal,returnRate,interestRate,tenure,termination)
        maturity = '{:,.2f}'.format(maturity)
        #maturity = "Maturity Value : RM " + maturity
        payment = '{:,.2f}'.format(-payment)
        #payment = "Monthly Instalment : RM " + payment
        sum = [maturity,payment,principal,returnRate,interestRate,tenure,termination]
        return render_template('app.html', sum = sum)


if __name__ == ' __main__':
    app.debug = True
    app.run()
