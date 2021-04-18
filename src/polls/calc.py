import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def test(file):
    xls = pd.read_excel(file)
    xls["mult"] = xls["tt"] * 2
    writer = ExcelWriter('Pandas-Example2.xlsx')
    return writer.save()