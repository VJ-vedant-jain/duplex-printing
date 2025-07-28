import pymupdf as pdf
import os

def get_two_files(path):
    path = path.strip().replace('\\', '/')

    if path.endswith('.pdf'):
        file = pdf.open(path)
    else:
        return "[ERROR]: Provided path is not a pdf"

    base_dir = os.path.dirname(__file__)
    temp_dir = os.path.join(base_dir, "temp")
    os.makedirs(temp_dir, exist_ok=True)


    doc1 = pdf.open()
    for page_index in range(0, len(file), 2):
        doc1.insert_pdf(file, from_page=page_index, to_page=page_index)
    doc1.save(os.path.join(temp_dir, 'first_run.pdf'))
    doc1.close()

    doc2 = pdf.open()
    if len(file)%2 != 0:
        doc2.new_page(width = file[0].rect.width, height = file[0].rect.height)
    for page_index in reversed(range(1, len(file), 2)):
        doc2.insert_pdf(file, from_page=page_index, to_page=page_index)
    doc2.save(os.path.join(temp_dir, 'second_run.pdf'))
    doc2.close()

    file.close()
    
    return "[DEBUG]: Splitting ended successfully"