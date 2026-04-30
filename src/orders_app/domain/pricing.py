from typing import Protocol


class PricingStrategy(Protocol):
    def calculate(self, base_price: float) -> float:
        ...


class NormalPricing:
    def calculate(self, base_price: float) -> float:
        return base_price


class DiscountPricing:
    def __init__(self, discount: float):
        self.discount = discount

    def calculate(self, base_price: float) -> float:
        return base_price * (1 - self.discount)


class TaxPricing:
    def __init__(self, tax: float):
        self.tax = tax

    def calculate(self, base_price: float) -> float:
        return base_price * (1 + self.tax)      