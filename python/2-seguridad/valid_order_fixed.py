from collections import namedtuple

PurchaseOrder = namedtuple('PurchaseOrder', 'id, date, items')
LineItem = namedtuple('LineItem', 'kind, detail, amount, quantity', defaults=(1,))


def valid_order(po):
    """Returns an error text if the purchase order (po) is invalid,
    or list of products to ship if valid [(quantity, SKU), ...].
    """
    products = []
    net = 0
    for item in po.items:
        if item.kind == 'payment':
            if item.amount > 1e13:
                raise ValueError("Invalid payment")
            net += item.amount
        elif item.kind == 'product':
            if item.amount < 0.01:
                raise ValueError("Invalid product value")
            products.append(item)
            net -= item.amount * item.quantity
        else:
            raise ValueError("Invalid LineItem type: %s" % item.kind)
    if net != 0:
        raise ValueError("Payment imbalance: $%0.2f." % net)
    return products




# if __name__ == '__main__':

