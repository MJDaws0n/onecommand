#This code has been jumbled to try to prevent less advanced people to try copy it

#Tho if you know what your doing and want to impove it then feel free to 

#welcome to MJDawson's command sender


#This is just random and is responsible for the welcome message

#There is actually a patten with the names - other than opps and oppsagain
cowfinger = "D"
winner = "o"
rat = "c"
cowcoppyright = "s"
fateleven = "!"
oopsagain = "e"
eleven = "o"
finger = "e"
cow = "W"
fat = "l"
oops = "m"
cowwinner = "'"
fingerfinger = "o"
fingerpong = "n"
fingerwinner = " "
cowrat = "w"
cowdrone = "M"
coppyright = " "
fatdrone = "e"
fatfinger = "d"
fingercoppyright = "s"
fingerfat = "m"
fingerdrone = " "
fingercow = "c"
cowabout = "n"
coweleven = "s"
cowfat = "a"
cowcow = "J"
cowpong = "o"
pong = " "
fingereleven = "a"
#Ha fatfat
fatfat = "e"
fatcow = "n"
fatrat = "r"
fatpong = "!"
fingerrat = "m"
fingerabout = "d"
about = "t"


#This is what happens when you type ]go[
def sendCommand():
    print("Your command is:")
    print("")
    
    #This is where the end of the command is added to the rest and added up
    print(command + '''
{id:command_block_minecart,Command:'setblock ~0 ~0 ~ fire[age=15]'},
]}''')



#welcome to MJDawson's command sender
print(f"{cow}{finger}{fat}{rat}{eleven}{oops}{oopsagain}{pong}{about}{winner}{coppyright}{cowdrone}{cowcow}{cowfinger}{cowfat}{cowrat}{coweleven}{cowpong}{cowabout}{cowwinner}{cowcoppyright}{fingerdrone}{fingercow}{fingerfinger}{fingerfat}{fingerrat}{fingereleven}{fingerpong}{fingerabout}{fingerwinner}{fingercoppyright}{fatdrone}{fatcow}{fatfinger}{fatfat}{fatrat}{fateleven}{fatpong}")

#This is the helpful bit
print('''1000 Commands Max!

Type "]go[" to generate your command.

Don't add the "/" before''')


#I know this is really not effient, but I was in a rush for this code

#Command one is differnt to all the rest
com1 = input("Command 1 - ")
if com1 == "]go[":
    #print error
    print("You need at least one command!")
else:
    #add command to list
    command = ('''summon falling_block ~ ~1 ~ {ByMJDawson:1,Time:1,BlockState:{Name:'activator_rail'},Passengers:[
{id:command_block_minecart,Command:''''' + "'" + com1 + ''''},''')

#This one just basically repeats up to 999

com2 = input("Command 2 - ")
if com2 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com2 + ''''},''')

com3 = input("Command 3 - ")
if com3 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com3 + ''''},''')

com4 = input("Command 4 - ")
if com4 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com4 + ''''},''')


com5 = input("Command 5 - ")
if com5 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com5 + ''''},''')


com6 = input("Command 6 - ")
if com6 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com6 + ''''},''')


com7 = input("Command 7 - ")
if com7 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com7 + ''''},''')


com8 = input("Command 8 - ")
if com8 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com8 + ''''},''')


com9 = input("Command 9 - ")
if com9 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com9 + ''''},''')


com10 = input("Command 10 - ")
if com10 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com10 + ''''},''')


com11 = input("Command 11 - ")
if com11 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com11 + ''''},''')


com12 = input("Command 12 - ")
if com12 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com12 + ''''},''')


com13 = input("Command 13 - ")
if com13 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com13 + ''''},''')


com14 = input("Command 14 - ")
if com14 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com14 + ''''},''')


com15 = input("Command 15 - ")
if com15 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com15 + ''''},''')


com16 = input("Command 16 - ")
if com16 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com16 + ''''},''')


com17 = input("Command 17 - ")
if com17 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com17 + ''''},''')


com18 = input("Command 18 - ")
if com18 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com18 + ''''},''')


com19 = input("Command 19 - ")
if com19 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com19 + ''''},''')


com20 = input("Command 20 - ")
if com20 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com20 + ''''},''')


com21 = input("Command 21 - ")
if com21 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com21 + ''''},''')


com22 = input("Command 22 - ")
if com22 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com22 + ''''},''')


com23 = input("Command 23 - ")
if com23 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com23 + ''''},''')


com24 = input("Command 24 - ")
if com24 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com24 + ''''},''')


com25 = input("Command 25 - ")
if com25 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com25 + ''''},''')


com26 = input("Command 26 - ")
if com26 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com26 + ''''},''')


com27 = input("Command 27 - ")
if com27 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com27 + ''''},''')


com28 = input("Command 28 - ")
if com28 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com28 + ''''},''')


com29 = input("Command 29 - ")
if com29 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com29 + ''''},''')


com30 = input("Command 30 - ")
if com30 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com30 + ''''},''')


com31 = input("Command 31 - ")
if com31 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com31 + ''''},''')


com32 = input("Command 32 - ")
if com32 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com32 + ''''},''')


com33 = input("Command 33 - ")
if com33 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com33 + ''''},''')


com34 = input("Command 34 - ")
if com34 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com34 + ''''},''')


com35 = input("Command 35 - ")
if com35 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com35 + ''''},''')


com36 = input("Command 36 - ")
if com36 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com36 + ''''},''')


com37 = input("Command 37 - ")
if com37 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com37 + ''''},''')


com38 = input("Command 38 - ")
if com38 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com38 + ''''},''')


com39 = input("Command 39 - ")
if com39 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com39 + ''''},''')


com40 = input("Command 40 - ")
if com40 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com40 + ''''},''')


com41 = input("Command 41 - ")
if com41 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com41 + ''''},''')


com42 = input("Command 42 - ")
if com42 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com42 + ''''},''')


com43 = input("Command 43 - ")
if com43 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com43 + ''''},''')


com44 = input("Command 44 - ")
if com44 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com44 + ''''},''')


com45 = input("Command 45 - ")
if com45 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com45 + ''''},''')


com46 = input("Command 46 - ")
if com46 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com46 + ''''},''')


com47 = input("Command 47 - ")
if com47 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com47 + ''''},''')


com48 = input("Command 48 - ")
if com48 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com48 + ''''},''')


com49 = input("Command 49 - ")
if com49 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com49 + ''''},''')


com50 = input("Command 50 - ")
if com50 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com50 + ''''},''')


com51 = input("Command 51 - ")
if com51 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com51 + ''''},''')


com52 = input("Command 52 - ")
if com52 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com52 + ''''},''')


com53 = input("Command 53 - ")
if com53 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com53 + ''''},''')


com54 = input("Command 54 - ")
if com54 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com54 + ''''},''')


com55 = input("Command 55 - ")
if com55 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com55 + ''''},''')


com56 = input("Command 56 - ")
if com56 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com56 + ''''},''')


com57 = input("Command 57 - ")
if com57 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com57 + ''''},''')


com58 = input("Command 58 - ")
if com58 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com58 + ''''},''')


com59 = input("Command 59 - ")
if com59 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com59 + ''''},''')


com60 = input("Command 60 - ")
if com60 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com60 + ''''},''')


com61 = input("Command 61 - ")
if com61 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com61 + ''''},''')


com62 = input("Command 62 - ")
if com62 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com62 + ''''},''')


com63 = input("Command 63 - ")
if com63 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com63 + ''''},''')


com64 = input("Command 64 - ")
if com64 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com64 + ''''},''')


com65 = input("Command 65 - ")
if com65 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com65 + ''''},''')


com66 = input("Command 66 - ")
if com66 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com66 + ''''},''')


com67 = input("Command 67 - ")
if com67 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com67 + ''''},''')


com68 = input("Command 68 - ")
if com68 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com68 + ''''},''')


com69 = input("Command 69 - ")
if com69 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com69 + ''''},''')


com70 = input("Command 70 - ")
if com70 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com70 + ''''},''')


com71 = input("Command 71 - ")
if com71 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com71 + ''''},''')


com72 = input("Command 72 - ")
if com72 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com72 + ''''},''')


com73 = input("Command 73 - ")
if com73 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com73 + ''''},''')


com74 = input("Command 74 - ")
if com74 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com74 + ''''},''')


com75 = input("Command 75 - ")
if com75 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com75 + ''''},''')


com76 = input("Command 76 - ")
if com76 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com76 + ''''},''')


com77 = input("Command 77 - ")
if com77 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com77 + ''''},''')


com78 = input("Command 78 - ")
if com78 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com78 + ''''},''')


com79 = input("Command 79 - ")
if com79 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com79 + ''''},''')


com80 = input("Command 80 - ")
if com80 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com80 + ''''},''')


com81 = input("Command 81 - ")
if com81 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com81 + ''''},''')


com82 = input("Command 82 - ")
if com82 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com82 + ''''},''')


com83 = input("Command 83 - ")
if com83 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com83 + ''''},''')


com84 = input("Command 84 - ")
if com84 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com84 + ''''},''')


com85 = input("Command 85 - ")
if com85 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com85 + ''''},''')


com86 = input("Command 86 - ")
if com86 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com86 + ''''},''')


com87 = input("Command 87 - ")
if com87 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com87 + ''''},''')


com88 = input("Command 88 - ")
if com88 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com88 + ''''},''')


com89 = input("Command 89 - ")
if com89 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com89 + ''''},''')


com90 = input("Command 90 - ")
if com90 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com90 + ''''},''')


com91 = input("Command 91 - ")
if com91 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com91 + ''''},''')


com92 = input("Command 92 - ")
if com92 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com92 + ''''},''')


com93 = input("Command 93 - ")
if com93 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com93 + ''''},''')


com94 = input("Command 94 - ")
if com94 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com94 + ''''},''')


com95 = input("Command 95 - ")
if com95 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com95 + ''''},''')


com96 = input("Command 96 - ")
if com96 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com96 + ''''},''')


