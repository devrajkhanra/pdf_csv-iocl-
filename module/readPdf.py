# ./modules/readPdf.py

# creating a pdf reader object
import PyPDF2

# Return pdf reader object
def read_PDF(path):
    # creating a pdf file object
    pdfFileObj = open(path, "rb")

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    return pdfReader

# Return no of pages in the pdf file
def get_Pages(pdfReaderObject):
    
    # printing number of pages in pdf file
    pages = len(pdfReaderObject.pages)
    return pages

# Return the whole pdf as list of list, where every line is a list
def pdf_List(pdfReaderObject, pages):
    result = []
    for i in range(pages):
    
        pageObj = pdfReaderObject.pages[i]

        
        text = pageObj.extract_text().split('\n')
        
        for i in range(len(text)):
                # Printing the line
                # Lines are seprated using "\n"
                # print(text[i],end=" ")
                # print('Text: ',text[i], ' Type: ',type(text[i]))
                
                word = text[i].split(' ')
                result.append(word)

    return result