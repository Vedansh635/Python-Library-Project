class Library:
    def __init__(self):
        print('->For adding books in Library use method \'appendb\' \n->For see library use method \'getlib\' \n->For see number of books use method \'numberofbooks\' ')
        self.books = []
        self.number_of_books = len(self.books)
    def appendb(self,*args):
         for arg in args:
             self.books.append(arg)
         self.number_of_books += len(args)

         print(*args , sep=' , ', end=' ')
         if len(args) == 1:  
           print('book is Successfully Appended!')
         elif len(args) > 1:
             print('books are Successfully Appended!')
             

    def getlib(self):
        print('Your libray: ' , self.books)
    
    def numberofbooks(self):
        print(f'Your library contains {self.number_of_books} books')
     
libreader = Library()

# Test Cases
libreader.appendb('C++','The chocolate factory','The jungle book')
libreader.getlib()
libreader.numberofbooks()
libreader.appendb('C','Python')
libreader.numberofbooks()
libreader.getlib()
