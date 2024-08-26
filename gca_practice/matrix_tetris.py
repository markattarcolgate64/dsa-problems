def drop_tetris(field, figure):
    #What we need to do is loop through the horizontal and then vertical and then horizontal again to check the length 
    #Horizontal loops
    for leftCol in range(len(field[0]) - len(figure[0]) + 1):
        #Now we need to go down the column to figure out 
        fake_field = field[:] 
        #Apply the drop to the fake field and then we'll go across the rows 
        #Loop from the bottom up to the top comparing the rows
        figureRowCount = len(figure) - 1
        moveUp = False
        for row in range(len(field) -1, 0, -1):
            #Apply the drop to the bottom 
            currRow = fake_field[row]
            figureRow = figure[figureRowCount]
            allOne = True
            for col in range(len(currRow)):
                fieldNum = currRow[col]

                if col < len(figureRow):
                    figureNum = figureRow[col]
                    if figureNum == 1 and fieldNum == 1:
                        moveUp = True
                        allOne = False
                        break
                    elif figureNum == 1 and fieldNum == 0:
                        currRow[col] = 1
                if fieldNum == 0:
                    allOne = False
                    moveUp = True
                    break
                
            if allOne:
                return leftCol
            
            if moveUp:
                figureRowCount -= 1 
            

            #if moveUp == True:
        print(figure)
        print(fake_field)



def main():
    figure = [[0, 0, 1],
         [0, 1, 1],
         [0, 0, 1]]

    field = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0]]
    print(field)
 
    drop_tetris(field, figure)
    
    
    
if __name__ == "__main__": 
    main()

