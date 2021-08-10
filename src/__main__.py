
#                       CUPS - Python - HTML to PDF
#                   
#
#                       Zheng Lin Lei - Apache 2.0
#
#
#          https://github.com/ZhengLinLei/cups-python-printer

import cups
import pdfkit # HTML to PDF
# ! Remmenber to install wkhtmltopdf 
# $ sudo apt-get install wkhtmltopdf
#

import uuid # TMP filename

import os


class PrintFile():

    files = []
    printer = 0

    def __init__(self) -> None:

        # Connect to CUPS
        self.conn = cups.Connection()
        self.printers = self.conn.getPrinters()

    def addFile(self, filepath, name, options):

        self.files.append([filepath, name, options])

    def choosePrinter(self, indexNum):

        for index, printer in enumerate(self.printers):

            print(index, printer, self.printers[printer]["device-uri"])

        self.printer = indexNum


    def printAll(self):

        if self.files:
            # Get the default or choosed printer
            printer_name = list(self.printers.keys())[self.printer]


            # Foreach the files array
            for file in self.files:
                self.conn.printFile (printer_name, file[0], file[1], file[2] if file[2] else {})


            return True
        else:
            print('ERROR: Nothing to print in the List')
            return False






# Print HTML with styles
# Special for receipt thermal printer

class PrintHTML():
    
    def __init__(self, temp, options) -> None:
        
        self.PrintRoot = PrintFile()
        self.temp = temp

        defaultOptions = {
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
        }


        self.options = options if options else defaultOptions

    def convertFile(self, filename, name, option):

        pdfkit.from_file(f'{filename}.html', f'{filename}.pdf', self.options)

        self.PrintRoot.addFile(f'{filename}.pdf', name, option)



    def removeFile(self, arrFile):

        for file in arrFile:

            os.remove(file)


    def addHTML(self, text, name, option):
        
        filename = f"{self.temp}/{str(uuid.uuid4())}"

        # Add html text
        file = open(f"{filename}.html","w")

        file.write(text)

        file.close()


        # Convert
        self.convertFile(filename, name, option)

        # Remove file
        self.removeFile([f'{filename}.html'])

    def choosePrinter(self, indexNum):

        for index, printer in enumerate(self.PrintRoot.printers):

            print(index, printer, self.PrintRoot.printers[printer]["device-uri"])

        self.PrintRoot.printer = indexNum

    def addFile(self, filepath, name, option):

        filename = filepath.replace('.html', '')

        # Convert
        self.convertFile(filename, name, option)

    def addUrl(self, url, name, option):

        filename = f"{self.temp}/{str(uuid.uuid4())}"

        pdfkit.from_url(url, f'{filename}.pdf')

        self.PrintRoot.addFile(f'{filename}.pdf', name, option)


    def printAll(self):

        res = self.PrintRoot.printAll()

        # delete all tmp pdf file
        rFiles = [x[0] for x in self.PrintRoot.files]
        self.removeFile(rFiles)

        return res




# aa = PrintFile()

# aa.addFile('./test/test.pdf', 'Test', options = {
#     'page-height': '210mm',
#     'page-width': '80mm',
# })

aa = PrintHTML('./tmp', options = {
    'page-height': '210mm',
    'page-width': '72mm',
    'margin-right': '1mm',
    'margin-left': '1mm',
    'encoding': "UTF-8",

})

aa.addFile('./test/test.html', 'Test', {})

# print(aa.options)

# aa.choosePrinter(0)


print(aa.printAll())
    