com97 = input("Command 97 - ")
if com97 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com97 + ''''},''')


com98 = input("Command 98 - ")
if com98 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com98 + ''''},''')


com99 = input("Command 99 - ")
if com99 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com99 + ''''},''')


com100 = input("Command 100 - ")
if com100 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com100 + ''''},''')


com101 = input("Command 101 - ")
if com101 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com101 + ''''},''')


com102 = input("Command 102 - ")
if com102 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com102 + ''''},''')


com103 = input("Command 103 - ")
if com103 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com103 + ''''},''')


com104 = input("Command 104 - ")
if com104 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com104 + ''''},''')


com105 = input("Command 105 - ")
if com105 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com105 + ''''},''')


com106 = input("Command 106 - ")
if com106 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com106 + ''''},''')


com107 = input("Command 107 - ")
if com107 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com107 + ''''},''')


com108 = input("Command 108 - ")
if com108 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com108 + ''''},''')


com109 = input("Command 109 - ")
if com109 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com109 + ''''},''')


com110 = input("Command 110 - ")
if com110 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com110 + ''''},''')


com111 = input("Command 111 - ")
if com111 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com111 + ''''},''')


com112 = input("Command 112 - ")
if com112 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com112 + ''''},''')


com113 = input("Command 113 - ")
if com113 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com113 + ''''},''')


com114 = input("Command 114 - ")
if com114 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com114 + ''''},''')


com115 = input("Command 115 - ")
if com115 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com115 + ''''},''')


com116 = input("Command 116 - ")
if com116 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com116 + ''''},''')


com117 = input("Command 117 - ")
if com117 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com117 + ''''},''')


com118 = input("Command 118 - ")
if com118 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com118 + ''''},''')


com119 = input("Command 119 - ")
if com119 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com119 + ''''},''')


com120 = input("Command 120 - ")
if com120 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com120 + ''''},''')


com121 = input("Command 121 - ")
if com121 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com121 + ''''},''')


com122 = input("Command 122 - ")
if com122 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com122 + ''''},''')


com123 = input("Command 123 - ")
if com123 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com123 + ''''},''')


com124 = input("Command 124 - ")
if com124 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com124 + ''''},''')


com125 = input("Command 125 - ")
if com125 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com125 + ''''},''')


com126 = input("Command 126 - ")
if com126 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com126 + ''''},''')


com127 = input("Command 127 - ")
if com127 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com127 + ''''},''')


com128 = input("Command 128 - ")
if com128 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com128 + ''''},''')


com129 = input("Command 129 - ")
if com129 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com129 + ''''},''')


com130 = input("Command 130 - ")
if com130 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com130 + ''''},''')


com131 = input("Command 131 - ")
if com131 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com131 + ''''},''')


com132 = input("Command 132 - ")
if com132 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com132 + ''''},''')


com133 = input("Command 133 - ")
if com133 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com133 + ''''},''')


com134 = input("Command 134 - ")
if com134 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com134 + ''''},''')


com135 = input("Command 135 - ")
if com135 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com135 + ''''},''')


com136 = input("Command 136 - ")
if com136 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com136 + ''''},''')


com137 = input("Command 137 - ")
if com137 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com137 + ''''},''')


com138 = input("Command 138 - ")
if com138 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com138 + ''''},''')


com139 = input("Command 139 - ")
if com139 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com139 + ''''},''')


com140 = input("Command 140 - ")
if com140 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com140 + ''''},''')


com141 = input("Command 141 - ")
if com141 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com141 + ''''},''')


com142 = input("Command 142 - ")
if com142 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com142 + ''''},''')


com143 = input("Command 143 - ")
if com143 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com143 + ''''},''')


com144 = input("Command 144 - ")
if com144 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com144 + ''''},''')


com145 = input("Command 145 - ")
if com145 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com145 + ''''},''')


com146 = input("Command 146 - ")
if com146 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com146 + ''''},''')


com147 = input("Command 147 - ")
if com147 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com147 + ''''},''')


com148 = input("Command 148 - ")
if com148 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com148 + ''''},''')


com149 = input("Command 149 - ")
if com149 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com149 + ''''},''')


com150 = input("Command 150 - ")
if com150 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com150 + ''''},''')


com151 = input("Command 151 - ")
if com151 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com151 + ''''},''')


com152 = input("Command 152 - ")
if com152 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com152 + ''''},''')


com153 = input("Command 153 - ")
if com153 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com153 + ''''},''')


com154 = input("Command 154 - ")
if com154 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com154 + ''''},''')


com155 = input("Command 155 - ")
if com155 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com155 + ''''},''')


com156 = input("Command 156 - ")
if com156 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com156 + ''''},''')


com157 = input("Command 157 - ")
if com157 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com157 + ''''},''')


com158 = input("Command 158 - ")
if com158 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com158 + ''''},''')


com159 = input("Command 159 - ")
if com159 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com159 + ''''},''')


com160 = input("Command 160 - ")
if com160 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com160 + ''''},''')


com161 = input("Command 161 - ")
if com161 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com161 + ''''},''')


com162 = input("Command 162 - ")
if com162 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com162 + ''''},''')


com163 = input("Command 163 - ")
if com163 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com163 + ''''},''')


com164 = input("Command 164 - ")
if com164 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com164 + ''''},''')


com165 = input("Command 165 - ")
if com165 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com165 + ''''},''')


com166 = input("Command 166 - ")
if com166 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com166 + ''''},''')


com167 = input("Command 167 - ")
if com167 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com167 + ''''},''')


com168 = input("Command 168 - ")
if com168 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com168 + ''''},''')


com169 = input("Command 169 - ")
if com169 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com169 + ''''},''')


com170 = input("Command 170 - ")
if com170 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com170 + ''''},''')


com171 = input("Command 171 - ")
if com171 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com171 + ''''},''')


com172 = input("Command 172 - ")
if com172 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com172 + ''''},''')


com173 = input("Command 173 - ")
if com173 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com173 + ''''},''')


com174 = input("Command 174 - ")
if com174 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com174 + ''''},''')


com175 = input("Command 175 - ")
if com175 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com175 + ''''},''')


com176 = input("Command 176 - ")
if com176 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com176 + ''''},''')


com177 = input("Command 177 - ")
if com177 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com177 + ''''},''')


com178 = input("Command 178 - ")
if com178 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com178 + ''''},''')


com179 = input("Command 179 - ")
if com179 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com179 + ''''},''')


com180 = input("Command 180 - ")
if com180 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com180 + ''''},''')


com181 = input("Command 181 - ")
if com181 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com181 + ''''},''')


com182 = input("Command 182 - ")
if com182 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com182 + ''''},''')


com183 = input("Command 183 - ")
if com183 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com183 + ''''},''')


com184 = input("Command 184 - ")
if com184 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com184 + ''''},''')


com185 = input("Command 185 - ")
if com185 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com185 + ''''},''')


com186 = input("Command 186 - ")
if com186 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com186 + ''''},''')


com187 = input("Command 187 - ")
if com187 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com187 + ''''},''')


com188 = input("Command 188 - ")
if com188 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com188 + ''''},''')


com189 = input("Command 189 - ")
if com189 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com189 + ''''},''')


com190 = input("Command 190 - ")
if com190 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com190 + ''''},''')


com191 = input("Command 191 - ")
if com191 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com191 + ''''},''')


com192 = input("Command 192 - ")
if com192 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com192 + ''''},''')


com193 = input("Command 193 - ")
if com193 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com193 + ''''},''')


com194 = input("Command 194 - ")
if com194 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com194 + ''''},''')


com195 = input("Command 195 - ")
if com195 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com195 + ''''},''')


com196 = input("Command 196 - ")
if com196 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com196 + ''''},''')


com197 = input("Command 197 - ")
if com197 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com197 + ''''},''')


com198 = input("Command 198 - ")
if com198 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com198 + ''''},''')


com199 = input("Command 199 - ")
if com199 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com199 + ''''},''')


com200 = input("Command 200 - ")
if com200 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com200 + ''''},''')


com201 = input("Command 201 - ")
if com201 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com201 + ''''},''')


com202 = input("Command 202 - ")
if com202 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com202 + ''''},''')


com203 = input("Command 203 - ")
if com203 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com203 + ''''},''')


com204 = input("Command 204 - ")
if com204 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com204 + ''''},''')


com205 = input("Command 205 - ")
if com205 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com205 + ''''},''')


com206 = input("Command 206 - ")
if com206 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com206 + ''''},''')


com207 = input("Command 207 - ")
if com207 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com207 + ''''},''')


com208 = input("Command 208 - ")
if com208 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com208 + ''''},''')


com209 = input("Command 209 - ")
if com209 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com209 + ''''},''')


com210 = input("Command 210 - ")
if com210 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com210 + ''''},''')


com211 = input("Command 211 - ")
if com211 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com211 + ''''},''')


com212 = input("Command 212 - ")
if com212 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com212 + ''''},''')


com213 = input("Command 213 - ")
if com213 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com213 + ''''},''')


com214 = input("Command 214 - ")
if com214 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com214 + ''''},''')


com215 = input("Command 215 - ")
if com215 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com215 + ''''},''')


com216 = input("Command 216 - ")
if com216 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com216 + ''''},''')


com217 = input("Command 217 - ")
if com217 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com217 + ''''},''')


com218 = input("Command 218 - ")
if com218 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com218 + ''''},''')


com219 = input("Command 219 - ")
if com219 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com219 + ''''},''')


com220 = input("Command 220 - ")
if com220 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com220 + ''''},''')


com221 = input("Command 221 - ")
if com221 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com221 + ''''},''')


com222 = input("Command 222 - ")
if com222 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com222 + ''''},''')


com223 = input("Command 223 - ")
if com223 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com223 + ''''},''')


com224 = input("Command 224 - ")
if com224 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com224 + ''''},''')


com225 = input("Command 225 - ")
if com225 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com225 + ''''},''')


