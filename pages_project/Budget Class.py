# title  : Budget Class 
# author : Tobe
# date   : 14/4/2021

class Category(): # Category class that holds all actions available to the category
    def __init__(self, t , amount ):
        self.t = t
        self.amount = amount
        print(self)

    def printBalance(self):
        print('Category %s Balance: %g' %(self.t, self.amount))

    def depositAmount(self,amt):
        self.amount = self.amount + amt
        self.printBalance()
    def withdrawAmount(self, amt):
        self.amount = self.amount - amt
        self.printBalance()

    def transferAmount( self,target , amt):
        try:
            target.amount = target.amount + amt
            self.amount = self.amount - amt
            self.printBalance()
            target.printBalance()
        except:
            print('Category %s does not exist.' %target)

class Budget(Category): # Budget class inherits Category methods to be able to manipulate categories
    
    def __init__(self, names = [], amounts = []):
        self.names = names
        self.amounts = amounts
        self.categories = []

    def createCategories(self ):
        for i in self.names:
            posIndx = self.names.index(i)
            i = Category(i , self.amounts[posIndx])
            self.categories.append(i)


    def transfer(self,name, target, amt):
        if name in self.names:
            self.categories[self.names.index(name)].transferAmount(self.categories[self.names.index(target)],amt)
        else:
            print('Category does not exist')
    
    def withdraw(self,name,  amt):
        if name in self.names:
            self.categories[self.names.index(name)].withdrawAmount(amt)
        else:
            print('Category does not exist, (Remember to run createCategories).')
        
    def deposit(self,name,amt):
        if name in self.names:
            self.categories[self.names.index(name)].depositAmount(amt)
        else:
            print('Category does not exist')
    def printBudget(self):
        for i in self.categories:
            print('---------------------------------')
            i.printBalance()
        print('Total Balance : %g' %sum(self.amounts) ) 
        
        
