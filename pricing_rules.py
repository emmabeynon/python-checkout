class PricingRules:
    def list(self):
        return {
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