com226 = input("Command 226 - ")
if com226 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com226 + ''''},''')


com227 = input("Command 227 - ")
if com227 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com227 + ''''},''')


com228 = input("Command 228 - ")
if com228 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com228 + ''''},''')


com229 = input("Command 229 - ")
if com229 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com229 + ''''},''')


com230 = input("Command 230 - ")
if com230 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com230 + ''''},''')


com231 = input("Command 231 - ")
if com231 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com231 + ''''},''')


com232 = input("Command 232 - ")
if com232 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com232 + ''''},''')


com233 = input("Command 233 - ")
if com233 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com233 + ''''},''')


com234 = input("Command 234 - ")
if com234 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com234 + ''''},''')


com235 = input("Command 235 - ")
if com235 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com235 + ''''},''')


com236 = input("Command 236 - ")
if com236 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com236 + ''''},''')


com237 = input("Command 237 - ")
if com237 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com237 + ''''},''')


com238 = input("Command 238 - ")
if com238 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com238 + ''''},''')


com239 = input("Command 239 - ")
if com239 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com239 + ''''},''')


com240 = input("Command 240 - ")
if com240 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com240 + ''''},''')


com241 = input("Command 241 - ")
if com241 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com241 + ''''},''')


com242 = input("Command 242 - ")
if com242 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com242 + ''''},''')


com243 = input("Command 243 - ")
if com243 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com243 + ''''},''')


com244 = input("Command 244 - ")
if com244 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com244 + ''''},''')


com245 = input("Command 245 - ")
if com245 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com245 + ''''},''')


com246 = input("Command 246 - ")
if com246 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com246 + ''''},''')


com247 = input("Command 247 - ")
if com247 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com247 + ''''},''')


com248 = input("Command 248 - ")
if com248 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com248 + ''''},''')


com249 = input("Command 249 - ")
if com249 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com249 + ''''},''')


com250 = input("Command 250 - ")
if com250 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com250 + ''''},''')


com251 = input("Command 251 - ")
if com251 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com251 + ''''},''')


com252 = input("Command 252 - ")
if com252 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com252 + ''''},''')


com253 = input("Command 253 - ")
if com253 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com253 + ''''},''')


com254 = input("Command 254 - ")
if com254 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com254 + ''''},''')


com255 = input("Command 255 - ")
if com255 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com255 + ''''},''')


com256 = input("Command 256 - ")
if com256 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com256 + ''''},''')


com257 = input("Command 257 - ")
if com257 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com257 + ''''},''')


com258 = input("Command 258 - ")
if com258 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com258 + ''''},''')


com259 = input("Command 259 - ")
if com259 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com259 + ''''},''')


com260 = input("Command 260 - ")
if com260 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com260 + ''''},''')


com261 = input("Command 261 - ")
if com261 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com261 + ''''},''')


com262 = input("Command 262 - ")
if com262 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com262 + ''''},''')


com263 = input("Command 263 - ")
if com263 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com263 + ''''},''')


com264 = input("Command 264 - ")
if com264 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com264 + ''''},''')


com265 = input("Command 265 - ")
if com265 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com265 + ''''},''')


com266 = input("Command 266 - ")
if com266 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com266 + ''''},''')


com267 = input("Command 267 - ")
if com267 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com267 + ''''},''')


com268 = input("Command 268 - ")
if com268 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com268 + ''''},''')


com269 = input("Command 269 - ")
if com269 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com269 + ''''},''')


com270 = input("Command 270 - ")
if com270 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com270 + ''''},''')


com271 = input("Command 271 - ")
if com271 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com271 + ''''},''')


com272 = input("Command 272 - ")
if com272 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com272 + ''''},''')


com273 = input("Command 273 - ")
if com273 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com273 + ''''},''')


com274 = input("Command 274 - ")
if com274 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com274 + ''''},''')


com275 = input("Command 275 - ")
if com275 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com275 + ''''},''')


com276 = input("Command 276 - ")
if com276 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com276 + ''''},''')


com277 = input("Command 277 - ")
if com277 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com277 + ''''},''')


com278 = input("Command 278 - ")
if com278 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com278 + ''''},''')


com279 = input("Command 279 - ")
if com279 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com279 + ''''},''')


com280 = input("Command 280 - ")
if com280 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com280 + ''''},''')


com281 = input("Command 281 - ")
if com281 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com281 + ''''},''')


com282 = input("Command 282 - ")
if com282 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com282 + ''''},''')


com283 = input("Command 283 - ")
if com283 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com283 + ''''},''')


com284 = input("Command 284 - ")
if com284 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com284 + ''''},''')


com285 = input("Command 285 - ")
if com285 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com285 + ''''},''')


com286 = input("Command 286 - ")
if com286 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com286 + ''''},''')


com287 = input("Command 287 - ")
if com287 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com287 + ''''},''')


com288 = input("Command 288 - ")
if com288 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com288 + ''''},''')


com289 = input("Command 289 - ")
if com289 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com289 + ''''},''')


com290 = input("Command 290 - ")
if com290 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com290 + ''''},''')


com291 = input("Command 291 - ")
if com291 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com291 + ''''},''')


com292 = input("Command 292 - ")
if com292 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com292 + ''''},''')


com293 = input("Command 293 - ")
if com293 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com293 + ''''},''')


com294 = input("Command 294 - ")
if com294 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com294 + ''''},''')


com295 = input("Command 295 - ")
if com295 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com295 + ''''},''')


com296 = input("Command 296 - ")
if com296 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com296 + ''''},''')


com297 = input("Command 297 - ")
if com297 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com297 + ''''},''')


com298 = input("Command 298 - ")
if com298 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com298 + ''''},''')


com299 = input("Command 299 - ")
if com299 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com299 + ''''},''')


com300 = input("Command 300 - ")
if com300 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com300 + ''''},''')


com301 = input("Command 301 - ")
if com301 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com301 + ''''},''')


com302 = input("Command 302 - ")
if com302 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com302 + ''''},''')


com303 = input("Command 303 - ")
if com303 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com303 + ''''},''')


com304 = input("Command 304 - ")
if com304 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com304 + ''''},''')


com305 = input("Command 305 - ")
if com305 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com305 + ''''},''')


com306 = input("Command 306 - ")
if com306 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com306 + ''''},''')


com307 = input("Command 307 - ")
if com307 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com307 + ''''},''')


com308 = input("Command 308 - ")
if com308 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com308 + ''''},''')


com309 = input("Command 309 - ")
if com309 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com309 + ''''},''')


com310 = input("Command 310 - ")
if com310 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com310 + ''''},''')


com311 = input("Command 311 - ")
if com311 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com311 + ''''},''')


com312 = input("Command 312 - ")
if com312 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com312 + ''''},''')


com313 = input("Command 313 - ")
if com313 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com313 + ''''},''')


com314 = input("Command 314 - ")
if com314 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com314 + ''''},''')


com315 = input("Command 315 - ")
if com315 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com315 + ''''},''')


com316 = input("Command 316 - ")
if com316 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com316 + ''''},''')


com317 = input("Command 317 - ")
if com317 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com317 + ''''},''')


com318 = input("Command 318 - ")
if com318 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com318 + ''''},''')


com319 = input("Command 319 - ")
if com319 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com319 + ''''},''')


com320 = input("Command 320 - ")
if com320 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com320 + ''''},''')


com321 = input("Command 321 - ")
if com321 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com321 + ''''},''')


com322 = input("Command 322 - ")
if com322 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com322 + ''''},''')


com323 = input("Command 323 - ")
if com323 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com323 + ''''},''')


com324 = input("Command 324 - ")
if com324 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com324 + ''''},''')


com325 = input("Command 325 - ")
if com325 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com325 + ''''},''')


com326 = input("Command 326 - ")
if com326 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com326 + ''''},''')


com327 = input("Command 327 - ")
if com327 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com327 + ''''},''')


com328 = input("Command 328 - ")
if com328 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com328 + ''''},''')


com329 = input("Command 329 - ")
if com329 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com329 + ''''},''')


com330 = input("Command 330 - ")
if com330 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com330 + ''''},''')


com331 = input("Command 331 - ")
if com331 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com331 + ''''},''')


com332 = input("Command 332 - ")
if com332 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com332 + ''''},''')


com333 = input("Command 333 - ")
if com333 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com333 + ''''},''')


com334 = input("Command 334 - ")
if com334 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com334 + ''''},''')


com335 = input("Command 335 - ")
if com335 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com335 + ''''},''')


com336 = input("Command 336 - ")
if com336 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com336 + ''''},''')


com337 = input("Command 337 - ")
if com337 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com337 + ''''},''')


com338 = input("Command 338 - ")
if com338 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com338 + ''''},''')


com339 = input("Command 339 - ")
if com339 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com339 + ''''},''')


com340 = input("Command 340 - ")
if com340 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com340 + ''''},''')


com341 = input("Command 341 - ")
if com341 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com341 + ''''},''')


com342 = input("Command 342 - ")
if com342 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com342 + ''''},''')


com343 = input("Command 343 - ")
if com343 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com343 + ''''},''')


com344 = input("Command 344 - ")
if com344 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com344 + ''''},''')


com345 = input("Command 345 - ")
if com345 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com345 + ''''},''')


com346 = input("Command 346 - ")
if com346 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com346 + ''''},''')


com347 = input("Command 347 - ")
if com347 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com347 + ''''},''')


com348 = input("Command 348 - ")
if com348 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com348 + ''''},''')


com349 = input("Command 349 - ")
if com349 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com349 + ''''},''')


com350 = input("Command 350 - ")
if com350 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com350 + ''''},''')


com351 = input("Command 351 - ")
if com351 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com351 + ''''},''')


com352 = input("Command 352 - ")
if com352 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com352 + ''''},''')


com353 = input("Command 353 - ")
if com353 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com353 + ''''},''')


com354 = input("Command 354 - ")
if com354 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com354 + ''''},''')


com355 = input("Command 355 - ")
if com355 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com355 + ''''},''')


