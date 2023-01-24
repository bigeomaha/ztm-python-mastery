import PyPDF2
import sys
import os

inputs = sys.argv[1:]

def pdf_watermarker(pdf_list):
    template = PyPDF2.PdfReader('./files/wtr.pdf')
    watermark = template.pages[0]
    save_file = PyPDF2.PdfWriter()
    for file in pdf_list:
        head, tail = os.path.split(file)
        output_file_name = "./files/wtr_" + tail
        in_file = PyPDF2.PdfReader(file)
        for page in in_file.pages:
            page.merge_page(watermark)
            save_file.add_page(page)

        save_file.write(output_file_name)
        save_file.close()

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write('./files/combined.pdf')
    merger.close()

pdf_watermarker(inputs)
