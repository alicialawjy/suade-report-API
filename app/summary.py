'''
Summary Class used to create the report summary.
Inputs to the Summary functions are DataFrame objects.
'''

import pandas as pd

class Summary:
    def __init__(self):
        self.number_of_items_sold = 0
        self.number_of_customers = 0
        self.total_discount = 0
        self.ave_discount_rate = 0
        self.number_of_orders = 0
        self.total_commission = 0
        self.ave_commission = 0

    def get_number_of_orders(self, order_df):
        '''
        Populates the total number of orders executed on that day.
        '''
        self.number_of_orders = len(order_df)
        return self.number_of_orders
    
    def get_number_of_items_sold(self, order_lines_df):
        '''
        TASK 1:
        Populates total number of items sold on that day.
        '''
        self.number_of_items_sold = sum(order_lines_df['quantity'])
        return self.number_of_items_sold
    
    def get_number_of_customers(self,order_df):
        '''
        TASK 2:
        Populates total number of customers that made an order that day.
        '''
        self.number_of_customers = len(pd.unique(order_df['customer_id']))
        return self.number_of_customers
    
    def get_total_discount(self, order_lines_df):
        '''
        TASK 3:
        Populates total amount (value) of discount given that day.
        '''
        self.total_discount = sum(order_lines_df['full_price_amount'] - order_lines_df['discounted_amount'])
        return self.total_discount
    
    def get_ave_discount_rate(self, order_lines_df):
        '''
        TASK 4:
        Populates average discount rate applied to the items sold that day.
        '''
        total_discount_rate = sum(order_lines_df['discount_rate']* order_lines_df['quantity'])
        self.ave_discount_rate = total_discount_rate/self.number_of_items_sold
    
        return self.ave_discount_rate

    def get_ave_order_total(self, order_lines_df):
        '''
        TASK 5:
        Populates the average order total for that day
        '''
        total_order = sum(order_lines_df['total_amount'])
        self.ave_order_total = total_order/ self.number_of_orders
    
        return self.ave_order_total

    def get_commission_total_and_ave(self,order_lines_df, order_df, commission_df):
        '''
        TASK 6:
        Populates the total amount of commissions generated that day.
        '''
        # sum the totals based on the order_ids to get the order total
        order_id_and_total = order_lines_df[['order_id','total_amount']].groupby('order_id').sum() # order totals
        # append the vendor_id corr to the order_id
        merge_vendor_id = order_id_and_total.merge(order_df, left_on='order_id',right_on='id')
        # sum the order totals based on the vendor_id
        vendor_id_and_total = merge_vendor_id[['vendor_id','total_amount']].groupby('vendor_id').sum() # vendor totals
        # append the commission rate corr to the vendor_id
        merge_commission_rate = vendor_id_and_total.merge(commission_df,on='vendor_id',how='left')
        
        # compute commissions
        self.total_commission = sum(merge_commission_rate['total_amount']*merge_commission_rate['rate'])
        self.ave_commission = self.total_commission/ self.number_of_orders
    
        return self.total_commission, self.ave_commission

    def get_summary(self, data):
        '''
        Populate the Summary object.
        NOTE: report does not include total amount of commissions earned per promotion (sorry!)

        Input:
        - data: Data class obj
            Contains data which has already been filtered to only contain 
            information about the date being enquired.

        Returns:
        - summary: dict
        '''
        self.get_number_of_orders(data.orders)
        self.get_number_of_items_sold(data.order_lines)
        self.get_number_of_customers(data.orders)
        self.get_total_discount(data.order_lines)
        self.get_ave_discount_rate(data.order_lines)
        self.get_ave_order_total(data.order_lines)
        self.get_commission_total_and_ave(data.order_lines, data.orders, data.commissions)

        return {
            "customers": self.number_of_customers, 
            "total_discount_amount": self.total_discount,
            "items": self.number_of_items_sold,
            "order_total_avg": self.ave_order_total,
            "discount_rate_avg": self.ave_discount_rate,
            "commissions": {
                "total": self.total_commission,
                "order_average": self.ave_commission 
                }
            }