com356 = input("Command 356 - ")
if com356 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com356 + ''''},''')


com357 = input("Command 357 - ")
if com357 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com357 + ''''},''')


com358 = input("Command 358 - ")
if com358 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com358 + ''''},''')


com359 = input("Command 359 - ")
if com359 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com359 + ''''},''')


com360 = input("Command 360 - ")
if com360 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com360 + ''''},''')


com361 = input("Command 361 - ")
if com361 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com361 + ''''},''')


com362 = input("Command 362 - ")
if com362 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com362 + ''''},''')


com363 = input("Command 363 - ")
if com363 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com363 + ''''},''')


com364 = input("Command 364 - ")
if com364 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com364 + ''''},''')


com365 = input("Command 365 - ")
if com365 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com365 + ''''},''')


com366 = input("Command 366 - ")
if com366 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com366 + ''''},''')


com367 = input("Command 367 - ")
if com367 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com367 + ''''},''')


com368 = input("Command 368 - ")
if com368 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com368 + ''''},''')


com369 = input("Command 369 - ")
if com369 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com369 + ''''},''')


com370 = input("Command 370 - ")
if com370 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com370 + ''''},''')


com371 = input("Command 371 - ")
if com371 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com371 + ''''},''')


com372 = input("Command 372 - ")
if com372 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com372 + ''''},''')


com373 = input("Command 373 - ")
if com373 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com373 + ''''},''')


com374 = input("Command 374 - ")
if com374 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com374 + ''''},''')


com375 = input("Command 375 - ")
if com375 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com375 + ''''},''')


com376 = input("Command 376 - ")
if com376 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com376 + ''''},''')


com377 = input("Command 377 - ")
if com377 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com377 + ''''},''')


com378 = input("Command 378 - ")
if com378 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com378 + ''''},''')


com379 = input("Command 379 - ")
if com379 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com379 + ''''},''')


com380 = input("Command 380 - ")
if com380 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com380 + ''''},''')


com381 = input("Command 381 - ")
if com381 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com381 + ''''},''')


com382 = input("Command 382 - ")
if com382 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com382 + ''''},''')


com383 = input("Command 383 - ")
if com383 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com383 + ''''},''')


com384 = input("Command 384 - ")
if com384 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com384 + ''''},''')


com385 = input("Command 385 - ")
if com385 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com385 + ''''},''')


com386 = input("Command 386 - ")
if com386 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com386 + ''''},''')


com387 = input("Command 387 - ")
if com387 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com387 + ''''},''')


com388 = input("Command 388 - ")
if com388 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com388 + ''''},''')


com389 = input("Command 389 - ")
if com389 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com389 + ''''},''')


com390 = input("Command 390 - ")
if com390 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com390 + ''''},''')


com391 = input("Command 391 - ")
if com391 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com391 + ''''},''')


com392 = input("Command 392 - ")
if com392 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com392 + ''''},''')


com393 = input("Command 393 - ")
if com393 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com393 + ''''},''')


com394 = input("Command 394 - ")
if com394 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com394 + ''''},''')


com395 = input("Command 395 - ")
if com395 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com395 + ''''},''')


com396 = input("Command 396 - ")
if com396 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com396 + ''''},''')


com397 = input("Command 397 - ")
if com397 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com397 + ''''},''')


com398 = input("Command 398 - ")
if com398 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com398 + ''''},''')


com399 = input("Command 399 - ")
if com399 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com399 + ''''},''')


com400 = input("Command 400 - ")
if com400 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com400 + ''''},''')


com401 = input("Command 401 - ")
if com401 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com401 + ''''},''')


com402 = input("Command 402 - ")
if com402 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com402 + ''''},''')


com403 = input("Command 403 - ")
if com403 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com403 + ''''},''')


com404 = input("Command 404 - ")
if com404 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com404 + ''''},''')


com405 = input("Command 405 - ")
if com405 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com405 + ''''},''')


com406 = input("Command 406 - ")
if com406 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com406 + ''''},''')


com407 = input("Command 407 - ")
if com407 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com407 + ''''},''')


com408 = input("Command 408 - ")
if com408 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com408 + ''''},''')


com409 = input("Command 409 - ")
if com409 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com409 + ''''},''')


com410 = input("Command 410 - ")
if com410 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com410 + ''''},''')


com411 = input("Command 411 - ")
if com411 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com411 + ''''},''')


com412 = input("Command 412 - ")
if com412 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com412 + ''''},''')


com413 = input("Command 413 - ")
if com413 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com413 + ''''},''')


com414 = input("Command 414 - ")
if com414 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com414 + ''''},''')


com415 = input("Command 415 - ")
if com415 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com415 + ''''},''')


com416 = input("Command 416 - ")
if com416 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com416 + ''''},''')


com417 = input("Command 417 - ")
if com417 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com417 + ''''},''')


com418 = input("Command 418 - ")
if com418 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com418 + ''''},''')


com419 = input("Command 419 - ")
if com419 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com419 + ''''},''')


com420 = input("Command 420 - ")
if com420 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com420 + ''''},''')


com421 = input("Command 421 - ")
if com421 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com421 + ''''},''')


com422 = input("Command 422 - ")
if com422 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com422 + ''''},''')


com423 = input("Command 423 - ")
if com423 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com423 + ''''},''')


com424 = input("Command 424 - ")
if com424 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com424 + ''''},''')


com425 = input("Command 425 - ")
if com425 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com425 + ''''},''')


com426 = input("Command 426 - ")
if com426 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com426 + ''''},''')


com427 = input("Command 427 - ")
if com427 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com427 + ''''},''')


com428 = input("Command 428 - ")
if com428 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com428 + ''''},''')


com429 = input("Command 429 - ")
if com429 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com429 + ''''},''')


com430 = input("Command 430 - ")
if com430 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com430 + ''''},''')


com431 = input("Command 431 - ")
if com431 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com431 + ''''},''')


com432 = input("Command 432 - ")
if com432 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com432 + ''''},''')


com433 = input("Command 433 - ")
if com433 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com433 + ''''},''')


com434 = input("Command 434 - ")
if com434 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com434 + ''''},''')


com435 = input("Command 435 - ")
if com435 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com435 + ''''},''')


com436 = input("Command 436 - ")
if com436 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com436 + ''''},''')


com437 = input("Command 437 - ")
if com437 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com437 + ''''},''')


com438 = input("Command 438 - ")
if com438 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com438 + ''''},''')


com439 = input("Command 439 - ")
if com439 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com439 + ''''},''')


com440 = input("Command 440 - ")
if com440 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com440 + ''''},''')


com441 = input("Command 441 - ")
if com441 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com441 + ''''},''')


com442 = input("Command 442 - ")
if com442 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com442 + ''''},''')


com443 = input("Command 443 - ")
if com443 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com443 + ''''},''')


com444 = input("Command 444 - ")
if com444 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com444 + ''''},''')


com445 = input("Command 445 - ")
if com445 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com445 + ''''},''')


com446 = input("Command 446 - ")
if com446 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com446 + ''''},''')


com447 = input("Command 447 - ")
if com447 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com447 + ''''},''')


com448 = input("Command 448 - ")
if com448 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com448 + ''''},''')


com449 = input("Command 449 - ")
if com449 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com449 + ''''},''')


com450 = input("Command 450 - ")
if com450 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com450 + ''''},''')


com451 = input("Command 451 - ")
if com451 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com451 + ''''},''')


com452 = input("Command 452 - ")
if com452 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com452 + ''''},''')


com453 = input("Command 453 - ")
if com453 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com453 + ''''},''')


com454 = input("Command 454 - ")
if com454 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com454 + ''''},''')


com455 = input("Command 455 - ")
if com455 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com455 + ''''},''')


com456 = input("Command 456 - ")
if com456 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com456 + ''''},''')


com457 = input("Command 457 - ")
if com457 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com457 + ''''},''')


com458 = input("Command 458 - ")
if com458 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com458 + ''''},''')


com459 = input("Command 459 - ")
if com459 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com459 + ''''},''')


com460 = input("Command 460 - ")
if com460 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com460 + ''''},''')


com461 = input("Command 461 - ")
if com461 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com461 + ''''},''')


com462 = input("Command 462 - ")
if com462 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com462 + ''''},''')


com463 = input("Command 463 - ")
if com463 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com463 + ''''},''')


com464 = input("Command 464 - ")
if com464 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com464 + ''''},''')


com465 = input("Command 465 - ")
if com465 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com465 + ''''},''')


com466 = input("Command 466 - ")
if com466 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com466 + ''''},''')


com467 = input("Command 467 - ")
if com467 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com467 + ''''},''')


com468 = input("Command 468 - ")
if com468 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com468 + ''''},''')


com469 = input("Command 469 - ")
if com469 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com469 + ''''},''')


com470 = input("Command 470 - ")
if com470 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com470 + ''''},''')


com471 = input("Command 471 - ")
if com471 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com471 + ''''},''')


com472 = input("Command 472 - ")
if com472 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com472 + ''''},''')


com473 = input("Command 473 - ")
if com473 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com473 + ''''},''')


com474 = input("Command 474 - ")
if com474 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com474 + ''''},''')


com475 = input("Command 475 - ")
if com475 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com475 + ''''},''')


com476 = input("Command 476 - ")
if com476 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com476 + ''''},''')


com477 = input("Command 477 - ")
if com477 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com477 + ''''},''')


com478 = input("Command 478 - ")
if com478 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com478 + ''''},''')


com479 = input("Command 479 - ")
if com479 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com479 + ''''},''')


com480 = input("Command 480 - ")
if com480 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com480 + ''''},''')


com481 = input("Command 481 - ")
if com481 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com481 + ''''},''')


com482 = input("Command 482 - ")
if com482 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com482 + ''''},''')


com483 = input("Command 483 - ")
if com483 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com483 + ''''},''')


com484 = input("Command 484 - ")
if com484 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com484 + ''''},''')


