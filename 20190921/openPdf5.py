import PyPDF2

pdf1File = open('pdf/meetingminutes.pdf','rb')
pdf2File = open('pdf/meetingminutes2.pdf','rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('merge.pdf', 'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()

pdf1File.close()
pdf2File.close()

print("작업이 완료되었습니다.")
print("파일이 저장되었습니다.")