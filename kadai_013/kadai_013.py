def calc_tax(price: int, tax: int):
    total = price + price * tax / 100
    return total

tax_price = calc_tax(1000, 10)
print(f"消費税を含めた金額は{tax_price}円です")