com485 = input("Command 485 - ")
if com485 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com485 + ''''},''')


com486 = input("Command 486 - ")
if com486 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com486 + ''''},''')


com487 = input("Command 487 - ")
if com487 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com487 + ''''},''')


com488 = input("Command 488 - ")
if com488 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com488 + ''''},''')


com489 = input("Command 489 - ")
if com489 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com489 + ''''},''')


com490 = input("Command 490 - ")
if com490 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com490 + ''''},''')


com491 = input("Command 491 - ")
if com491 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com491 + ''''},''')


com492 = input("Command 492 - ")
if com492 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com492 + ''''},''')


com493 = input("Command 493 - ")
if com493 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com493 + ''''},''')


com494 = input("Command 494 - ")
if com494 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com494 + ''''},''')


com495 = input("Command 495 - ")
if com495 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com495 + ''''},''')


com496 = input("Command 496 - ")
if com496 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com496 + ''''},''')


com497 = input("Command 497 - ")
if com497 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com497 + ''''},''')


com498 = input("Command 498 - ")
if com498 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com498 + ''''},''')


com499 = input("Command 499 - ")
if com499 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com499 + ''''},''')


com500 = input("Command 500 - ")
if com500 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com500 + ''''},''')


com501 = input("Command 501 - ")
if com501 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com501 + ''''},''')


com502 = input("Command 502 - ")
if com502 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com502 + ''''},''')


com503 = input("Command 503 - ")
if com503 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com503 + ''''},''')


com504 = input("Command 504 - ")
if com504 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com504 + ''''},''')


com505 = input("Command 505 - ")
if com505 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com505 + ''''},''')


com506 = input("Command 506 - ")
if com506 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com506 + ''''},''')


com507 = input("Command 507 - ")
if com507 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com507 + ''''},''')


com508 = input("Command 508 - ")
if com508 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com508 + ''''},''')


com509 = input("Command 509 - ")
if com509 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com509 + ''''},''')


com510 = input("Command 510 - ")
if com510 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com510 + ''''},''')


com511 = input("Command 511 - ")
if com511 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com511 + ''''},''')


com512 = input("Command 512 - ")
if com512 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com512 + ''''},''')


com513 = input("Command 513 - ")
if com513 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com513 + ''''},''')


com514 = input("Command 514 - ")
if com514 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com514 + ''''},''')


com515 = input("Command 515 - ")
if com515 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com515 + ''''},''')


com516 = input("Command 516 - ")
if com516 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com516 + ''''},''')


com517 = input("Command 517 - ")
if com517 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com517 + ''''},''')


com518 = input("Command 518 - ")
if com518 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com518 + ''''},''')


com519 = input("Command 519 - ")
if com519 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com519 + ''''},''')


com520 = input("Command 520 - ")
if com520 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com520 + ''''},''')


com521 = input("Command 521 - ")
if com521 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com521 + ''''},''')


com522 = input("Command 522 - ")
if com522 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com522 + ''''},''')


com523 = input("Command 523 - ")
if com523 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com523 + ''''},''')


com524 = input("Command 524 - ")
if com524 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com524 + ''''},''')


com525 = input("Command 525 - ")
if com525 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com525 + ''''},''')


com526 = input("Command 526 - ")
if com526 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com526 + ''''},''')


com527 = input("Command 527 - ")
if com527 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com527 + ''''},''')


com528 = input("Command 528 - ")
if com528 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com528 + ''''},''')


com529 = input("Command 529 - ")
if com529 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com529 + ''''},''')


com530 = input("Command 530 - ")
if com530 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com530 + ''''},''')


com531 = input("Command 531 - ")
if com531 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com531 + ''''},''')


com532 = input("Command 532 - ")
if com532 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com532 + ''''},''')


com533 = input("Command 533 - ")
if com533 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com533 + ''''},''')


com534 = input("Command 534 - ")
if com534 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com534 + ''''},''')


com535 = input("Command 535 - ")
if com535 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com535 + ''''},''')


com536 = input("Command 536 - ")
if com536 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com536 + ''''},''')


com537 = input("Command 537 - ")
if com537 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com537 + ''''},''')


com538 = input("Command 538 - ")
if com538 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com538 + ''''},''')


com539 = input("Command 539 - ")
if com539 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com539 + ''''},''')


com540 = input("Command 540 - ")
if com540 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com540 + ''''},''')


com541 = input("Command 541 - ")
if com541 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com541 + ''''},''')


com542 = input("Command 542 - ")
if com542 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com542 + ''''},''')


com543 = input("Command 543 - ")
if com543 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com543 + ''''},''')


com544 = input("Command 544 - ")
if com544 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com544 + ''''},''')


com545 = input("Command 545 - ")
if com545 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com545 + ''''},''')


com546 = input("Command 546 - ")
if com546 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com546 + ''''},''')


com547 = input("Command 547 - ")
if com547 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com547 + ''''},''')


com548 = input("Command 548 - ")
if com548 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com548 + ''''},''')


com549 = input("Command 549 - ")
if com549 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com549 + ''''},''')


com550 = input("Command 550 - ")
if com550 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com550 + ''''},''')


com551 = input("Command 551 - ")
if com551 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com551 + ''''},''')


com552 = input("Command 552 - ")
if com552 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com552 + ''''},''')


com553 = input("Command 553 - ")
if com553 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com553 + ''''},''')


com554 = input("Command 554 - ")
if com554 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com554 + ''''},''')


com555 = input("Command 555 - ")
if com555 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com555 + ''''},''')


com556 = input("Command 556 - ")
if com556 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com556 + ''''},''')


com557 = input("Command 557 - ")
if com557 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com557 + ''''},''')


com558 = input("Command 558 - ")
if com558 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com558 + ''''},''')


com559 = input("Command 559 - ")
if com559 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com559 + ''''},''')


com560 = input("Command 560 - ")
if com560 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com560 + ''''},''')


com561 = input("Command 561 - ")
if com561 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com561 + ''''},''')


com562 = input("Command 562 - ")
if com562 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com562 + ''''},''')


com563 = input("Command 563 - ")
if com563 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com563 + ''''},''')


com564 = input("Command 564 - ")
if com564 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com564 + ''''},''')


com565 = input("Command 565 - ")
if com565 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com565 + ''''},''')


com566 = input("Command 566 - ")
if com566 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com566 + ''''},''')


com567 = input("Command 567 - ")
if com567 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com567 + ''''},''')


com568 = input("Command 568 - ")
if com568 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com568 + ''''},''')


com569 = input("Command 569 - ")
if com569 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com569 + ''''},''')


com570 = input("Command 570 - ")
if com570 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com570 + ''''},''')


com571 = input("Command 571 - ")
if com571 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com571 + ''''},''')


com572 = input("Command 572 - ")
if com572 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com572 + ''''},''')


com573 = input("Command 573 - ")
if com573 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com573 + ''''},''')


com574 = input("Command 574 - ")
if com574 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com574 + ''''},''')


com575 = input("Command 575 - ")
if com575 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com575 + ''''},''')


com576 = input("Command 576 - ")
if com576 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com576 + ''''},''')


com577 = input("Command 577 - ")
if com577 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com577 + ''''},''')


com578 = input("Command 578 - ")
if com578 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com578 + ''''},''')


com579 = input("Command 579 - ")
if com579 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com579 + ''''},''')


com580 = input("Command 580 - ")
if com580 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com580 + ''''},''')


com581 = input("Command 581 - ")
if com581 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com581 + ''''},''')


com582 = input("Command 582 - ")
if com582 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com582 + ''''},''')


com583 = input("Command 583 - ")
if com583 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com583 + ''''},''')


com584 = input("Command 584 - ")
if com584 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com584 + ''''},''')


com585 = input("Command 585 - ")
if com585 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com585 + ''''},''')


com586 = input("Command 586 - ")
if com586 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com586 + ''''},''')


com587 = input("Command 587 - ")
if com587 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com587 + ''''},''')


com588 = input("Command 588 - ")
if com588 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com588 + ''''},''')


com589 = input("Command 589 - ")
if com589 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com589 + ''''},''')


com590 = input("Command 590 - ")
if com590 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com590 + ''''},''')


com591 = input("Command 591 - ")
if com591 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com591 + ''''},''')


com592 = input("Command 592 - ")
if com592 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com592 + ''''},''')


com593 = input("Command 593 - ")
if com593 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com593 + ''''},''')


com594 = input("Command 594 - ")
if com594 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com594 + ''''},''')


com595 = input("Command 595 - ")
if com595 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com595 + ''''},''')


com596 = input("Command 596 - ")
if com596 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com596 + ''''},''')


com597 = input("Command 597 - ")
if com597 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com597 + ''''},''')


com598 = input("Command 598 - ")
if com598 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com598 + ''''},''')


com599 = input("Command 599 - ")
if com599 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com599 + ''''},''')


com600 = input("Command 600 - ")
if com600 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com600 + ''''},''')


com601 = input("Command 601 - ")
if com601 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com601 + ''''},''')


com602 = input("Command 602 - ")
if com602 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com602 + ''''},''')


com603 = input("Command 603 - ")
if com603 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com603 + ''''},''')


com604 = input("Command 604 - ")
if com604 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com604 + ''''},''')


com605 = input("Command 605 - ")
if com605 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com605 + ''''},''')


com606 = input("Command 606 - ")
if com606 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com606 + ''''},''')


com607 = input("Command 607 - ")
if com607 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com607 + ''''},''')


com608 = input("Command 608 - ")
if com608 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com608 + ''''},''')


com609 = input("Command 609 - ")
if com609 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com609 + ''''},''')


com610 = input("Command 610 - ")
if com610 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com610 + ''''},''')


com611 = input("Command 611 - ")
if com611 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com611 + ''''},''')


com612 = input("Command 612 - ")
if com612 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com612 + ''''},''')


com613 = input("Command 613 - ")
if com613 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com613 + ''''},''')


com614 = input("Command 614 - ")
if com614 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com614 + ''''},''')


