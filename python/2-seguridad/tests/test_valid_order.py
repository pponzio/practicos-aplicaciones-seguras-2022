import pytest
from valid_order import LineItem, PurchaseOrder, valid_order


def test_valid_order():
    tv = LineItem(kind='product', detail='BigTV', amount=10000.00)
    paid = LineItem(kind='payment', detail='CC#12345', amount=10000.00)
    goodPO = PurchaseOrder(id='777', date='6/16/2022', items=[tv, paid])
    res = valid_order(goodPO)
    assert len(res) == 1
    assert res[0].kind == 'product'
    assert res[0].detail == 'BigTV'
    assert res[0].amount == 10000.00


def test_unpaid_order():
    tv = LineItem(kind='product', detail='BigTV', amount=10000.00)
    unpaidPO = PurchaseOrder(id='888', date='6/16/2022', items=[tv])
    with pytest.raises(ValueError) as exc_info:
        valid_order(unpaidPO)


def test_malicious_order():
    fake1 = LineItem(kind='payment', detail='FAKE', amount=1e30)
    fake2 = LineItem(kind='payment', detail='FAKE', amount=-1e30)
    tv = LineItem(kind='product', detail='BigTV', amount=10000.00, quantity=1000)
    nonpayment = [fake1, tv, fake2]
    fraudPO = PurchaseOrder(id='999', date='6/16/2022', items=nonpayment)
    res = valid_order(fraudPO)
    assert len(res) == 1
    assert res[0].kind == 'product'
    assert res[0].detail == 'BigTV'
    assert res[0].amount == 10000.00
    assert res[0].quantity == 1000