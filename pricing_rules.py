def apply_bogof(product, count):
    price = product["price"]
    if count % 2 > 0:
        return ((count - 1) / 2 * price) + price
    else:
        return (count / 2) * price

def apply_bulk_discount(product, count):
    if count >= product["threshold"]:
        return (product["price"] * count) - (product["discount"] * count)
    else:
        return product["price"] * count