com615 = input("Command 615 - ")
if com615 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com615 + ''''},''')


com616 = input("Command 616 - ")
if com616 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com616 + ''''},''')


com617 = input("Command 617 - ")
if com617 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com617 + ''''},''')


com618 = input("Command 618 - ")
if com618 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com618 + ''''},''')


com619 = input("Command 619 - ")
if com619 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com619 + ''''},''')


com620 = input("Command 620 - ")
if com620 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com620 + ''''},''')


com621 = input("Command 621 - ")
if com621 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com621 + ''''},''')


com622 = input("Command 622 - ")
if com622 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com622 + ''''},''')


com623 = input("Command 623 - ")
if com623 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com623 + ''''},''')


com624 = input("Command 624 - ")
if com624 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com624 + ''''},''')


com625 = input("Command 625 - ")
if com625 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com625 + ''''},''')


com626 = input("Command 626 - ")
if com626 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com626 + ''''},''')


com627 = input("Command 627 - ")
if com627 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com627 + ''''},''')


com628 = input("Command 628 - ")
if com628 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com628 + ''''},''')


com629 = input("Command 629 - ")
if com629 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com629 + ''''},''')


com630 = input("Command 630 - ")
if com630 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com630 + ''''},''')


com631 = input("Command 631 - ")
if com631 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com631 + ''''},''')


com632 = input("Command 632 - ")
if com632 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com632 + ''''},''')


com633 = input("Command 633 - ")
if com633 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com633 + ''''},''')


com634 = input("Command 634 - ")
if com634 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com634 + ''''},''')


com635 = input("Command 635 - ")
if com635 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com635 + ''''},''')


com636 = input("Command 636 - ")
if com636 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com636 + ''''},''')


com637 = input("Command 637 - ")
if com637 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com637 + ''''},''')


com638 = input("Command 638 - ")
if com638 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com638 + ''''},''')


com639 = input("Command 639 - ")
if com639 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com639 + ''''},''')


com640 = input("Command 640 - ")
if com640 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com640 + ''''},''')


com641 = input("Command 641 - ")
if com641 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com641 + ''''},''')


com642 = input("Command 642 - ")
if com642 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com642 + ''''},''')


com643 = input("Command 643 - ")
if com643 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com643 + ''''},''')


com644 = input("Command 644 - ")
if com644 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com644 + ''''},''')


com645 = input("Command 645 - ")
if com645 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com645 + ''''},''')


com646 = input("Command 646 - ")
if com646 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com646 + ''''},''')


com647 = input("Command 647 - ")
if com647 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com647 + ''''},''')


com648 = input("Command 648 - ")
if com648 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com648 + ''''},''')


com649 = input("Command 649 - ")
if com649 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com649 + ''''},''')


com650 = input("Command 650 - ")
if com650 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com650 + ''''},''')


com651 = input("Command 651 - ")
if com651 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com651 + ''''},''')


com652 = input("Command 652 - ")
if com652 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com652 + ''''},''')


com653 = input("Command 653 - ")
if com653 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com653 + ''''},''')


com654 = input("Command 654 - ")
if com654 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com654 + ''''},''')


com655 = input("Command 655 - ")
if com655 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com655 + ''''},''')


com656 = input("Command 656 - ")
if com656 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com656 + ''''},''')


com657 = input("Command 657 - ")
if com657 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com657 + ''''},''')


com658 = input("Command 658 - ")
if com658 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com658 + ''''},''')


com659 = input("Command 659 - ")
if com659 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com659 + ''''},''')


com660 = input("Command 660 - ")
if com660 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com660 + ''''},''')


com661 = input("Command 661 - ")
if com661 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com661 + ''''},''')


com662 = input("Command 662 - ")
if com662 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com662 + ''''},''')


com663 = input("Command 663 - ")
if com663 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com663 + ''''},''')


com664 = input("Command 664 - ")
if com664 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com664 + ''''},''')


com665 = input("Command 665 - ")
if com665 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com665 + ''''},''')


com666 = input("Command 666 - ")
if com666 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com666 + ''''},''')


com667 = input("Command 667 - ")
if com667 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com667 + ''''},''')


com668 = input("Command 668 - ")
if com668 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com668 + ''''},''')


com669 = input("Command 669 - ")
if com669 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com669 + ''''},''')


com670 = input("Command 670 - ")
if com670 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com670 + ''''},''')


com671 = input("Command 671 - ")
if com671 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com671 + ''''},''')


com672 = input("Command 672 - ")
if com672 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com672 + ''''},''')


com673 = input("Command 673 - ")
if com673 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com673 + ''''},''')


com674 = input("Command 674 - ")
if com674 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com674 + ''''},''')


com675 = input("Command 675 - ")
if com675 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com675 + ''''},''')


com676 = input("Command 676 - ")
if com676 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com676 + ''''},''')


com677 = input("Command 677 - ")
if com677 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com677 + ''''},''')


com678 = input("Command 678 - ")
if com678 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com678 + ''''},''')


com679 = input("Command 679 - ")
if com679 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com679 + ''''},''')


com680 = input("Command 680 - ")
if com680 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com680 + ''''},''')


com681 = input("Command 681 - ")
if com681 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com681 + ''''},''')


com682 = input("Command 682 - ")
if com682 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com682 + ''''},''')


com683 = input("Command 683 - ")
if com683 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com683 + ''''},''')


com684 = input("Command 684 - ")
if com684 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com684 + ''''},''')


com685 = input("Command 685 - ")
if com685 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com685 + ''''},''')


com686 = input("Command 686 - ")
if com686 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com686 + ''''},''')


com687 = input("Command 687 - ")
if com687 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com687 + ''''},''')


com688 = input("Command 688 - ")
if com688 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com688 + ''''},''')


com689 = input("Command 689 - ")
if com689 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com689 + ''''},''')


com690 = input("Command 690 - ")
if com690 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com690 + ''''},''')


com691 = input("Command 691 - ")
if com691 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com691 + ''''},''')


com692 = input("Command 692 - ")
if com692 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com692 + ''''},''')


com693 = input("Command 693 - ")
if com693 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com693 + ''''},''')


com694 = input("Command 694 - ")
if com694 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com694 + ''''},''')


com695 = input("Command 695 - ")
if com695 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com695 + ''''},''')


com696 = input("Command 696 - ")
if com696 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com696 + ''''},''')


com697 = input("Command 697 - ")
if com697 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com697 + ''''},''')


com698 = input("Command 698 - ")
if com698 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com698 + ''''},''')


com699 = input("Command 699 - ")
if com699 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com699 + ''''},''')


com700 = input("Command 700 - ")
if com700 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com700 + ''''},''')


com701 = input("Command 701 - ")
if com701 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com701 + ''''},''')


com702 = input("Command 702 - ")
if com702 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com702 + ''''},''')


com703 = input("Command 703 - ")
if com703 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com703 + ''''},''')


com704 = input("Command 704 - ")
if com704 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com704 + ''''},''')


com705 = input("Command 705 - ")
if com705 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com705 + ''''},''')


com706 = input("Command 706 - ")
if com706 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com706 + ''''},''')


com707 = input("Command 707 - ")
if com707 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com707 + ''''},''')


com708 = input("Command 708 - ")
if com708 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com708 + ''''},''')


com709 = input("Command 709 - ")
if com709 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com709 + ''''},''')


com710 = input("Command 710 - ")
if com710 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com710 + ''''},''')


com711 = input("Command 711 - ")
if com711 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com711 + ''''},''')


com712 = input("Command 712 - ")
if com712 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com712 + ''''},''')


com713 = input("Command 713 - ")
if com713 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com713 + ''''},''')


com714 = input("Command 714 - ")
if com714 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com714 + ''''},''')


com715 = input("Command 715 - ")
if com715 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com715 + ''''},''')


com716 = input("Command 716 - ")
if com716 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com716 + ''''},''')


com717 = input("Command 717 - ")
if com717 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com717 + ''''},''')


com718 = input("Command 718 - ")
if com718 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com718 + ''''},''')


com719 = input("Command 719 - ")
if com719 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com719 + ''''},''')


com720 = input("Command 720 - ")
if com720 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com720 + ''''},''')


com721 = input("Command 721 - ")
if com721 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com721 + ''''},''')


com722 = input("Command 722 - ")
if com722 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com722 + ''''},''')


com723 = input("Command 723 - ")
if com723 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com723 + ''''},''')


com724 = input("Command 724 - ")
if com724 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com724 + ''''},''')


com725 = input("Command 725 - ")
if com725 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com725 + ''''},''')


com726 = input("Command 726 - ")
if com726 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com726 + ''''},''')


com727 = input("Command 727 - ")
if com727 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com727 + ''''},''')


com728 = input("Command 728 - ")
if com728 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com728 + ''''},''')


com729 = input("Command 729 - ")
if com729 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com729 + ''''},''')


com730 = input("Command 730 - ")
if com730 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com730 + ''''},''')


com731 = input("Command 731 - ")
if com731 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com731 + ''''},''')


com732 = input("Command 732 - ")
if com732 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com732 + ''''},''')


com733 = input("Command 733 - ")
if com733 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com733 + ''''},''')


com734 = input("Command 734 - ")
if com734 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com734 + ''''},''')


com735 = input("Command 735 - ")
if com735 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com735 + ''''},''')


com736 = input("Command 736 - ")
if com736 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com736 + ''''},''')


com737 = input("Command 737 - ")
if com737 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com737 + ''''},''')


com738 = input("Command 738 - ")
if com738 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com738 + ''''},''')


com739 = input("Command 739 - ")
if com739 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com739 + ''''},''')


com740 = input("Command 740 - ")
if com740 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com740 + ''''},''')


com741 = input("Command 741 - ")
if com741 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com741 + ''''},''')


com742 = input("Command 742 - ")
if com742 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com742 + ''''},''')


com743 = input("Command 743 - ")
if com743 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com743 + ''''},''')


com744 = input("Command 744 - ")
if com744 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com744 + ''''},''')


