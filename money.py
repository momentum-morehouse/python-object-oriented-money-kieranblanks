# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        return '{} {}' .format(self.name,self.digits)
        return '{} {}' .format(self.symbol,self.code)
        #return f"{self.name} of {self.digits}" 
        #return f"{self.symbol} of {self.code}"


    def __eq__(self, other): 
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)

class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        
        self.amount = amount
        self.currency = currency
        
       
        
    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol:
            return f"{self.currency.symbol}{self.amount:}{self.currency.digits}"
        else:
            return f"{self.currency.code}{self.amount:}{self.currency.digits}"


    def __repr__(self):
        return f"<Money {str(self.currency), str(self.amount)}>"

#def __repr__(self):
        #return {'name':self.name, 'age':self.age}

    


    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
    
        if self.currency == other.currency:
            return
            amount = self.amount + other.amount,
            currency = self.currency

        raise TypeError('DifferentCurrencyError')


    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """

        if self.currency == other.currency:
            return
            amount = self.amount - other.amount,
            currency = self.currency

        raise TypeError('DifferentCurrencyError')


    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        if self.currency == other.currency:
            return
            amount = self.amount * other.amount,
            currency = self.currency

        raise TypeError('DifferentCurrencyError')



    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        if self.currency == other.currency:
            return
            amount = self.amount / other.amount,
            currency = self.currency

        raise TypeError('DifferentCurrencyError')
