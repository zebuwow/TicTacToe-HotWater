print("would you like to play Tic Tac Toe? y or n?")
LI = [" " , " " , " ", " " , " " , " " , " ", " " , " "]
QI = [2 , 9 , 4 , 7 , 5 , 3 , 6 , 1 , 8]
XI = [ ]
OI = [ ]
def prboard():
    print("("+LI[0]+") ("+LI[1]+") ("+LI[2]+")")
    print("("+LI[3]+") ("+LI[4]+") ("+LI[5]+")")
    print("("+LI[6]+") ("+LI[7]+") ("+LI[8]+")")


ans = input()
if ans[0] != "y":
      exit("okay bye")
game2 = True
while game2 == True:
    game = True
    while game == True:
        prboard()
        
 
        index = 10
        ILF = 0
        iILF = 0
        for GF in range(2):
            BLF = "x"
            if ILF == 1:
                BLF = "o"
            ILF = 1
            
            for LF in range(3):
                check =[]
                for IF in range(3):
                    
                    if LI[IF + LF * 3] == BLF:
                        check.append(1)
                    if sum(check) == 2:
                        for XF in range(3):
                            if LI[XF+ LF* 3] == " " and index == 10:
                                  index = XF + LF * 3
                                  LI[XF + LF * 3] = "x"
                                  XI.append(QI[XF + LF * 3])
        if index == 10:
            for iGF in range(2):
                iBLF = "x"
                if iILF == 1:
                    iBLF = "o"
                iILF = 1
            
                for iLF in range(3):
                    check =[]
                    for iIF in range(3):
                        
                        if LI[iIF * 3 + iLF] == iBLF:
                            check.append(1)
                        if sum(check) == 2:
                            for iXF in range(3):
                                if LI[iXF*3 + iLF] == " " and index == 10:
                                      index = iXF * 3 + iLF 
                                      LI[iXF * 3 + iLF] = "x"
                                      XI.append(QI[iXF * 3  + iLF])
                                        

        if index == 10:
            if LI[0] == " ":
                LI[0] = "x"
                index = 0
                XI.append(QI[0])
            elif LI[6] == "x" and LI[8] == "x" and LI[7] == " ":
                LI[7] = "x"
                index = 7
                XI.append(QI[7])
            elif LI[6] =="x" and LI[0] == "x" and LI[3] == " ":
                LI[3] = "x"
                index = 3
                XI.append(QI[3])
            elif LI[6] == " " and LI[8] == " ":
                LI[8] = "x"
                index = 8
                XI.append(QI[8])
            elif LI[0] == "x" and LI[8] == "x" and LI[4] == " ":
                LI[4] = "x"
                index = 4
                XI.append(QI[4])
            elif LI[8] == "x" and LI[7] == " " and LI[6] == " " and LI[3] == " ":
                LI[6] = "x"
                index = 6
                XI.append(QI[6])
            elif LI[6] == " ":
                LI[6] = "x"
                index = 6
                XI.append(QI[6])
            elif LI[2] == " ":
                LI[2] = "x"
                index = 2
                XI.append(QI[2])
            elif LI[4] == " ":
                LI[4] = "x"
                index = 4
                XI.append(QI[4])
            else:
                for i in range(9):
                    if LI[i] == " ":
                        LI[i] = "x"
                        index = i
                        XI.append(QI[i])
                        break
            
        
            
            
        print("which horizontal row would you like to place on")
        print(index // 3 + 1)
        print("which vertical column would you like to place on")
        print(index % 3 + 1)
        
        
        
        
        if len(XI) == 3:
            if sum(XI) == 15:
                print("X won")
                prboard()
                game = False
                break
                
        if len(XI) == 4:
            for i in range(4):
                newlist = XI.copy()
                newlist.pop(i)
                if sum(newlist) == 15:
                    print("X won")
                    prboard()
                    game = False
                    break
                    
                
        if len(XI) == 5:
            for P in range(5):
                for T in range(5):
                    if P > T:
                        newlist = XI.copy()
                        newlist.pop(P)
                        newlist.pop(T)
                        if sum(newlist) == 15:
                            print("X won")
                            prboard()
                            game = False
                            break
            if game == True:
                print("game is draw")
                prboard()
                game = False
                break
        if game == True:
            prboard()
            print("which horizontal row would you like to place on")
            horz = int(input())
            print("which vertical column would you like to place on")
            vert = int(input())
            index = (horz - 1) * 3 + (vert - 1)
            if LI[index] == " ":
                LI[index] = "o"
            else:
                exit("okay bye")
            OI.append(QI[index])
            if len(OI) == 3:
                if sum(OI) == 15:
                    print("O won")
                    prboard()
                    game = False
                    break
            if len(OI) == 4:
                for i in range(4):
                    newlist = OI.copy()
                    newlist.pop(i)
                    if sum(newlist) == 15:
                        print("O won")
                        prboard()
                        game = False
                        break
                    
        
    LI = [" " , " " , " ", " " , " " , " " , " ", " " , " "]
    QI = [2 , 9 , 4 , 7 , 5 , 3 , 6 , 1 , 8]
    XI = []
    OI = []
    print("would you like to play Tic Tac Toe again? y or n?")
    ans = input()
    if ans[0] != "y":
        exit("okay bye")







