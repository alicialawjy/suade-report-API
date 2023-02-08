from datetime import datetime
from data import Data
from summary import Summary

def valid_date(date_str):
    '''
    Checks if the date is in the valid YYYY-MM-DD format
    date [str]
    '''
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True

    except ValueError:
        return False

def build_summary(date):
    '''
    Builds the summary.

    Input:
    - date (str): valid date in the form of YYYY-MM-DD
    
    Returns:
    - The summary (dict): summary is returned if records from that date exists, OR
    - Response (str): a statement notifying users that no records of those dates exist.
    '''
    data = Data()
    data.filter_for_date(date)

    if len(data.orders):                    # perform checks only if data exists
        summary = Summary()
        return summary.get_summary(data)
    
    else:
        return "no entries for this date"

