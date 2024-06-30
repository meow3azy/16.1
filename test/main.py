from utils.product import Product
from utils.category import Category


def main():
    category = Category()

    category.add_product(Product("Яблоко", 50))
    category.add_product(Product("Банан", 30))
    category.add_product(Product("Апельсин", 20))

    category.print_average_price()

    category.products.clear()

    category.print_average_price()
    try:
        product1 = Product("Яблоко", 50)
        print(f"Добавлен продукт: {product1.name}, количество: {product1.quantity}")

        product2 = Product("Груша", 1, 0)
        print(f"Добавлен продукт: {product2.name}, количество: {product2.quantity}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
