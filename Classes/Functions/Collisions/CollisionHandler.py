from Classes.Settings import MAP_WIDTH,MAP_HEIGHT

def createBroadPhaseList():
    #CREATE A LIST REPRESENTING A GRID EACH CELL 200X200PX,EACH ENTRY IS A POINT
    gridWidth=200
    gridHeight=200
    broadPhaseList=[]
    x=[]
    y=[]


    #initialisation
    for i in range(0, MAP_WIDTH // gridWidth):
        x=[]
        broadPhaseList.append(x)
        for j in range(0, MAP_HEIGHT // gridHeight):
            y=[]
            broadPhaseList[i].append(y)
    #example of how an list array would work in python
    broadPhaseList[10][10].append((10,10))
    broadPhaseList[i][j].clear()
    broadPhaseList[10][10].append((10, 10))

    broadPhaseList[10][11].append((10, 11))

    broadPhaseList[10][24].append((10, 24))
    # finding a location with an enrtry (should be 2 entries or more for the game)
    print(broadPhaseList)
    for i in range(0, MAP_WIDTH // gridWidth):
        for j in range(0, MAP_HEIGHT // gridHeight):
            if broadPhaseList[i][j].__len__()>0:
                print(broadPhaseList[i][j])


    return broadPhaseList