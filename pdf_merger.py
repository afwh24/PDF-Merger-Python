import PyPDF2
import os
import sys

#Script current path
path = os.path.dirname(os.path.abspath(sys.argv[0]))
if(path != os.getcwd()): os.chdir(path)


merger = PyPDF2.PdfMerger()
if not (os.path.exists(f"{path}/PDF input")): os.makedirs(f"{path}/PDF input")
if not (os.path.exists(f"{path}/PDF output")): os.makedirs(f"{path}/PDF output")

counter = 0

while True:
    #Only perform PDF merger when > 1 PDF files
    if(len(os.listdir(f"{path}/PDF input")) > 1):
        for file in os.listdir(f"{path}/PDF input"):
            if file.endswith(".pdf"):
                merger.append(f"{path}/PDF input/{file}")    


        #Combined PDF naming conventions
        if counter == 0: 
            merger.write(f"{path}/PDF output/combinedPDF.pdf")

        else: 
            merger.write(f"{path}/PDF output/combinedPDF({counter}).pdf")

        counter += 1

        print("PDF files have been successfully combined\n")

    #Less than 2 PDF files in input folder
    else:
        print("Your PDF input folder has insufficient files to combine\n")

    #User control
    print("=== Menu ===")
    print("Rename the PDF files into the order of PDF combination")
    print("0: Terminate the program")
    userInput = int(input("Input: "))
    if userInput == 0: break