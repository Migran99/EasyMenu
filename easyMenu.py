## Menu handler
#Miguel Granero Ramos - 2020
import pdb
import os

def exitProgram():
    os._exit(1)

def f1(p1):
    print("Example 1: ",p1)

def f2(p1,p2):
    print("Example 2: ",p1,p2)
Ex_functions = [f1,f2]

Ex_options = {  0:{ 'name':'Option 0 Name','function':None},
                1:{ 'name':'Option 1 Name','function':None},
                99:{ 'name':'Exit','function': exitProgram}
            }

class Menu:    
    def __init__(self,options=Ex_options):
        self.options = options
        print(self.options)
        
    def printOptions(self):
        print('------------Actions Menu----------')
        for i in self.options:
           print("[{}]: {}".format(str(i),self.options[i]['name']))

    def addOptions(self,options):
        for option in options:
            if(option not in self.options):
                self.options[option] = options[option]
            else:
                print('Option number {} already exists. Do you wish to overwrite it? [Y]'.format(option))
                if(input().capitalize() == 'Y'):
                    self.options[option] = options[option]

    def setFunction(self,id,function):
        if(id in self.options):
            self.options[id]['function'] = function
            print('Function updated')

    def selecOption(self):
        sel = None

        while(sel == None):
            user_input = input('Select option and add parameters: ').split(' ')
            sel = int(user_input[0])
            parameters = user_input[1:]
            if(sel in self.options):
                if (self.options[sel]['function'] != None):
                    try:
                        self.options[sel]['function'](*parameters)
                    except TypeError:
                        print('Error while executing function. Maybe not enough arguments?')
                else:
                    print('This option does not have an associated function')
            else:
                sel = None
                print('Not valid')

if (__name__ == "__main__"):
    print('Example functionality of the Easy Menu Handler')
    mymenu = Menu()
    mymenu.printOptions()
    mymenu.selecOption()
    print('\nWe see that there is no assigned function to 0 or 1')
    print('\nNow we are going to edit option number 0 and assign to it the function f1 with Menu.addOptions(option)')
    mymenu.printOptions()
    mymenu.addOptions({0:{'name':'test change option','function':f1}})
    print('\nOption 0 now has an assigned function. Now lets add a new option with 2 parameters p1 and p2')
    mymenu.printOptions()
    mymenu.addOptions({2:{'name':'test add option','function':f2}})
    print('\nDone, now we have a new menu!!!!')
    while(1):
        mymenu.printOptions()
        mymenu.selecOption()