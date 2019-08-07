# from tkinter import Frame, Tk, BOTH, Text, Menu, END
#import tkFileDialog 
import tkinter.filedialog

import PyPDF2
from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        #self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '*.pdf'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            
            

    def readFile(self, filename):
        pdf_reader = PyPDF2.PdfFileReader(filename)
        for i in range(pdf_reader.numPages):
            page = pdf_reader.getPage(i)
            print(page.extractText())
            Label(text=page.extractText()).pack()

def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()





# import PyPDF2
# from tkinter import *
# root = Tk()

# my_file = open('symfony.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(my_file)
# # print (pdf_reader.numPages)
# # page_one = pdf_reader.getPage(0)
# # print(page_one.extractText())

# for i in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(i)
#     #print (page.extractText())

#     Label(root, text=page.extractText()).pack()

# root.mainloop()



# import PyPDF2
# from tkinter import *
# root = Tk()

# FILE_PATH = './path/symfony.pdf'
# with open(FILE_PATH, mode='rb') as f:
#     reader = PyPDF2.PdfFileReader(f)
#     page = reader.getPage(1)
#     # sprint(page.extractText())
#     Label(root, text=page.extractText()).pack()

# root.mainloop()













# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# root = Tk()
# def openfile():
#     return filedialog.askopenfilename()
# button = ttk.Button(root, text="Open", command=openfile)  # <------
# button.grid(column=1, row=1)

# root.mainloop()

# from tkinter import *

# root = Tk()

# with open("file.txt", "r") as f:
#     Label(root, text=f.read()).pack()

# root.mainloop()