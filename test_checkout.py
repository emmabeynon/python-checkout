from checkout import Checkout

rules = {
            "FR1": {
                "price": 311,
                "rule": "BOGOF"
            },
            "SR1": {
                "price": 500,
                "rule": "Bulk discount",
                "threshold": 3,
                "discount": 50
            },
            "CF1": {
                "price": 1123,
                "rule": "none"
            }
        }

class TestCheckout:
    def test_three_fruit_teas_one_strawberries_one_coffee(self):
        co = Checkout(rules)
        co.scan("FR1")
        co.scan("SR1")
        co.scan("FR1")
        co.scan("FR1")
        co.scan("CF1")
        assert co.calculate() == 22.45

    def test_two_fruit_teas(self):
        co = Checkout(rules)
        co.scan("FR1")
        co.scan("FR1")
        assert co.calculate() == 3.11

    def test_three_strawberries_one_fruit_tea(self):
        co = Checkout(rules)
        co.scan("SR1")
        co.scan("SR1")
        co.scan("FR1")
        co.scan("SR1")
        assert co.calculate() == 16.61
