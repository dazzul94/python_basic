#!/usr/bin/env python3          #파일명: 1excel_introspect_workbook.py
import sys

# xlrd 모듈에서 open_workbook()함수를 임포트하여 엑셀파일을 읽고 파싱(분석)
from xlrd import open_workbook

# 사용자가 엑셀파일을 지정한다.
input_file = sys.argv[1]

# 사용자가 지정한 엑셀파일을 읽고 파싱(분석)
workbook = open_workbook(input_file)

# 워크시트 숫자를 출력
print('Number of worksheets:', workbook.nsheets)

# for 반복문으로 모든 워크시트를 반복한다.
# sheets()함수는 통합엑셀문서의 개별 워크시트를 식별한다.
for worksheet in workbook.sheets():

        # 각 워크시트의 이름과 행 & 열 수를 출력한다.
	print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)

# cmd> python 1excel_introspect_workbook.py sales_2013.xlsx
# cmd> python 1excel_introspect_workbook.py sales_2014.xlsx
# cmd> python 1excel_introspect_workbook.py sales_2015.xlsx














