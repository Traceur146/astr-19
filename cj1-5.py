import numpy as np
from tabulate import tabulate
from astropy.table import Table

def sinx():
    x = np.linspace(0, np.pi, 1000)
    y = np.sin(x)
    table_data = [(a, b) for a,b in zip(x, y)]
    table_headers = ['x', 'y']
    print(tabulate(table_data, tablefmt='grid', headers=table_headers, floatfmt='.3f'))

sinx()