import os
class Filelo(object):

    filename = None

    def __init__(self,filename):
        self.filename = filename

    def ReadFile(self):
        try:
            f = open(self.filename, "r")
            text = f.read()
            print(text)
            f.close()

        except IOError:
            print(self.filename + " not found")



    def CopyToNewFile(self):
        oFileName = self.filename + "_copy.txt"
        # print(oFileName)
        with open(self.filename, "r") as o, open(oFileName,"w") as n:
            for line in o:
                n.write(line)

    def ReplaceWord(self, ofile,text,word):
        f = open(self.filename,"r")
        data = f.read()
        # print(type(data))
        data = data.replace(text,word)
        fnew = open(ofile,"w")
        fnew.write(data)
        f.close()
        fnew.close()


fObj = Filelo("testfile")
# fObj.ReadFile()
# fObj.CopyToNewFile()
fObj.ReplaceWord("hello.txt","file", "filelo")