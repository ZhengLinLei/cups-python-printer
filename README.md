# CUPS Python Printer Software

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
