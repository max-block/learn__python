from decimal import Decimal


def convert_to_float():
    d = Decimal("123.123")
    print(d, type(d))  # 123.123 <class 'decimal.Decimal'>
    f = float(d)
    print(f, type(f))  # 123.123 <class 'float'>


def is_fractional_number():
    d1 = Decimal("123.123")
    print(d1 == d1.to_integral_value())  # False

    d2 = Decimal("123")
    print(d2 == d2.to_integral_value())  # True

    d3 = Decimal("123.0")
    print(d3 == d3.to_integral_value())  # True


if __name__ == "__main__":
    # convert_to_float()
    is_fractional_number()
