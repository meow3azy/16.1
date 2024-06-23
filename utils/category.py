from product import Product

class Category:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            count = len(self.products)
            if count == 0:
                raise ZeroDivisionError
            return total_price / count
        except ZeroDivisionError:
            return 0
