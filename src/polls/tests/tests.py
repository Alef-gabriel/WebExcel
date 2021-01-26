import os
import pandas as pd
from django.test import TestCase
from django.test import Client

c = Client()
response = c.post('/')
print(response.status_code)

f = 'C:/Users/alefg/projects/webExcel/src/polls/tests/xlsTest.xlsx'
file = {'fileXls': f }
xls = pd.read_excel(f)
print(xls.head())


