import PyPDF2

# 기본 pdf 열어서 첫페이지 찾기
pdfFile = open('pdf/meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfFirstPage = pdfReader.getPage(0)

# 워터마크 pdf 열어서 기본페이지 첫페이지에 머지 
pdfWatermarkReader = PyPDF2.PdfFileReader(open('pdf/watermark.pdf','rb'))
pdfFirstPage.mergePage(pdfWatermarkReader.getPage(0))

# 파일 쓰기
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pdfFirstPage)

# 첫페이지 제외한 나머지 페이지 추가
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# 새로운 파일 생성
pdfOutputFile = open('merge_watermark.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()
print("작업이완료되었고 파일이 저장되었습니다.")

# cmd> python openPdf6.py