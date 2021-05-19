class Book:
    def details(self,libraryname,bookname,author,pages):
        self.libraryname=libraryname
        self.bookname=bookname
        self.author=author
        self.pages=pages

        print(self.libraryname,self.bookname,self.author,self.pages)
    def __str__(self):
        return self.libraryname + self.bookname + self.author + str(self.pages)


bk=Book()
bk.details("shantabookstall","programming skills","abcd",100)
print(bk)