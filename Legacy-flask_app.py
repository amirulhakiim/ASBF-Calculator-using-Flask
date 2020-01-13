from flask import Flask, request

from processing import calculate

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        number3 = None
        number4 = None
        number5 = None

        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        try:
            number3 = float(request.form["number3"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number3"])
        try:
            number4 = int(request.form["number4"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number4"])
        try:
            number5 = int(request.form["number5"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number5"])

        if number1 is not None and number2 is not None:
            if number3 is not None and number4 is not None:
                if number5 is not None:
                    balance = calculate(number1, number2, number3, number4, number5)
                    return '''
                        <html>
                            <body>
                                <p>Maturity Value : RM {result}</p>
                                <p><a href="/">Click here to calculate again</a>
                            </body>
                        </html>
                    '''.format(result = balance)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <label>Loan amount (ex : 200,000) = </label>
                    <input type="text" name="number1" /><br>

                    <label>Asb return (ex : 8%) = </label>
                    <input type="text" name="number2" /><br>

                    <label>Loan interest (ex : 4.5%) = </label>
                    <input type="text" name="number3" /><br>

                    <label>Loan tenure (ex : 30 years) = </label>
                    <input type="text" name="number4" /><br>

                    <label>Termination year (ex : 10 years) = </label>
                    <input type="text" name="number5" /><br>

                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)