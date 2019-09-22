#!/usr/bin/env python3     #파일명: 3pandas_parsing_and_write_keep_dates.py
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

# cmd> python 3pandas_parsing_and_write_keep_dates.py sales_2013.xlsx ./output/3pandas.xls
