# Program: PDF Separate and Merge Application with PyPDF2
#           This app for three main functions[Merge two files, Extract a page from file, Split file into separate pages]
#           and to do it we used PyPDF library by using PdfReader, PdfWriter built-in functions and to check the path
#           of files error used PyPDF2.errors by using PyPdfError built-in function
# Authors: Ahmed Atef ( Developed the Merger function )
#          Kirollos Adel Samir ( Developed the split files & main & options functions and the all validation of the program)
#          Mina Maher ( Developed the extract file function )
# Version: 3.0
# Date: 2 / 27 / 2024


from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PyPdfError


# Merge two files function
def merger(file1, file2, new_file_name):
    merger = PdfWriter()
    pdfs = [rf'{file1}.pdf', rf'{file2}.pdf']  # Read tow input pdf files
    for pdf in pdfs:
        merger.append(pdf)  # Add two files to merge them
    merger.write(f"merged-{new_file_name}.pdf")  # The merged pdf file


# extract a page from pdf file function
def extract_file(filename, pagenum):
    reader_pdf = PdfReader(f"{filename}.pdf")  # Read the input pdf file
    reader = reader_pdf.pages[pagenum - 1]  # Get the number of pages
    writepage = PdfWriter()  # create a new PDF
    writepage.add_page(reader)  # Add the extract file
    output = open(f'{filename}-{pagenum}.pdf', 'wb')  # save the pages in new file
    writepage.write(output)  # close output file




# Split a new pdf file function
def split_pdf(file_name,new_file_name):
    reader = PdfReader(f"{file_name}.pdf")
    # Split code
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{new_file_name} {i + 1}.pdf", "wb") as file_output:
            writer.write(file_output)
            file_output.close()

# The option function
def options(num):
    global page_number
    if num == 1:  # Merge two files
        file1 = input("Enter the name of the file one: ")
        file2 = input("Enter the name of the file two: ")
        new_file = input("Enter the new output file name: ")
        merger(file1, file2, new_file)
    elif num == 2:  # Extract a page from file
        file = input("Enter the name of the file: ")
        reader_pdf = PdfReader(f"{file}.pdf")
        pages = len(reader_pdf.pages)
        print(f"Number of {file}.pdf pages: {pages}")
        while True:  # Loop Validation
            try:
                page_number = int(input("Enter the page number: "))
            except:
                print("Error! Insert a valid page number")
                continue
            if page_number < 0:
                print("Error! Insert a valid page number")
                continue
            if page_number <= pages and page_number != 0:
                extract_file(file, page_number)
            else:
                print("Error! Insert a valid page number")
                continue
            break

    elif num == 3:  # Split file into separate pages
        file = input("Enter the name of the file: ")
        new_file = input("Enter the new output file name: ")
        split_pdf(file, new_file)
    else:
        print("Error! Please insert a valid option")


Menu = """
1) Merge two files 
2) Extract a page from file
3) Split file into separate pages
4) Exit """


def main():
    while True:
        print("Wellcome to PDF app")
        print("Please choose from the following options")
        print(Menu)
        try:
            user_op = int(input("=> "))
        except:
            print("Error! Please insert a valid option")
            continue
        if user_op == 4:
            print("EXIT")
            break
        try:
            options(user_op)
        # This block of code checks if the pdf file in the dictionary or not
        except OSError as error:
            print(f"Error!: {error.filename}: {error.strerror}")
        # except PyPdfError as error:
        #     print(f"Error!: PyPdf2:", *error.args)
main()