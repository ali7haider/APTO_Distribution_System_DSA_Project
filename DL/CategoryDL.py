import csv
class category:
    def __init__(self,category):
        self.category = category
    def category(self):
        return self.category()

class categoryDL:
    allCategories = []
    
    @staticmethod
    def addCategoryIntoList(c):
        flag = True
        for i in categoryDL.allCategories:
            if(i.category == c.category):
                flag  = False
        if(flag == True):
            categoryDL.allCategories.append(c)
    @staticmethod
    def deleteCategory(c):
        for i in categoryDL.allCategories:
            if(i.category == c.category):
                categoryDL.allCategories.remove(i)
    def readCategoryFromFile(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:      
              if row:                      
                o = str(row[0])
                c = category(o)
                categoryDL.allCategories.append(c)
        file.close()
    def storeCategoryIntoFile(path,c):
        with open(path,"a", newline='') as file:
            file.write(c.category+"\n")
            file.close()
    def storeAllCategoryIntoFile(path):
        with open(path,"w", newline='') as file:
            for i in categoryDL.allCategories:
                file.write(i.category+"\n")
            file.close()