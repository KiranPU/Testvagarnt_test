
products_in_basket = [
    {"name": "leather wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"name": "umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"name": "cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"name": "honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2},
]


def calculate_gst_amount(unit_price, gst_percentage, quantity):
    gst_amount = (unit_price * gst_percentage / 100) * quantity
    return gst_amount


for product in products_in_basket:
    if product["unit_price"] > 500:
        product["unit_price"] *= 0.95  


max_gst_amount = 0
max_gst_product = None

for product in products_in_basket:
    gst_amount = calculate_gst_amount(product["unit_price"], product["gst_percentage"], product["quantity"])
    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product

if max_gst_product:
    print("Product with the maximum GST amount:", max_gst_product["name"])
else:
    print("No product found in the basket")


total_amount = sum((p["unit_price"] * p["quantity"]) + calculate_gst_amount(p["unit_price"], p["gst_percentage"], p["quantity"]) for p in products_in_basket)
print("Total amount to be paid to the shopkeeper:", round(total_amount, 2))