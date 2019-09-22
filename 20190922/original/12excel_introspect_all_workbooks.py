#!/usr/bin/env python3   #파일명: 12excel_introspect_all_workbooks.py
import glob
import os
import sys
from xlrd import open_workbook

input_directory = sys.argv[1]   #파일을 지정하지 않고 파일이 위치한 디렉토리 경로를 지정한다.

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
	workbook = open_workbook(input_file)
	print('Workbook: {}'.format(os.path.basename(input_file)))
	print('Number of worksheets: {}'.format(workbook.nsheets))
	for worksheet in workbook.sheets():
		print('Worksheet name:', worksheet.name, '\tRows:',\
				worksheet.nrows, '\tColumns:', worksheet.ncols)
	workbook_counter += 1
print('Number of Excel workbooks: {}'.format(workbook_counter))
