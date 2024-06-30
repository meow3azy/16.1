from utils.product import Product

class Category:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def average_price(self):
        total_price = sum(product.price for product in self.products)
        count = len(self.products)
        if count == 0:
            return 0
        return total_price / count

    def print_average_price(self):
        avg_price = self.average_price()
        if avg_price == 0:
            print("В категории нет товаров.")
        else:
            print(f"Средний ценник: {avg_price:.2f}")
