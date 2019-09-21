import PyPDF2

pdfFile = open('pdf/encrypted.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
pdfReader.decrypt('rosebud')

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# -----------------------------------------------------------

pdfWriter.encrypt('banana')
resultPdf = open('encrypted2.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

print("작업이 완료되었습니다")
print("파일이 저장되었습니다")

# cmd> python openPdf3.py