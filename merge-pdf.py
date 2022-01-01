from pathlib import Path
from PyPDF2 import PdfFileMerger
import csv

folder_with_csv = Path("C:/Users/.Michal/Desktop/")
csv_file_name = "ideas.csv"

folder_with_pdfs = Path("C:/Users/.Michal/Desktop/")
pdf_file_format = '{name}.pdf'
pdf_result_file_name = "result.pdf"

pdfs = []
with open(folder_with_csv / csv_file_name, 'rt') as file:
    csv_file_content = csv.reader(file)
    for row in csv_file_content:
        person_name = row[0]
        pdf_file = pdf_file_format.format(name=person_name)
        pdfs.append(pdf_file)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

with open(folder_with_pdfs / pdf_result_file_name, "wb") as output:
    merger.write(output)
