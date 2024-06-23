from product import Product
from category import Category

def main():
    category = Category()

    # Добавление товаров в категорию
    category.add_product(Product("Яблоко", 50))
    category.add_product(Product("Банан", 30))
    category.add_product(Product("Апельсин", 20))

    print("Средний ценник:", category.average_price())

    # Удаление всех товаров для демонстрации ZeroDivisionError
    category.products.clear()

    print("Средний ценник после удаления всех товаров:", category.average_price())

if __name__ == "__main__":
    main()
