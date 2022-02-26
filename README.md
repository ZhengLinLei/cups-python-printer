# CUPS Python Printer Software

Window users [https://github.com/ZhengLinLei/windows-python-printer](https://github.com/ZhengLinLei/windows-python-printer)


## Installation

Install `wkhtmltopdf` in [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html).

**Linux user**
```terminal
sudo apt-get install wkhtmltopdf
# or
sudo apt install wkhtmltopdf
```

Import the source code to your project, and read the examples.
```python

aa = PrintFile()

aa.addFile('./test/test.pdf', 'Test', options = {
     'page-height': '210mm',
     'page-width': '80mm',
})

aa = PrintHTML('./tmp', options = {
    'page-height': '210mm',
    'page-width': '72mm',
    'margin-right': '1mm',
    'margin-left': '1mm',
   'encoding': "UTF-8",

})

aa.addFile('./test/test.html', 'Test', {})

print(aa.options)

aa.choosePrinter(0)


print(aa.printAll())
```
