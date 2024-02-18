print("Welcome to TREASURE ISLAND\nYour mission is to find the treasure")


choice1=input('''
            You are at a port asking for a ship to take
            you to an island shown in the map 
            your family had as an heirloom for generations.
            All the sailors laughed at your efforts ,dismissing it as a fool's errand. Only 2 captains agreed to take you there,
            the 'Red Grouper' promised to take you for 120 gold coins and the 'Moby Dick' for 150 gold coins.
            Who will you choose??(give the whole name of the ships)               
               ''').lower()
if (choice1=="red grouper"):
    print(" it was a scam, they took all your possesions and threw you into the sea")
    stage="GAME OVER"
else:
    print(" the captain kept his promise and after many perilous days on rough seas ,you have reached on the island shore")
    choice2= input('''
            the captain asks whether he should stay for your return or not,what is your choice??
            ( if he waits you would have to give him a signicant portion of the treasure,y or n)
                   ''').lower()
    if (choice2=="y"):
        wait=True
    else:
        wait=False
        
        
    choice3=input('''
            You look and see two paths in front of you .Confused ,you refer the map. It shows the 2 paths ,
            both towards the location of the treasure.One is shorter than the other ,
            which one will you choose(r or l)
                  ''').lower()
    if (choice3=="r"):
        print("this was the shortest and easiest path to the treasure,congratulations you have found the treasure")
     
        print("you return back to the beach")
        if (wait==True):
            print("the captain is still there and you give him a significant portion of the treasure")
            print("you safely return to your home with the rest of the treasure and retire in luxury")
        else:
            print("the captain is not there and you are stranded on the island forever.")
            stage="GAME OVER"
    else:
        print('''you took the longer and more deadlier path. While trying to dodge some venomous wasps chasing you,
              you fell into a pit and died''')
        stage="GAME OVER"

if (stage=="GAME OVER"):
    print("GAME OVER")
else:
    print("CONGRATULATIONS YOU HAVE WON THE GAME")