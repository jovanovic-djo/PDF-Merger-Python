from PyPDF2 import PdfMerger

pdfs = []
# Write all pdf files you want to merge in 'pdfs' array
# For example: pdfs = ["book1.pdf", "book2.pdf", "book3.pdf"]

merger = PdfMerger()

for i in pdfs:
    merger.append(i)

merger.write("Final.pdf")

merger.close()