com745 = input("Command 745 - ")
if com745 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com745 + ''''},''')


com746 = input("Command 746 - ")
if com746 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com746 + ''''},''')


com747 = input("Command 747 - ")
if com747 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com747 + ''''},''')


com748 = input("Command 748 - ")
if com748 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com748 + ''''},''')


com749 = input("Command 749 - ")
if com749 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com749 + ''''},''')


com750 = input("Command 750 - ")
if com750 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com750 + ''''},''')


com751 = input("Command 751 - ")
if com751 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com751 + ''''},''')


com752 = input("Command 752 - ")
if com752 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com752 + ''''},''')


com753 = input("Command 753 - ")
if com753 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com753 + ''''},''')


com754 = input("Command 754 - ")
if com754 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com754 + ''''},''')


com755 = input("Command 755 - ")
if com755 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com755 + ''''},''')


com756 = input("Command 756 - ")
if com756 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com756 + ''''},''')


com757 = input("Command 757 - ")
if com757 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com757 + ''''},''')


com758 = input("Command 758 - ")
if com758 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com758 + ''''},''')


com759 = input("Command 759 - ")
if com759 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com759 + ''''},''')


com760 = input("Command 760 - ")
if com760 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com760 + ''''},''')


com761 = input("Command 761 - ")
if com761 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com761 + ''''},''')


com762 = input("Command 762 - ")
if com762 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com762 + ''''},''')


com763 = input("Command 763 - ")
if com763 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com763 + ''''},''')


com764 = input("Command 764 - ")
if com764 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com764 + ''''},''')


com765 = input("Command 765 - ")
if com765 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com765 + ''''},''')


com766 = input("Command 766 - ")
if com766 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com766 + ''''},''')


com767 = input("Command 767 - ")
if com767 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com767 + ''''},''')


com768 = input("Command 768 - ")
if com768 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com768 + ''''},''')


com769 = input("Command 769 - ")
if com769 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com769 + ''''},''')


com770 = input("Command 770 - ")
if com770 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com770 + ''''},''')


com771 = input("Command 771 - ")
if com771 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com771 + ''''},''')


com772 = input("Command 772 - ")
if com772 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com772 + ''''},''')


com773 = input("Command 773 - ")
if com773 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com773 + ''''},''')


com774 = input("Command 774 - ")
if com774 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com774 + ''''},''')


com775 = input("Command 775 - ")
if com775 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com775 + ''''},''')


com776 = input("Command 776 - ")
if com776 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com776 + ''''},''')


com777 = input("Command 777 - ")
if com777 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com777 + ''''},''')


com778 = input("Command 778 - ")
if com778 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com778 + ''''},''')


com779 = input("Command 779 - ")
if com779 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com779 + ''''},''')


com780 = input("Command 780 - ")
if com780 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com780 + ''''},''')


com781 = input("Command 781 - ")
if com781 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com781 + ''''},''')


com782 = input("Command 782 - ")
if com782 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com782 + ''''},''')


com783 = input("Command 783 - ")
if com783 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com783 + ''''},''')


com784 = input("Command 784 - ")
if com784 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com784 + ''''},''')


com785 = input("Command 785 - ")
if com785 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com785 + ''''},''')


com786 = input("Command 786 - ")
if com786 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com786 + ''''},''')


com787 = input("Command 787 - ")
if com787 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com787 + ''''},''')


com788 = input("Command 788 - ")
if com788 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com788 + ''''},''')


com789 = input("Command 789 - ")
if com789 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com789 + ''''},''')


com790 = input("Command 790 - ")
if com790 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com790 + ''''},''')


com791 = input("Command 791 - ")
if com791 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com791 + ''''},''')


com792 = input("Command 792 - ")
if com792 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com792 + ''''},''')


com793 = input("Command 793 - ")
if com793 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com793 + ''''},''')


com794 = input("Command 794 - ")
if com794 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com794 + ''''},''')


com795 = input("Command 795 - ")
if com795 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com795 + ''''},''')


com796 = input("Command 796 - ")
if com796 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com796 + ''''},''')


com797 = input("Command 797 - ")
if com797 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com797 + ''''},''')


com798 = input("Command 798 - ")
if com798 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com798 + ''''},''')


com799 = input("Command 799 - ")
if com799 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com799 + ''''},''')


com800 = input("Command 800 - ")
if com800 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com800 + ''''},''')


com801 = input("Command 801 - ")
if com801 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com801 + ''''},''')


com802 = input("Command 802 - ")
if com802 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com802 + ''''},''')


com803 = input("Command 803 - ")
if com803 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com803 + ''''},''')


com804 = input("Command 804 - ")
if com804 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com804 + ''''},''')


com805 = input("Command 805 - ")
if com805 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com805 + ''''},''')


com806 = input("Command 806 - ")
if com806 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com806 + ''''},''')


com807 = input("Command 807 - ")
if com807 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com807 + ''''},''')


com808 = input("Command 808 - ")
if com808 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com808 + ''''},''')


com809 = input("Command 809 - ")
if com809 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com809 + ''''},''')


com810 = input("Command 810 - ")
if com810 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com810 + ''''},''')


com811 = input("Command 811 - ")
if com811 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com811 + ''''},''')


com812 = input("Command 812 - ")
if com812 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com812 + ''''},''')


com813 = input("Command 813 - ")
if com813 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com813 + ''''},''')


com814 = input("Command 814 - ")
if com814 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com814 + ''''},''')


com815 = input("Command 815 - ")
if com815 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com815 + ''''},''')


com816 = input("Command 816 - ")
if com816 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com816 + ''''},''')


com817 = input("Command 817 - ")
if com817 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com817 + ''''},''')


com818 = input("Command 818 - ")
if com818 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com818 + ''''},''')


com819 = input("Command 819 - ")
if com819 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com819 + ''''},''')


com820 = input("Command 820 - ")
if com820 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com820 + ''''},''')


com821 = input("Command 821 - ")
if com821 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com821 + ''''},''')


com822 = input("Command 822 - ")
if com822 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com822 + ''''},''')


com823 = input("Command 823 - ")
if com823 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com823 + ''''},''')


com824 = input("Command 824 - ")
if com824 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com824 + ''''},''')


com825 = input("Command 825 - ")
if com825 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com825 + ''''},''')


com826 = input("Command 826 - ")
if com826 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com826 + ''''},''')


com827 = input("Command 827 - ")
if com827 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com827 + ''''},''')


com828 = input("Command 828 - ")
if com828 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com828 + ''''},''')


com829 = input("Command 829 - ")
if com829 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com829 + ''''},''')


com830 = input("Command 830 - ")
if com830 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com830 + ''''},''')


com831 = input("Command 831 - ")
if com831 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com831 + ''''},''')


com832 = input("Command 832 - ")
if com832 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com832 + ''''},''')


com833 = input("Command 833 - ")
if com833 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com833 + ''''},''')


com834 = input("Command 834 - ")
if com834 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com834 + ''''},''')


com835 = input("Command 835 - ")
if com835 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com835 + ''''},''')


com836 = input("Command 836 - ")
if com836 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com836 + ''''},''')


com837 = input("Command 837 - ")
if com837 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com837 + ''''},''')


com838 = input("Command 838 - ")
if com838 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com838 + ''''},''')


com839 = input("Command 839 - ")
if com839 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com839 + ''''},''')


com840 = input("Command 840 - ")
if com840 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com840 + ''''},''')


com841 = input("Command 841 - ")
if com841 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com841 + ''''},''')


com842 = input("Command 842 - ")
if com842 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com842 + ''''},''')


com843 = input("Command 843 - ")
if com843 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com843 + ''''},''')


com844 = input("Command 844 - ")
if com844 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com844 + ''''},''')


com845 = input("Command 845 - ")
if com845 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com845 + ''''},''')


com846 = input("Command 846 - ")
if com846 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com846 + ''''},''')


com847 = input("Command 847 - ")
if com847 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com847 + ''''},''')


com848 = input("Command 848 - ")
if com848 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com848 + ''''},''')


com849 = input("Command 849 - ")
if com849 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com849 + ''''},''')


com850 = input("Command 850 - ")
if com850 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com850 + ''''},''')


com851 = input("Command 851 - ")
if com851 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com851 + ''''},''')


com852 = input("Command 852 - ")
if com852 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com852 + ''''},''')


com853 = input("Command 853 - ")
if com853 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com853 + ''''},''')


com854 = input("Command 854 - ")
if com854 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com854 + ''''},''')


com855 = input("Command 855 - ")
if com855 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com855 + ''''},''')


com856 = input("Command 856 - ")
if com856 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com856 + ''''},''')


com857 = input("Command 857 - ")
if com857 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com857 + ''''},''')


com858 = input("Command 858 - ")
if com858 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com858 + ''''},''')


com859 = input("Command 859 - ")
if com859 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com859 + ''''},''')


com860 = input("Command 860 - ")
if com860 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com860 + ''''},''')


com861 = input("Command 861 - ")
if com861 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com861 + ''''},''')


com862 = input("Command 862 - ")
if com862 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com862 + ''''},''')


com863 = input("Command 863 - ")
if com863 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com863 + ''''},''')


com864 = input("Command 864 - ")
if com864 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com864 + ''''},''')


com865 = input("Command 865 - ")
if com865 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com865 + ''''},''')


com866 = input("Command 866 - ")
if com866 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com866 + ''''},''')


com867 = input("Command 867 - ")
if com867 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com867 + ''''},''')


com868 = input("Command 868 - ")
if com868 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com868 + ''''},''')


com869 = input("Command 869 - ")
if com869 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com869 + ''''},''')


com870 = input("Command 870 - ")
if com870 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com870 + ''''},''')


com871 = input("Command 871 - ")
if com871 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com871 + ''''},''')


com872 = input("Command 872 - ")
if com872 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com872 + ''''},''')


com873 = input("Command 873 - ")
if com873 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com873 + ''''},''')


