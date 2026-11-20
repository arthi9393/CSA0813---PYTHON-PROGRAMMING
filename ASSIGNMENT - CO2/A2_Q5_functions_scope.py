def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    return amount + gst, gst

print("Buggy:", add_item_buggy("Tea"), add_item_buggy("Vada"))
print("Correct:", add_item("Tea"), add_item("Vada"))
print("Defaults:", add_item_buggy.__defaults__)
total, gst = bill(200, gst_rate=0.05)
print(f"Total including GST: {total:.2f}; GST: {gst:.2f}")

global_count = 0
def update_global():
    global global_count
    global_count += 1
update_global()
print("Global count:", global_count)

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    return count
print("Nonlocal count:", outer())
