import PyPDF2

minutesFile = open('pdf/meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

# 90도 회전
page = pdfReader.getPage(0)
# page.rotateClockwise(90)
page.rotateClockwise(180)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

# resultPdfFile = open('rotate1.pdf', 'wb')
resultPdfFile = open('rotate2.pdf', 'wb')

pdfWriter.write(resultPdfFile)
resultPdfFile.close()