com874 = input("Command 874 - ")
if com874 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com874 + ''''},''')


com875 = input("Command 875 - ")
if com875 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com875 + ''''},''')


com876 = input("Command 876 - ")
if com876 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com876 + ''''},''')


com877 = input("Command 877 - ")
if com877 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com877 + ''''},''')


com878 = input("Command 878 - ")
if com878 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com878 + ''''},''')


com879 = input("Command 879 - ")
if com879 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com879 + ''''},''')


com880 = input("Command 880 - ")
if com880 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com880 + ''''},''')


com881 = input("Command 881 - ")
if com881 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com881 + ''''},''')


com882 = input("Command 882 - ")
if com882 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com882 + ''''},''')


com883 = input("Command 883 - ")
if com883 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com883 + ''''},''')


com884 = input("Command 884 - ")
if com884 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com884 + ''''},''')


com885 = input("Command 885 - ")
if com885 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com885 + ''''},''')


com886 = input("Command 886 - ")
if com886 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com886 + ''''},''')


com887 = input("Command 887 - ")
if com887 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com887 + ''''},''')


com888 = input("Command 888 - ")
if com888 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com888 + ''''},''')


com889 = input("Command 889 - ")
if com889 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com889 + ''''},''')


com890 = input("Command 890 - ")
if com890 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com890 + ''''},''')


com891 = input("Command 891 - ")
if com891 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com891 + ''''},''')


com892 = input("Command 892 - ")
if com892 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com892 + ''''},''')


com893 = input("Command 893 - ")
if com893 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com893 + ''''},''')


com894 = input("Command 894 - ")
if com894 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com894 + ''''},''')


com895 = input("Command 895 - ")
if com895 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com895 + ''''},''')


com896 = input("Command 896 - ")
if com896 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com896 + ''''},''')


com897 = input("Command 897 - ")
if com897 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com897 + ''''},''')


com898 = input("Command 898 - ")
if com898 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com898 + ''''},''')


com899 = input("Command 899 - ")
if com899 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com899 + ''''},''')


com900 = input("Command 900 - ")
if com900 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com900 + ''''},''')


com901 = input("Command 901 - ")
if com901 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com901 + ''''},''')


com902 = input("Command 902 - ")
if com902 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com902 + ''''},''')


com903 = input("Command 903 - ")
if com903 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com903 + ''''},''')


com904 = input("Command 904 - ")
if com904 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com904 + ''''},''')


com905 = input("Command 905 - ")
if com905 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com905 + ''''},''')


com906 = input("Command 906 - ")
if com906 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com906 + ''''},''')


com907 = input("Command 907 - ")
if com907 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com907 + ''''},''')


com908 = input("Command 908 - ")
if com908 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com908 + ''''},''')


com909 = input("Command 909 - ")
if com909 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com909 + ''''},''')


com910 = input("Command 910 - ")
if com910 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com910 + ''''},''')


com911 = input("Command 911 - ")
if com911 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com911 + ''''},''')


com912 = input("Command 912 - ")
if com912 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com912 + ''''},''')


com913 = input("Command 913 - ")
if com913 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com913 + ''''},''')


com914 = input("Command 914 - ")
if com914 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com914 + ''''},''')


com915 = input("Command 915 - ")
if com915 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com915 + ''''},''')


com916 = input("Command 916 - ")
if com916 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com916 + ''''},''')


com917 = input("Command 917 - ")
if com917 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com917 + ''''},''')


com918 = input("Command 918 - ")
if com918 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com918 + ''''},''')


com919 = input("Command 919 - ")
if com919 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com919 + ''''},''')


com920 = input("Command 920 - ")
if com920 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com920 + ''''},''')


com921 = input("Command 921 - ")
if com921 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com921 + ''''},''')


com922 = input("Command 922 - ")
if com922 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com922 + ''''},''')


com923 = input("Command 923 - ")
if com923 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com923 + ''''},''')


com924 = input("Command 924 - ")
if com924 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com924 + ''''},''')


com925 = input("Command 925 - ")
if com925 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com925 + ''''},''')


com926 = input("Command 926 - ")
if com926 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com926 + ''''},''')


com927 = input("Command 927 - ")
if com927 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com927 + ''''},''')


com928 = input("Command 928 - ")
if com928 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com928 + ''''},''')


com929 = input("Command 929 - ")
if com929 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com929 + ''''},''')


com930 = input("Command 930 - ")
if com930 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com930 + ''''},''')


com931 = input("Command 931 - ")
if com931 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com931 + ''''},''')


com932 = input("Command 932 - ")
if com932 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com932 + ''''},''')


com933 = input("Command 933 - ")
if com933 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com933 + ''''},''')


com934 = input("Command 934 - ")
if com934 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com934 + ''''},''')


com935 = input("Command 935 - ")
if com935 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com935 + ''''},''')


com936 = input("Command 936 - ")
if com936 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com936 + ''''},''')


com937 = input("Command 937 - ")
if com937 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com937 + ''''},''')


com938 = input("Command 938 - ")
if com938 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com938 + ''''},''')


com939 = input("Command 939 - ")
if com939 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com939 + ''''},''')


com940 = input("Command 940 - ")
if com940 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com940 + ''''},''')


com941 = input("Command 941 - ")
if com941 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com941 + ''''},''')


com942 = input("Command 942 - ")
if com942 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com942 + ''''},''')


com943 = input("Command 943 - ")
if com943 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com943 + ''''},''')


com944 = input("Command 944 - ")
if com944 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com944 + ''''},''')


com945 = input("Command 945 - ")
if com945 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com945 + ''''},''')


com946 = input("Command 946 - ")
if com946 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com946 + ''''},''')


com947 = input("Command 947 - ")
if com947 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com947 + ''''},''')


com948 = input("Command 948 - ")
if com948 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com948 + ''''},''')


com949 = input("Command 949 - ")
if com949 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com949 + ''''},''')


com950 = input("Command 950 - ")
if com950 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com950 + ''''},''')


com951 = input("Command 951 - ")
if com951 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com951 + ''''},''')


com952 = input("Command 952 - ")
if com952 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com952 + ''''},''')


com953 = input("Command 953 - ")
if com953 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com953 + ''''},''')


com954 = input("Command 954 - ")
if com954 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com954 + ''''},''')


com955 = input("Command 955 - ")
if com955 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com955 + ''''},''')


com956 = input("Command 956 - ")
if com956 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com956 + ''''},''')


com957 = input("Command 957 - ")
if com957 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com957 + ''''},''')


com958 = input("Command 958 - ")
if com958 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com958 + ''''},''')


com959 = input("Command 959 - ")
if com959 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com959 + ''''},''')


com960 = input("Command 960 - ")
if com960 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com960 + ''''},''')


com961 = input("Command 961 - ")
if com961 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com961 + ''''},''')


com962 = input("Command 962 - ")
if com962 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com962 + ''''},''')


com963 = input("Command 963 - ")
if com963 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com963 + ''''},''')


com964 = input("Command 964 - ")
if com964 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com964 + ''''},''')


com965 = input("Command 965 - ")
if com965 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com965 + ''''},''')


com966 = input("Command 966 - ")
if com966 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com966 + ''''},''')


com967 = input("Command 967 - ")
if com967 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com967 + ''''},''')


com968 = input("Command 968 - ")
if com968 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com968 + ''''},''')


com969 = input("Command 969 - ")
if com969 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com969 + ''''},''')


com970 = input("Command 970 - ")
if com970 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com970 + ''''},''')


com971 = input("Command 971 - ")
if com971 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com971 + ''''},''')


com972 = input("Command 972 - ")
if com972 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com972 + ''''},''')


com973 = input("Command 973 - ")
if com973 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com973 + ''''},''')


com974 = input("Command 974 - ")
if com974 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com974 + ''''},''')


com975 = input("Command 975 - ")
if com975 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com975 + ''''},''')


com976 = input("Command 976 - ")
if com976 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com976 + ''''},''')


com977 = input("Command 977 - ")
if com977 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com977 + ''''},''')


com978 = input("Command 978 - ")
if com978 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com978 + ''''},''')


com979 = input("Command 979 - ")
if com979 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com979 + ''''},''')


com980 = input("Command 980 - ")
if com980 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com980 + ''''},''')


com981 = input("Command 981 - ")
if com981 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com981 + ''''},''')


com982 = input("Command 982 - ")
if com982 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com982 + ''''},''')


com983 = input("Command 983 - ")
if com983 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com983 + ''''},''')


com984 = input("Command 984 - ")
if com984 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com984 + ''''},''')


com985 = input("Command 985 - ")
if com985 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com985 + ''''},''')


com986 = input("Command 986 - ")
if com986 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com986 + ''''},''')


com987 = input("Command 987 - ")
if com987 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com987 + ''''},''')


com988 = input("Command 988 - ")
if com988 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com988 + ''''},''')


com989 = input("Command 989 - ")
if com989 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com989 + ''''},''')


com990 = input("Command 990 - ")
if com990 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com990 + ''''},''')


com991 = input("Command 991 - ")
if com991 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com991 + ''''},''')


com992 = input("Command 992 - ")
if com992 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com992 + ''''},''')


com993 = input("Command 993 - ")
if com993 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com993 + ''''},''')


com994 = input("Command 994 - ")
if com994 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com994 + ''''},''')


com995 = input("Command 995 - ")
if com995 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com995 + ''''},''')


com996 = input("Command 996 - ")
if com996 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com996 + ''''},''')


com997 = input("Command 997 - ")
if com997 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com997 + ''''},''')


com998 = input("Command 998 - ")
if com998 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com998 + ''''},''')


com999 = input("Command 999 - ")
if com999 == "]go[":
    sendCommand()
else:
    command = (command + '''
{id:command_block_minecart,Command:''''' + "'" + com999 + ''''},''')

#This is just 👌 to let the crazy commanded people that they hav reached the end
print("Command limit reached")

#This fixes the script just closing at the end, with just one line, rather that importing things
input()
