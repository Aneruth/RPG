#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Get to the Garden with the key 
Avoid Monsters

Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dinning Room' 
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'Monster'
                },
                'Dinning Room':{
                   'west': 'Hall'
                },
        'Hall'  :{
               'south' : 'Kitchen',
               'east'  : 'Dinning Room',
               'item'  : 'key'
        },
        
        'Kitchen' : {
              'north' : 'Hall',
              'south' : 'Garden',
              'item'  : 'Monster'
        },
        
        "Dinning Room" :{
                      'west': 'Hall',
                      'south': 'Garden',
                      'item' : 'potion'
        },
        
        'Garden' :{
          'north' : 'Dinning Room'
        }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  #if player enters the monster's room
  if 'item' in rooms[currentRoom] and 'Monster' in rooms[currentRoom]['item']:
    print('HA HA HA HA!!!!! Game Over')
    break
      
  #if player wins when they get to garden
  if currentRoom=='Garden' and 'key' in inventory and 'potion' in inventory:
    print('You Win :-D')
    break