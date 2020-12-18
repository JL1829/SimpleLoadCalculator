# Author: Johnny Lu
# Contact: joh@johdev.com
# Copyright: Johnny Lu
# LICENSE: MIT
import math


class LoanCalculator:
    """
    Load calculator
    """
    def __init__(self):
        self.principal = None
        self.annuity = None
        self.period = None
        self.diff = None
        self.overpayment = None

    def __repr__(self):
        return f"Principal = {self.principal}\n" \
               f"Annuity = {self.annuity}\n" \
               f"Period = {self.period}\n" \
               f"Diff = {self.diff}\n" \
               f"Overpayment = {self.overpayment}"

    def getPeriod(self, interest):
        interest = interest / 100 / 12
        temp = self.annuity / (self.annuity - interest * self.principal)
        self.period = math.ceil(math.log(temp, 1 + interest))
        self.overpayment = self.annuity * self.period - self.principal
        return self.period, self.overpayment

    def getAnnuityAmount(self, interest):
        interest = interest / 100 / 12
        num = interest * math.pow((1 + interest), self.period)
        den = math.pow((1 + interest), self.period) - 1
        self.annuity = math.ceil(self.principal * (num / den))
        self.overpayment = self.annuity * self.period - self.principal
        return self.annuity, self.overpayment

    def getPrincipal(self, interest):
        interest = interest / 100 / 12
        num = interest * math.pow((1 + interest), self.period)
        den = math.pow((1 + interest), self.period) - 1
        self.principal = math.floor(self.annuity / (num / den))
        self.overpayment = self.annuity * self.period - self.principal
        return self.principal, self.overpayment

    def getDiff(self, interest):
        interest = interest / 100 / 12
        self.diff = []
        for i in range(1, self.period + 1):
            self.diff.append(
                math.ceil(self.principal / self.period + interest * (self.principal
                                                                     - self.principal * (i - 1) / self.period))
            )
        self.overpayment = sum(self.diff) - self.principal
        return self.diff, self.overpayment
