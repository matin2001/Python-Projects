from math import ceil


class Pagination:
    def __init__(self, items, page_size):
        self.__itmes = items
        if (type(page_size) == float):
            page_size = ceil(page_size)
        self.__page_size = page_size
        self.page = 0
        a = len(self.__itmes)/self.__page_size
        a = ceil(a)
        self.total_pages = a

    def getVisibleItems(self):
        if (self.page == self.total_pages - 1):
            b = len(self.__itmes) % self.__page_size
            a = 0
            c = ((self.total_pages-1)*self.__page_size)
            while(a<b):
                print(self.__itmes[c+a], end=" ")
                a = a + 1
            print("")
        else:
            a = self.page * self.__page_size
            b = (self.page+1) * self.__page_size
            while(a<b):
                print(self.__itmes[a], end=" ")
                a = a + 1
            print("")

    def prevPage(self):
        if (self.page > 1):
            self.page = self.page - 1

    def nextPage(self):
        self.page = self.page + 1

    def firstPage(self):
        self.page = 0

    def lastPage(self):
        self.page = self.total_pages - 1

    def goToPage(self, page):
        if (type(page) == float):
            page = ceil(page)

        if(page < 1):
            self.page = 0
        elif(page > self.total_pages):
            self.page = self.total_pages - 1
        else:
            self.page = page - 1

    def __str__(self):
        content = ""
        if (self.page == self.total_pages - 1):
            b = len(self.__itmes) % self.__page_size
            a = 0
            c = ((self.total_pages-1)*self.__page_size)
            while(a<b):
                content = content + self.__itmes[c+a] + " "
                a = a + 1
        else:
            a = self.page * self.__page_size
            b = (self.page+1) * self.__page_size
            while(a<b):
                content = content + self.__itmes[a] + " "
                a = a + 1
        return "we are on page " +  str(self.page+1) + " and the total pages is " + str(self.total_pages) +\
            ".\ncontent of current page: " + content

    def __repr__(self):
        return "Pagination object with " + str(self.total_pages) +  " pages and now on page " + str(self.page+1) + "."



if __name__ == '__main__':
    content = input().split()
    page_size = int(input())
    pagination = Pagination(content, page_size)
    n = int(input())
    for i in range(n):
       eval(input())
