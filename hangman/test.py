import math
def readPuzzles():
    SuperheroMovies = []
    MusicalInstruments = []
    Sports = []
    puzl = open('puzzles.txt','r')
    for aline in puzl:
        newPuzl = aline.strip().split(',')
        print(newPuzl)
        if newPuzl[-1] == '1':
            SuperheroMovies.append(newPuzl)
            print(SuperheroMovies)
        elif newPuzl[-1] == '2':
            MusicalInstruments.append(newPuzl)
            print(MusicalInstruments)
        elif newPuzl[-1] == '3':
            Sports.append(newPuzl)
            print(Sports)
    puzl.close()
    return [SuperheroMovies,MusicalInstruments,Sports]
puzzles = readPuzzles()
#puzDone = [[],[],[]]
#puzzle = puzzles[1][random.randrange(0,len(puzzles[1]))]
print(puzzles)
