from tkinter import Frame, Tk, BOTH, Text, Menu, END
#import tkFileDialog 
import tkinter.filedialog

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        #dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        #f = open(filename, 'r', encoding='utf-8') 
        text = f.read()
        return text


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()


# # modules for 
# import PyPDF2
# # pdf file object
# # you can find find the pdf file with complete code in below
# pdfFileObj = open('symfony.pdf', 'rb')
# # pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # number of pages in pdf
# print(pdfReader.numPages)
# # a page object
# pageObj = pdfReader.getPage(0)
# # extracting text from page.
# # this will print the text you can also save that into String
# print(pageObj.extractText())