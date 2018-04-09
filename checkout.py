from pricing_rules import apply_bogof, apply_bulk_discount

class Checkout:
    def __init__(self, pricing_rules):
        self.basket = {}
        self.pricing_rules = pricing_rules

    def scan(self, product_code):
        # Use the .get() method's default argument when product isn't in basket.
        # Alternatively we could use a defaultdict.
        self.basket[product_code] = self.basket.get(product_code, 0) + 1

    def calculate(self):
        # You can just combine sum() and a generator to calculate the total directly.
        total = sum(self.calculate_product_total(code, count) for code, count in self.basket.items())

        # Hope you're not siphoning those shaved-off fractions of a penny into an
        # account in the Caiman Islands :p
        return round(total/100, 2)

    def calculate_product_total(self, product_code, count):
        # Assume a default rule of 'none' if there isn't one defined for the product.
        rule = self.pricing_rules[product_code].get('rule', 'none')

        # Take advantage of being able to pass functions/lambdas around like objects
        # We can also declare a dict and use it straight away!
        rule_fn = {
            'BOGOF': apply_bogof,
            'Bulk discount': apply_bulk_discount,
            'none': lambda product, count: count * product['price']
        }[rule]

        return rule_fn(product_code, count)

