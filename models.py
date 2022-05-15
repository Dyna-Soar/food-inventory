# Food models

class Food:
    def __init__(self, price, vat, category, amount=0):
        self.price = price
        self.amount = amount
        self.vat = vat
        self.final_price = price * (1+vat)
        self.category = category
