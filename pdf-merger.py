from pypdf import PdfWriter

#assign variable to PdfWriter() call
merger = PdfWriter()

# generate list of files you want to merge as string
lista = []
while True:
    a = input('Enter file name:  ')
    if a == ('n'):
        break
    else:
        lista.append(str(a))
        print(a + 'added')
print('Merging Files...')

#name of files you want to merge
for pdf in lista:
    merger.append(pdf)

#name of new merged pdf file
merger.write("merged-PDFile.pdf")

merger.close()
print('Merge Complete')