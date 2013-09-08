from data import*

class Vocabolario:

    def __init__(self):
        self.V = initVocabulary()
        self.count = len(self.V)
        
    def addWord(self, w):
        r = self.findWord("DEL")
        if r == -1:
            self.V.append(w)
        else:
            self.V[r] = w
            

    def findWord(self, w):
        for i in range(self.count):
            if self.V[i] == w:
                return i
        return -1

    def delWord(self, w):
        r = self.findWord(w)
        if r != -1:
            self.V[r]= "DEL"
        else:
            print "Parola non presente nel dizionario!"

    def printVoc(self):
        print "Vocabolario"
        for i in range(self.count):
            print str(self.V[i])

    def __len__(self):
        return len(self.V) 

    def __setitem__(self, w):  
        self.addWord(w)

    def __getitem__(self, w):         # supports v = T[k]
        return self.V[w]