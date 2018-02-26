class Checkout:
    def __init__(self, pricing_rules):
        self.basket = {}
        self.pricing_rules = pricing_rules

    def scan(self, product_code):
        if product_code not in self.basket:
            self.basket[product_code] = 1
        else:
            self.basket[product_code] += 1

    def calculate(self):
        total = 0
        for product_code, count in self.basket.items():
            product_total = self.calculate_product_total(product_code, count)
            total += product_total

        return round(total/100, 2)

    def calculate_product_total(self, product_code, count):
        product = self.pricing_rules[product_code]
        if product["rule"] == "BOGOF":
            return self.apply_bogof(product, count)
        elif product["rule"] == "Bulk discount":
            return self.apply_bulk_discount(product, count)
        else:
            return count * product["price"]

    def apply_bogof(self, product, count):
        price = product["price"]
        if count % 2 > 0:
            return ((count - 1) / 2 * price) + price
        else:
            return (count / 2) * price

    def apply_bulk_discount(self, product, count):
        if count >= product["threshold"]:
            return (product["price"] * count) - (product["discount"] * count)
        else:
            return product["price"] * count
