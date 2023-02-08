'''
This is a simplified unit test.
Ideally I would test the API responses and the Data class as well. 
'''
import pandas as pd
from summary import Summary

# Create dummy variables to test
test_order_data = {'id':[1,2],
            'date':['2023-01-01','2023-01-01'],
            'vendor_id': [1,2],
            'customer_id':[1,1]}

test_order_line_data = {'order_id':[1,1,2,2],
                        'quantity':[1,1,1,1],
                        'full_price_amount':[5,5,5,5],
                        'discounted_amount':[4,4,4,4],
                        'total_amount':[4.5,4.5,4.5,4.5],
                        'discount_rate':[0.25,0.25,0.25,0.25]}

test_commission_data = {'date':['2023-01-01','2023-01-01'],
                        'vendor_id':[1,2],
                        'rate':[0.1,0.2]}

order_df = pd.DataFrame(data=test_order_data)
order_line_df = pd.DataFrame(data=test_order_line_data)
commission_df = pd.DataFrame(data=test_commission_data)
summary = Summary()

def test_get_number_of_orders():
    assert summary.get_number_of_orders(order_df) == 2

def test_get_number_of_items_sold():
    assert summary.get_number_of_items_sold(order_line_df) == 4

def test_get_number_of_customers():
    assert summary.get_number_of_customers(order_df) == 1

def test_get_total_discount():
    assert summary.get_total_discount(order_line_df) == 4

def test_get_ave_discount_rate():
    assert summary.get_ave_discount_rate(order_line_df) == 0.25

def test_get_ave_order_total():
    assert summary.get_ave_order_total(order_line_df)==9
    
def test_get_commission_total_and_ave():
    assert summary.get_commission_total_and_ave(order_line_df, order_df, commission_df)==(2.7,1.35)

if __name__=="__main__":
    test_get_number_of_orders()
    test_get_number_of_items_sold()
    test_get_number_of_customers()
    test_get_total_discount()
    test_get_ave_discount_rate()
    test_get_ave_order_total()
    test_get_commission_total_and_ave()