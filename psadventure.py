import os
import sys

room_num = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]
room_name = [[None,None,'Backyard','Shed',None],
             ['Gym','Hallway Stairs','Living Room','Kitchen','Laundry Room'],
             [None,None,'Mudroom','Dining Room','Seating Area'],
             [None,None,None,'Bedroom Stairs','Basement Stairs']
             ]
room_map = []
rows = 4
cols = 5

menuBar = {'H':'Help', 'I':'Inventory','M':'Menu','Q':'Quit'}
actions = {'Z':'Sleep', 'P':'Play', 'A':'Eat', 'T':'Take', 'U':'Use', 'R':'Purr', 'X':'Scratch', 'L':'Loaf'}

tab = '        '
spaces = len(tab)

def createFloorMap(index, room):
   floor_map = []
   room_names = []
   cols = len(index[1])
   rows = len(index)
   

   for i in range(0,rows):
       for x in range(0,cols):
           floor_map.append(index[i][x])
    
   for i in range(0,rows):
        for x in range(0,cols):
            room_names.append(room[i][x])

   ff_map_dict = {num: room for num, room in zip (floor_map, room_names)}
   
   return ff_map_dict


def generateRoom(room,message=''):

    os.system('cls')    

  

    def createNav():
        print('Navigation\n----------')
        pathDisplay, pathDict = availpathDisplay(room,room_map)
        prtToScreen(pathDisplay, 'list')
        return pathDisplay, pathDict
        
    def prtToScreen(dictionary, style):
        keys = list(dictionary.keys())
        values = list(dictionary.values())
        
        if style == 'list':
            for i in range(0,len(keys)):
                print(keys[i]+": "+values[i])
        elif style == 'horizontal':
            menu = ''
            for i in range(0,len(keys)):
                menu += (keys[i]+": "+values[i]+'  |  ')
            print(menu)
        elif style == 'columns':
            row = 1
            menu = ''
            for i in range(0,len(keys)):           
                if (i+1) % 3 == 0:
                    menu += (keys[i]+": "+values[i])
                    menu += '\n'
                    row += 1
                elif row > 1:
                    topRow = len((keys[i-(3*(row-1))]+": "+values[i-(3*(row-1))]))
                    menu += (keys[i]+": "+values[i])
                    currentWord = len((keys[i]+": "+values[i]))
                    spaceToAdd = (topRow + 8) - currentWord                       
                    menu += ' '*spaceToAdd
                else:    
                    menu += (keys[i]+": "+values[i]+tab)
            print(menu)

    def prtMenuBar():
        prtToScreen(menuBar,'horizontal')     

    def roomDesc():
        print('Area: '+room_map[room])
        print('\tPlaceholder Room Description\n')
                 
    
    def prtActions():
        print()
        prtToScreen(actions,'columns')

# Begin to print the display elements:

    prtMenuBar()
    print('\n')
    
    print(roomDesc())
    print()
    pathDisplay, pathDict = createNav()
    prtActions()
    print(message)
    
    allActions = {**menuBar,**actions,**pathDict}

    return allActions, pathDict

def availpathDisplay(currentRoom,roommap):
        north = currentRoom - 5
        east = currentRoom + 1
        south = currentRoom + 5
        west = currentRoom - 1

        gonorth = True
        goeast = True
        gosouth = True
        gowest = True

        pathDisplay = {}
        pathDict = {}

        if (currentRoom < 5) or (roommap[north] == None):
            gonorth = False
            

        if east % 5 == 0 or (roommap[east] == None):
            goeast = False
            

        if currentRoom > 14 or (roommap[south] == None):
            gosouth = False
            

        if currentRoom % 5 == 0 or (roommap[west] == None):
            gowest = False
            
        
        if (gonorth != False):
            gonorth = (roommap[north])
            pathDisplay.update({'(N)orth':gonorth})
            pathDict.update({'N':gonorth})
        
        if (goeast != False):
            goeast = (roommap[east])
            pathDisplay.update({'(E)ast':goeast})
            pathDict.update({'E':goeast})

        if (gosouth != False):
            gosouth = (roommap[south])
            pathDisplay.update({'(S)outh':gosouth})
            pathDict.update({'S':gosouth})
        
        if (gowest != False):
            gowest = (roommap[west])
            pathDisplay.update({'(W)est':gowest})
            pathDict.update({'W':gowest})

        return pathDisplay, pathDict


## End Paint Screen

def moveRm(choice,room):
    if choice == 'N':
        newRoom = room - 5
    elif choice == 'E':
        newRoom = room + 1
    elif choice == 'S':
        newRoom = room + 5
    elif choice == 'W':
        newRoom = room - 1
    return newRoom
    


def quitMenu():
    os.system('cls')
    confirmQuit = ''
    
    while confirmQuit.upper() != 'Y' and confirmQuit.upper() != 'N':
        
        confirmQuit = input('Do you really want to quit? (Y/N):')        

        if confirmQuit.upper() == 'Y':            
            print('Goodbye.')
            sys.exit()
        elif confirmQuit.upper() == 'N':
            x = ''                   
        else:
            string = f'"{confirmQuit}"'+' is not an option. Try again.'
            print(string)

def actionCmds(choice):
    os.system('cls')
    if choice == 'Z':
        print('Sleeping Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'P':
        print('Playing Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'A':
        print('Eating Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'T':
        print('Take Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'U':
        print('Use Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'R':
        print('Purr Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'X':
        print('Scratch Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'L':
        print('Loaf Function\n\n\nZzzzzzzzz\n\n\n')
        input('Press ENTER to return to the game.')

actions = {'Z':'Sleep', 'P':'Play', 'A':'Eat', 'T':'Take', 'U':'Use', 'R':'Purr', 'X':'Scratch', 'L':'Loaf'}

def menuCmds(choice):
    os.system('cls')
    if choice == 'H':
        print('Help Screen\n\n\nHelp Screen Text\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'I':
        print('Inventory Screen\n\n\nInventory Displayed Here.\n\n\n')
        input('Press ENTER to return to the game.')
    if choice == 'M':
        print('Menu Screen\n\n\n-Save\n-Load\n-Restart\n-Quit\n\n\n')
        input('Press ENTER to return to the game.')
        

room = 13

room_map = createFloorMap(room_num, room_name)
run = True
msg = ''

while run == True:
    options, pathDisplay = generateRoom(room,msg)
    msg=''
    usrInput = input('Enter an command: ')
    usrInput = usrInput.upper()
    

    if usrInput == 'Q':
        quitMenu()
    elif usrInput in options:
        if usrInput in menuBar:
            menuCmds(usrInput)
        elif usrInput in actions:
            actionCmds(usrInput)            
        else:
            currentRoom = room
            room = moveRm(usrInput, currentRoom)
            #if not in menuBar or actions, this would be navigation options. need to have this as variable
        
    else:        
        msg = f'"{usrInput}"'+' is not an option. Try again.'
       
        




