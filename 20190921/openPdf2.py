import PyPDF2

pdfFile = open('pdf/encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
pdfReader.decrypt('rosebud') #password

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

print("페이지: ", pdfReader.numPages)
print("=============================================")

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

# cmd> python openPdf2.py