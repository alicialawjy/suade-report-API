
'''
Data class used to read and extract data from the date of concern.
'''

import pandas as pd

class Data:
    def __init__(self):
        self.commissions = pd.read_csv('data/commissions.csv')
        self.order_lines = pd.read_csv('data/order_lines.csv')
        self.orders = pd.read_csv('data/orders.csv')

    def clean_order_csv_dates(self):
        '''
        order.csv uses 'created_at' column which combines the data and time of an order.
        This function extracts the date and appends it to the order DataFrame as an additional column. 
        '''
        self.orders['date'] = self.orders['created_at'].str.split(' ', n=1 ).str[0]
    
    def filter_for_date(self, date):
        '''
        This function extracts the rows that contain data from the date enquired.

        Input:
        - date (str): valid date in the form of YYYY-MM-DD
        '''
        self.clean_order_csv_dates()
        self.commissions = self.commissions[self.commissions['date']==date]
        self.orders = self.orders[self.orders['date']==date]
        order_ids_for_date = self.orders['id']
        self.order_lines = self.order_lines[self.order_lines['order_id'].isin(order_ids_for_date)]