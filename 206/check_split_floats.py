import pytest

ndigit = 2

def _rnd(num):
    return round(num, ndigit)

def check_split(item_total, tax_rate, tip, people, expected ):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    #getcontext().prec=10
    total = _rnd(float(item_total.strip('$')))
    rate = _rnd(total * float(tax_rate.strip('%')) / 100)
    tips = _rnd((total + rate) * float(tip.strip('%')) / 100)
    grand_total = _rnd(total + rate + tips)
    print(f'Grand_total: {grand_total},{"+" * 10} Exp: {expected}')
    split = [_rnd(grand_total) / _rnd(people)] * people

    diff = grand_total - sum(split)
    while diff:
        print('Diff:', diff)
        if diff != 0:
            split[0] += diff
        diff = grand_total - sum(split)
        #print(f'---GrandT:{grand_total} -- Split:{sum(split)} -- Exp:{expected}')
    print('sum split: ', sum(split))
    sum_split = sum(split)
    return (f'${grand_total}', split)

# TESTS::
# args = [
#      (('$8.68', '4.75%', '10%', 3), '$10.00'),
#      (('$8.44', '6.75%', '11%', 3), '$10.00'),
#      (('$9.99', '3.25%', '10%', 2), '$11.34'),
#      (('$186.70', '6.75%', '18%', 6), '$235.17'),
#      (('$191.57', '6.75%', '15%', 6), '$235.18'),
#      (('$0.00', '0%', '0%', 1), '$0.00'),
#      (('$100.03', '0%', '0%', 4), '$100.03'),
#      (('$141.86', '2%', '18%', 9), '$170.75'),
#      (('$16.99', '10%', '20%', 1), '$22.43'),
#      (('$16.99', '10%', '20%', 2), '$22.43'),
#      (('$16.99', '10%', '20%', 3), '$22.43'),
#      (('$16.99', '10%', '20%', 4), '$22.43')
# ]

# for *arguments, expected in args:
#     total, tax_rate, tip, people = arguments[0]
#     check_split(total, tax_rate, tip, people, expected)


