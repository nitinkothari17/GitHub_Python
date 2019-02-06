#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class getPrintString(object):
    
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = raw_input()
    
    def outString(self):
        print self.s
        
strobj = getPrintString()
strobj.getString()
strobj.outString()
