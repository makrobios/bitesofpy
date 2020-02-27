from math import floor, ceil

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    # default case
    func = ceil 
    if up == False:
        func = floor
    return list( map(func, transactions) )