#Created on 08/nov/2012

from editDistance import editDistance
from vocabolario import Vocabolario

def checkError(x, v):
    if x:
        l = len(v)
        found = False
        i = 0
        while (found == False and i < l):
            if v[i] == x:
                found = True
            else:
                i = i +1
        if found == True:
            print 'Parola corretta!'
        else:
            best = 100
            for j in range(len(v)):
                distance = editDistance(x, v[j])
                if(distance < best):
                    best = distance
                    word = j
            print "Forse cercavi '"+ v[word] + "'" 

def testInput():
        x = raw_input("Inserisci una parola: ")
        print "Parola inserita '" + x +"'"
        checkError(x, V)




'''Test'''
global V
V = Vocabolario()
testInput()
