import numpy as np

def compound(principal,period,rate):
    CI = principal * (pow((1 + rate / 100), period))
    return CI

def amortization(loan,rate,tenure,terminate):

    per = np.arange(tenure*12) + 1
    per_terminate = np.arange(terminate*12) + 1
    ipmt = np.ipmt((rate/100)/12, per, tenure*12, loan)
    ppmt = np.ppmt((rate/100)/12, per, tenure*12, loan)

    pmt = np.pmt((rate/100)/12, tenure*12, loan)

    balance = []
    for payment in per_terminate:
        index = payment - 1
        loan = loan + ppmt[index]
        balance.append(loan)
    return balance,pmt,ppmt,ipmt

def calculate(principal,asb_return,loan_interest,loan_tenure,year_terminate):
    compounded_interest = compound(principal,year_terminate,asb_return)
    balance,payment,ppmt,ipmt = amortization(principal,loan_interest,loan_tenure,year_terminate)

    balance = float(balance[int(year_terminate*12) - 1])
    maturity = compounded_interest - balance
    return maturity
