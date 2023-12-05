long = 4
high = 3
# ChessCar = [[0 for i in range(long)] for j in range(high)]
ChessCar=[1,0,0,0,1,0,1,0,1,1,1,1]
ScoreList=list()
def eva():
    ScoreList.clear()
    for i in range(long*high):
        if ChessCar[i] == 1:
            ChessCar[i]=0
            ScoreList.append(i)
            Chess1=ChessCar
            Chess2=list()
            while len(Chess1)!=len(Chess2):
                for elem in ScoreList:
                    Chess2= CheckAround(elem,ChessCar)

            return  pow(len(ScoreList),2)
def CheckAround(i,ChessCar):
    if i-long>=0 and ChessCar[i-long]==1:
        ChessCar[i-long]=0
        ScoreList.append(i-long)
    if i-1>0 and (i-1)%long!=3 and ChessCar[i-1]==1:
        ChessCar[i-1]=0
        ScoreList.append(i-1)
    if (i+1)%long!=0 and ChessCar[i+1]==1:
        ChessCar[i+1]=0
        ScoreList.append(i+1)
    if i+long<long*high and ChessCar[i+long]==1:
        ChessCar[i+long]=0
        ScoreList.append(i+long)
    return ChessCar
score = 0
tag = 1
while tag:
    SingleScore = eva()
    if type(SingleScore)==type(None):
        tag = 0
    else:
        score +=SingleScore

print(score)
