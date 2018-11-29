from __future__ import print_function
from objects.base.object import Object
from objects.exceptions.exceptions import *


class Account(Object):
    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

        self._balance = 0.0

    @property
    def balance(self):
        return self._balance



class Budget(Object):


    def __init__(self, **kwargs):
        super(Budget, self).__init__(**kwargs)

        self._balance = 0.0
        self._obligations = []
        self._transactions = []
        self._salary = 40.74*108*2 #encoded lol
        self._monthly = {}
        self.test_dog = "Derp"

        self.save_info.extend(["_monthly", "test_dog"])
        self._perc_savings = 25
        self._perc_giving  = 10

        self._monthly["rent"] =     BudgetItem( 1600, "rent", 1 )
        self._monthly["odyssey"]  = BudgetItem( 590, "car loan", 21)
        self._monthly["spotify"]  = BudgetItem( 15, "spotify", 21)
        self._monthly["hbo"]      = BudgetItem( 15, "hbo", 21)
        self._monthly["internet"] = BudgetItem( 65, "internet", 21)

        self._realm.io.update_table( self )

    def add(self, amount, description):
        transaction = Transaction(amount=amount, description=description)
        if transaction.id not in [o.id for o in self._transactions]:
            self._transactions.append( transaction )
        else:
            raise UniqueMembershipException("This transaction is already in this budget.")

    def actualize(self):
        self._balance = self._salary
        self._balance -= sum(v.amount for k,v in self._monthly.iteritems())
        self._balance += sum(i.amount for i in self._transactions)
        return self._balance

    def breakdown(self, monthly_number):
        print("$%.2f a month.\n$%.2f every 2 weeks.\n$%.2f every week.\n$%.2f every day.\n" %(monthly_number, monthly_number/2, monthly_number/4, monthly_number/30 ))
        print("Ends up being:\n$%.2f every year.\n$%.2f every 5 years.\n$%.2f until you retire" % (monthly_number*12, monthly_number*12*5, monthly_number*12*25))

    def report(self):
        print("*"*20)
        print("Income Total:\t$%.2f" %self._salary)


class BudgetItem(Object):

    @property
    def date(self):
        return self._draft_date


    @date.setter
    def date(self, day):
        if -1 < day < 32:
            self._draft_date = day
        else:
            raise ValueError("Day number out of monthly range. Please use 1-31")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amt):
        self._amount = amt

    def __init__(self, amount=None, category=None, day=None,  **kwargs):
        super(BudgetItem, self).__init__(**kwargs)
        self._amount = 0.0
        self._draft_date = None

        if amount:
            self.amount = amount
        if category:
            self.category = category
        if day:
            self.date = day


class Transaction(Object):
    def __init__(self, amount=None, **kwargs):
        super(Transaction, self).__init__(**kwargs)
        self.amount = 0.0
        if amount:
            self.amount = amount

    def __add__(self, other):
        if other.type == self.type:
            return getattr(self, "_amount") + getattr(other, "_amount")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amt):
        self._amount = amt




