class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
        return f"Nowa cena {self.name}: {self.price:.2f} zł"

produkt = Product("Laptop", 3000)
print(produkt.apply_discount(10)) 
