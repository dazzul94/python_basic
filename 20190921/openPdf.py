import PyPDF2
import re

pdfFileObj = open('pdf/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.numPages
pageObj = pdfReader.getPage(0)

text = str(pageObj.extractText())
print(text)
quotes = re.findall(r'"[^"]*"', text)
for quote in quotes:
    print(quote)
    print()
# print(pageObj.extractText())

# cmd> python openPdf.py

