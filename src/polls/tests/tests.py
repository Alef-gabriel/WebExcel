import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from django.test import TestCase
from django.test import Client

c = Client()
response = c.post('/')
print(response.status_code)

f = 'C:/Users/alefg/projects/webExcel/src/polls/tests/xlsTest.xlsx'
xls = pd.read_excel(f)
print(xls.head())

def ok(file):
    xls = pd.read_excel(file)
    xls["mult"] = xls["tt"] * 2
    writer = ExcelWriter('Pandas-Example2.xlsx')
    return writer.save()

ok(f)
