import re
class searchFile(object):
    filename = None
    def __init__(self, filename):
        self.filename = filename

    # prints the first line where the pattern matches
    def searchPattern(self,pattern):
        f = open(self.filename,"r")
        lines = f.readlines()

        for line in lines:
            result = re.search(pattern,line)
            if result:
                print(line)
                break
        f.close()

    # prints all the lines where the pattern matches
    def searchPatternAllLines(self,pattern):
        f = open(self.filename,"r")
        lines = f.readlines()

        for line in lines:
            result = re.search(pattern,line)
            if result:
                print(line)
        f.close()

    def printHostDom(self,st):
        result = re.search(r'([\w]+)@([\w]+)\.([\w]+)',st)
        if result:
            print("Domain = " + result.group(1))
            print("Host = " + result.group(2) + "." + result.group(3))
        else:
            print("No email id found")

    def printWithRoot(self,st):
        result = re.search(r'([\w]+)@([\w]+)\.([\w]+)',st)
        if result:
            print(result.group(1) + "@root")

sF = searchFile("hello.txt")
# sF.searchPatternAllLines("in")
sF.printWithRoot("Contact us at : support@datacamp.com")


