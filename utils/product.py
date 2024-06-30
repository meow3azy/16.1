class Product:
    def __init__(self, name, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Количество товара должно быть больше нуля.")
        self.name = name
        self.price = price
        self.quantity = quantity