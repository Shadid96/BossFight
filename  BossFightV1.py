import random
#Function for character stat creation
def charCreate(level, title):
    global job
    global HP
    global MP
    global STR
    global DEF
    global MAG
    if title ==1:
        job = "Fighter"
        HP = int(level * 1500)
        MP = int(level * 30)
        STR = int(level * 3)
        DEF = int(level * 2)
        MAG = int(level)
    elif title == 2:
        job = "Soldier"
        HP = level * 2000
        MP = level * 15
        STR = level * 2
        DEF = level * 3
        MAG = level
    elif title == 3:
        job = "White Mage"
        HP = level * 1000
        MP = level * 60
        STR = level * 1
        DEF = level * 2
        MAG = level * 2
    elif title == 4:
        job = "Black Mage"
        HP = level * 1250
        MP = level * 60
        STR = level * 2
        DEF = level * 1
        MAG = level * 2



#Character creation        
aName = str(input("What's your first character's name?: "))

#try/except to ensure only valid numbers entered
while True:
    try:
        aTitle = int(input( "What class is this character?\n"
                "1. Fighter\n"
                "2. Soldier\n"
                "3. White Mage\n"
                "4. Black Mage\n"))
        if aTitle in range (1,5):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass

while True:
    try:
        aLevel = int(input("What level is this character? (Input number from 1 to 99): "))
        if aTitle in range (1,100):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass

charCreate(aLevel, aTitle)#call function
aJob = job
aHP= HP
aHPmax = HP
aMP = MP
aSTR = STR
aDEF = DEF
aMAG = MAG


#Repeat
bName = str(input("What's your second character's name?: "))
while True:
    try:
        bTitle = int(input( "What class is this character?\n"
                "1. Fighter\n"
                "2. Soldier\n"
                "3. White Mage\n"
                "4. Black Mage\n"))
        if bTitle in range (1,5):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass

while True:
    try:
        bLevel = int(input("What level is this character? (Input number from 1 to 99): "))
        if bTitle in range (1,100):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass
charCreate(bLevel, bTitle)
bJob = job
bHP= HP
bHPmax= HP
bMP = MP
bSTR = STR
bDEF = DEF
bMAG = MAG

cName = str(input("What's your third character's name?: "))
while True:
    try:
        cTitle = int(input( "What class is this character?\n"
                "1. Fighter\n"
                "2. Soldier\n"
                "3. White Mage\n"
                "4. Black Mage\n"))
        if cTitle in range (1,5):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass

while True:
    try:
        cLevel = int(input("What level is this character? (Input number from 1 to 99): "))
        if cTitle in range (1,100):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass
charCreate(cLevel, cTitle)
cJob = job
cHP= HP
cHPmax = HP
cMP = MP
cSTR = STR
cDEF = DEF
cMAG = MAG

dName = str(input("What's your last character's name?: "))
while True:
    try:
        dTitle = int(input( "What class is this character?\n"
                "1. Fighter\n"
                "2. Soldier\n"
                "3. White Mage\n"
                "4. Black Mage\n"))
        if dTitle in range (1,5):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass

while True:
    try:
        dLevel = int(input("What level is this character? (Input number from 1 to 99): "))
        if dTitle in range (1,100):
            break
        else:
            print("Bad value")
    except ValueError:
        print("Sorry, I didn't understand that.")
        pass
charCreate(dLevel, dTitle)
dJob = job
dHP= HP
dHPmax = HP
dMP = MP
dSTR = STR
dDEF = DEF
dMAG = MAG

teamHP = aHP + bHP + cHP + dHP #to begin calculations for game


print("\nYour fighters are:\n",aName,", a level", aLevel, aJob,": ",aHP, "HP, ",aMP, "MP")
print(bName,", a level", bLevel, bJob,": ",bHP, "HP, ",bMP, "MP,")
print(cName,", a level", cLevel, cJob,": ",cHP, "HP, ",cMP, "MP,")
print("and ",dName,", a level", dLevel, dJob,": ",dHP, "HP, ",dMP, "MP.\n")

#create boss stats
bossLevel = int((aLevel+ bLevel+ cLevel+ dLevel)/4 + 5)
bossHP = int((aHP+ bHP+ cHP+ dHP) * 1.5)
bossHPmax = bossHP
bossMP = int((aMP+ bMP+ cMP+ dMP) * 1.5)
bossSTR = bossLevel * 3
bossDEF = bossLevel * 3
bossMAG = bossLevel * 3
heartlessAmmo = 1
poison = 0
enemyPoison = 0
enemySleep = 0

print(" The level", bossLevel, "boss has ",bossHP, "hitpoints")

#Function to set up active stats
def active(user):
    global XHP
    global XHPmax
    global XMP
    global XSTR
    global XDEF
    global XMAG
    global aHP
    global aHPmax
    global aMP
    global aSTR
    global aDEF
    global aMAG
    global bHP
    global bHPmax
    global bMP
    global bSTR
    global bDEF
    global bMAG
    global cHP
    global cHPmax
    global cMP
    global cSTR
    global cDEF
    global cMAG
    global dHP
    global dHPmax
    global dMP
    global dSTR
    global dDEF
    global dMAG
    if user == 1:
        XHP= aHP
        XHPmax = aHPmax
        XMP = aMP
        XSTR = aSTR
        XDEF = aDEF
        XMAG = aMAG
    elif user == 2:
        XHP= bHP
        XHPmax = bHPmax
        XMP = bMP
        XSTR = bSTR
        XDEF = bDEF
        XMAG = bMAG
    elif user == 3:
        XHP= cHP
        XHPmax = cHPmax
        XMP = cMP
        XSTR = cSTR
        XDEF = cDEF
        XMAG = cMAG
    elif user == 4:
        XHP= dHP
        XHPmax = dHPmax
        XMP = dMP
        XSTR = dSTR
        XDEF = dDEF
        XMAG = dMAG

def inactive(user):
    global XHP
    global XHPmax
    global XMP
    global XSTR
    global XDEF
    global XMAG
    global aHP
    global aHPmax
    global aMP
    global aSTR
    global aDEF
    global aMAG
    global bHP
    global bHPmax
    global bMP
    global bSTR
    global bDEF
    global bMAG
    global cHP
    global cHPmax
    global cMP
    global cSTR
    global cDEF
    global cMAG
    global dHP
    global dHPmax
    global dMP
    global dSTR
    global dDEF
    global dMAG
    if user == 1:
        aHP= XHP
        aHPmax = XHPmax
        aMP = XMP
        aSTR = XSTR
        aDEF = XDEF
        aMAG = XMAG
    elif user == 2:
        bHP= XHP
        bHPmax = XHPmax
        bMP = XMP
        bSTR = XSTR
        bDEF = XDEF
        bMAG = XMAG
    elif user == 3:
        cHP= XHP
        cHPmax = XHPmax
        cMP = XMP
        cSTR = XSTR
        cDEF = XDEF
        cMAG = XMAG
    elif user == 4:
        cHP= XHP
        cHPmax = XHPmax
        cMP = XMP
        cSTR = XSTR
        cDEF = XDEF
        cMAG = XMAG

fighterMenu = """
                 ____________________________________________________
                |++++++++++++++++++++++++++++++++++++++++++++++++++++|
                |+ 1.Punch- Hi DMG, costs HP                        +|
                |+ 2.Slash- Lo DMG                                  +|
                |+ 3.Lucky Sevens- 7, 77, 777 or 7777 damage (5 MP) +|
                |+ 4.Potion- +20% health (30 MP)                    +|
                |+  \  /                                            +|
                |+   \/   LIMIT BREAK                               +|
                |+   /\   DEMI: Lower oppenent's health by 25%      +|
                |+  /  \  (Enter "5" If less your HP that 20% hp)   +|
                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"""
def fighter(a):
    global DMG
    global REC
    global defBoost
    global bossHP
    global XHP
    global XSTR
    global XDEF
    global XMAG
    global XMP
    global poison
    global enemyPoison
    global bossDEF
    global enemySleep
    global XHPmax
    
    if a == 1:
        DMG = XSTR *1000/bossDEF
        REC = XSTR *250
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        XHP = XHP - round(DMGval)
        print("Did ", round(DMGval), "damage to boss with ", round(REC/XDEF), "Damage done to the character")
    
    elif a == 2:
        DMG = XSTR * 500/bossDEF
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        print("Did ", round(DMGval), "damage!")
    elif a == 3:
        XMP = XMP - 5
        sevens = random.randint(1,4)
        if sevens == 1:
            DMG = 7
        elif sevens == 2:
            DMG = 77
        elif sevens == 3:
            DMG = 777
        elif sevens == 4:
            DMG = 7777
        bossHP = bossHP - DMG
        print(" Did ", DMG, "points of damage!")
    elif a == 4:
        XMP = XMP - 30
        if XHP <= 4*XHPmax/5 and XHP > 0:
            XHP = round(XHP + XHPmax/5)
        elif XHP >= 4*XHPmax/5 and XHP > 0:
            XHP = XHPmax
        print("Healed! Health is now ",XHP)
    elif a == 5:
        if XHP <= XHPmax/5:
            bossHP = round(bossHP*3/4)
            print("Special move! You cast DEMI")
            print("Did ", bossHP/4, "damage!")
        else:
            print("Action Failed!")
    
    
soldierMenu = """
                 ______________________________________
                |++++++++++++++++++++++++++++++++++++++|
                |+ 1.Shoot- Lo DMG                    +|
                |+ 2.Grenade- Hi DMG, costs HP        +|
                |+ 3.Difference-Damage = maxHp-HP(5MP)+|
                |+ 4.Potion- +20% health (30MP)       +|
                |+  \  /                              +|
                |+   \/   LIMIT BREAK                 +|
                |+   /\   BERSERK:Permanently up ATK! +|
                |+  /  \ (Enter 5 if less that 20% hp)+|
                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"""
def soldier(a):
    global DMG
    global REC
    global defBoost
    global bossHP
    global XHP
    global XSTR
    global XDEF
    global XMAG
    global XMP
    global poison
    global enemyPoison
    global bossDEF
    global enemySleep
    global XHPmax
    if a == 1:
        DMG = XSTR * 500/bossDEF
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        print("Did ", round(DMGval), "damage!")
    elif a == 2:
        DMG = XSTR *1000/bossDEF
        REC = XSTR *250
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        XHP = XHP - round(REC/XDEF)
        print("Did ", round(DMGval), "damage to boss with ", round(REC/XDEF), "Damage done to the character")
    
    elif a == 3:
        XMP = XMP-5
        DMG = XHPmax - XHP
        bossHP = bossHP-round(DMG)
        print("Did ", round(DMG), "damage!")
        
    elif a == 4:
        XMP = XMP - 30
        if XHP <= 4*XHPmax/5 and XHP > 0:
            XHP = round(XHP + XHPmax/5)
        elif XHP >= 4*XHPmax/5 and XHP > 0:
            XHP = XHPmax
        print("Healed! Health is now ",XHP)
    elif a == 5:
        if XHP <= XHPmax/5:
            XSTR = XSTR* 1.5
            print("Special move! Berserk increased attack stat by 50% permanently!")
        else:
            print("Action Failed!")

wmMenu =      """
                 ______________________________________
                |++++++++++++++++++++++++++++++++++++++|
                |+ 1.CureAll- +40% HP for all (100 MP)+|
                |+ 2.Antidote- Remove poison  (20 MP) +|
                |+ 3.Wack- Miniscule Damage           +|
                |+ 4.Revive- 1/4 HP for down (50 MP)  +|
                |+  \  /                              +|
                |+   \/   LIMIT BREAK                 +|
                |+   /\   ABSORB:Team absorbs boss HP +|
                |+  /  \  Press 5 if less that 20% hp +|
                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"""
def healer(a):
    global DMG
    global REC
    global defBoost
    global bossHP
    global XHP
    global XSTR
    global XDEF
    global XMAG
    global XMP
    global poison
    global enemyPoison
    global bossDEF
    global enemySleep
    global XHPmax
    global aHP
    global aHPmax
    global bHP
    global bHPmax
    global cHP
    global cHPmax
    global dHP
    global dHPmax
    global revival
    if a ==1:
        XMP = XMP- 100
        if aHP <= 4*aHPmax/5 and aHP > 0:
            aHP = round(aHP + aHPmax/5)
        elif aHP >= 4*aHPmax/5 and aHP > 0:
            aHP = aHPmax
       
        if bHP <= 4*bHPmax/5 and bHP > 0:
            bHP = round(bHP + bHPmax/5)
        elif bHP >= 4*bHPmax/5 and bHP > 0:
            bHP = bHPmax
        
        if cHP <= 4*cHPmax/5 and cHP > 0:
            cHP = round(cHP + cHPmax/5)
        elif cHP >= 4*cHPmax/5 and cHP > 0:
            cHP = cHPmax
        
        if dHP <= 4*dHPmax/5 and dHP > 0:
            dHP = round(dHP + dHPmax/5)
        elif dHP >= 4*dHPmax/5 and dHP > 0:
            dHP = dHPmax
        print("Everyone was healed!")
        
    elif a == 2:
        XMP = XMP - 20
        poison = 0 
        print("No more poison!")
        
    elif a == 3:
        DMG = XSTR * 5
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        print("Did ", round(DMGval), "damage!")
        
    elif a == 4:
        XMP = XMP - 50
        while True:
            try:
                revival = int(input("Who needs reviving? player 1, 2, 3, or 4?"))
                if a in range (1,5):
                    break
                else:
                    print("Bad value")
                    continue
            except ValueError:
                print("Sorry, I didn't understand that.")
        if revival == 1 and aHP <= 0:
                aHP = round(aHPmax/2)
                print(aName, "Revived!")
        elif revival == 2 and bHP <= 0:
                bHP = round(bHPmax/2)
                print(bName, "Revived!")
        elif revival == 1 and cHP <= 0:
                cHP = round(cHPmax/2)
                print(cName, "Revived!")
        elif revival == 1 and dHP <= 0:
                dHP = round(dHPmax/2)
                print(dName, "Revived!")
        else: print("Nothing happened.")
            
    elif a == 5:
        if XHP <= XHPmax/5:#add down clause
            DMG = round(DMG/bossDEF)
            bossHP = bossHP - DMG
            
            if aHP <= aHPmax:
                aHP = round(aHP + DMG/4)
            else: aHP = aHPmax
            
            if bHP <= bHPmax:
                bHP = round(bHP + DMG/4)
            else: bHP = bHPmax
            
            if cHP <= cHPmax:
                cHP = round(cHP + DMG/4)
            else: cHP = cHPmax
            
            if dHP <= dHPmax:
                dHP = round(dHP + DMG/4)
            else: dHP = dHPmax
        else:
            print("Action Failed!")
        print("Special move! Absorbed and split ", bossHP*.02,"HP from boss!")
    
            
bmMenu =      """
                 _______________________________________________
                |+++++++++++++++++++++++++++++++++++++++++++++++|
                |+ 1.Meteor- Hi DMG, costs HP                  +|
                |+ 2.Poison-Cause DMG/turn (15 MP)             +|
                |+ 3.Sleep- 50% chance (15 MP)                 +|
                |+ 4.Potion- +20% health (15 MP)               +|
                |+  \  /                                       +|
                |+   \/   LIMIT BREAK                          +|
                |+   /\   ULTIMA: Massive Magic Damage         +|
                |+  /  \  Press 5 if less than 20% hp          +|
                TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"""
def wizard(a):
    global DMG
    global REC
    global defBoost
    global bossHP
    global XHP
    global XSTR
    global XDEF
    global XMAG
    global XMP
    global poison
    global enemyPoison
    global bossDEF
    global enemySleep
    global XHPmax
    if a == 1:
        DMG = XMAG *800
        REC = XMAG *500
        DMGval = random.randint(round(DMG*0.85), round(DMG*1.15))
        bossHP = bossHP - round(DMGval)
        XHP = XHP - round(REC/XDEF)
        print("Did ", round(DMGval), "damage to boss with ", round(REC/XDEF), "Damage done to the character")
    
    elif a == 2:
        XMP = XMP - 15
        enemyPoison = 1
        print("Enemy posioned!")
    
    elif a == 3:
        XMP = XMP - 15
        enemySleep = 1
        print("Enemy put to sleep!")
    
    elif a == 4:
        XMP = XMP - 15
        if XHP <= 4*XHPmax/5 and XHP > 0:
            XHP = round(XHP + XHPmax/5)
        elif XHP >= 4*XHPmax/5 and XHP > 0:
            XHP = XHPmax
        print("Healed! Health is now ",XHP)
    
    elif a == 5:
        if XHP <= XHPmax/5:
            DMG = XMAG *2000
            bossHP = round(bossHP - DMG/boss/DEF)


def boss(z):
    global DMG
    global enemyPoison
    global poison
    global aHP
    global aDEF
    global bHP
    global bDEF
    global cHP
    global cDEF
    global dHP
    global dDEF
    global target
    global bossSTR
    global heartlessAmmo
    if z == 1:
        enemyPoison = 0
        print("The boss casted Antidote! He's no longer poisoned.")
    if z == 2:
        poison = 1
        print("The boss casted poison! The team is now poisoned")
    if z == 3:
        DMG = (bossSTR *7500)
        aHP = aHP - round(DMG/aDEF)
        bHP = bHP - round(DMG/bDEF)
        cHP = cHP - round(DMG/cDEF)
        dHP = dHP - round(DMG/dDEF)
        print("The boss slashed your team!")
        print(aName, "took ", round(DMG/aDEF), "Damage")
        print(bName, "took ", round(DMG/bDEF), "Damage")
        print(cName, "took ", round(DMG/cDEF), "Damage")
        print(dName, "took ", round(DMG/dDEF), "Damage")
        
    if z == 4:
        target = random.randint(1,4)
        DMG = (bossSTR *10000)
        if target == 1:
            aHP = aHP - round(DMG/aDEF)
            print("The boss slashed", aName, "for",round(DMG/aDEF), "!")
        elif target == 2:
            bHP = bHP - round(DMG/bDEF)       
            print("The boss slashed", bName, "for",round(DMG/aDEF), "!")
        elif target == 3:
            cHP = cHP - round(DMG/cDEF)
            print("The boss slashed", cName, "for",round(DMG/aDEF), "!")
        elif target == 4:
            dHP = dHP - round(DMG/dDEF)
            print("The boss slashed", dName, "for",round(DMG/aDEF), "!")

    if z == 5 and heartlessAmmo == 1:
        aHP = 1
        bHP = 1
        cHP = 1
        dHP = 1
        heartlessAmmo = 0
        enemySleep = 1
        print("The boss is desperate! He dropped everyone's HP to 1. The boss is recharging.")
        
#Boss Moves:
#1. antidote
#2. poison 
#3. attackAll
#4. attackOne
#5. heartless



if aTitle == 1:
    amenu = fighterMenu
elif aTitle == 2:
    amenu = soldierMenu
elif aTitle == 3:
    amenu = wmMenu
elif aTitle == 4:
    amenu = bmMenu
    
if bTitle == 1:
    bmenu = fighterMenu
elif bTitle == 2:
    bmenu = soldierMenu
elif bTitle == 3:
    bmenu = wmMenu
elif bTitle == 4:
    bmenu = bmMenu
    
if cTitle == 1:
    cmenu = fighterMenu
elif cTitle == 2:
    cmenu = soldierMenu
elif cTitle == 3:
    cmenu = wmMenu
elif cTitle == 4:
    cmenu = bmMenu
    
if dTitle == 1:
    dmenu = fighterMenu
elif dTitle == 2:
    dmenu = soldierMenu
elif dTitle == 3:
    dmenu = wmMenu
elif dTitle == 4:
    dmenu = bmMenu

#Actual fight code
while bossHP > 0 or teamHP > 0:
    print("\nBoss HP: ",bossHP,"\n")
    print(aName,": ",aHP, "HP, ",aMP, "MP")
    print(bName,": ",bHP, "HP, ",bMP, "MP,")
    print(cName,": ",cHP, "HP, ",cMP, "MP,")
    print(dName,": ",dHP, "HP, ",dMP, "MP.\n")

    if aHP>0:
        active(1)
        print(aName,"'s turn!\n")
        if aHP <= aHPmax/20:
            print("Limit available")
        if poison == 1:
            aHP = aHP - round(aHP/32)
            print(aName, "took ",round(aHP/32), "poison damage!")
        print(aHP, "HP---",aMP, "MP\n")
        print(amenu)
        while True:
            try:
                a = int(input("Choose your action: \n"))
                if a in range (1,6):
                    break
                else:
                    print("Bad value")
            except ValueError:
                print("Sorry, I didn't understand that.")
                pass
        if aTitle == 1:
            fighter(a)
        elif aTitle == 2:
            soldier(a)
        elif aTitle == 3:
            healer(a)
        elif aTitle == 4:
            wizard(a)
        inactive(1)

    
    teamHP = aHP + bHP + cHP + dHP
    print("\nBoss HP: ",bossHP,"\n")
    print(aName,": ",aHP, "HP, ",aMP, "MP")
    print(bName,": ",bHP, "HP, ",bMP, "MP,")
    print(cName,": ",cHP, "HP, ",cMP, "MP,")
    print(dName,": ",dHP, "HP, ",dMP, "MP.\n") 

    if bHP>0:
        active(2)
        print(bName,"'s turn!\n")
        if bHP <= bHPmax/20:
            print("Limit available")
        if poison == 1:
            bHP = bHP - round(bHP/32)
            print(bName, "took ",round(bHP/32), "poison damage!")
        print(bHP, "HP---",bMP, "MP\n")
        print(bmenu)
        while True: 
            try:
                a = int(input("Choose your action: \n"))
                if a in range (1,6) :
                    break
                else:
                    print("Bad value")
            except ValueError:
                print("Sorry, I didn't understand that.")
                pass
        if bTitle == 1:
            fighter(a)
        elif bTitle == 2:
            soldier(a)
        elif bTitle == 3:
            healer(a)
        elif bTitle == 4:
            wizard(a)  
        inactive(2)
    
    teamHP = aHP + bHP + cHP + dHP

    
    print("\nBoss HP: ",bossHP,"\n")
    print(aName,": ",aHP, "HP, ",aMP, "MP")
    print(bName,": ",bHP, "HP, ",bMP, "MP,")
    print(cName,": ",cHP, "HP, ",cMP, "MP,")
    print(dName,": ",dHP, "HP, ",dMP, "MP.\n")
    
    if cHP > 0:
        active(3)
        print(cName,"'s turn!\n")
        if cHP <= cHPmax/20:
            print("Limit available")
        if poison == 1:
            cHP = cHP - round(cHP/32)
            print(cName, "took ",round(cHP/32), "poison damage!")
        print(cHP, "HP---",aMP, "MP\n")
        print(cmenu)
        while True: 
            try:
                a = int(input("Choose your action: \n"))
                if a in range (1,6) :
                    break
                else:
                    print("Bad value")
            except ValueError:
                print("Sorry, I didn't understand that.")
                pass
        if cTitle == 1:
            fighter(a)
        elif cTitle == 2:
            soldier(a)
        elif cTitle == 3:
            healer(a)
        elif cTitle == 4:
            wizard(a)
        inactive(3)
    
    teamHP = aHP + bHP + cHP + dHP

    
    print("\nBoss HP: ",bossHP,"\n")
    print(aName,": ",aHP, "HP, ",aMP, "MP")
    print(bName,": ",bHP, "HP, ",bMP, "MP,")
    print(cName,": ",cHP, "HP, ",cMP, "MP,")
    print(dName,": ",dHP, "HP, ",dMP, "MP.\n")
    
    if dHP > 0:
        active(4)
        print(dName,"'s turn!\n")
        if dHP <= dHPmax/20:
            print("Limit available")
        if poison == 1:
            dHP = dHP - round(dHP/32)
            print(dName, "took ",round(dHP/32), "poison damage!")
        print(dHP, "HP---",aMP, "MP\n")
        print(dmenu)
        while True: 
            try:
                a = int(input("Choose your action: \n"))
                if a in range (1,6):
                    break
                else:
                    print("Bad value")
            except ValueError:
                print("Sorry, I didn't understand that.")
                pass
        if dTitle == 1:
            fighter(a)
        elif dTitle == 2:
            soldier(a)
        elif dTitle == 3:
            healer(a)
        elif dTitle == 4:
            wizard(a)
        inactive(4)

    teamHP = aHP + bHP + cHP + dHP

    print("\nBoss HP: ",bossHP,"\n")
    print(aName,": ",aHP, "HP, ",aMP, "MP")
    print(bName,": ",bHP, "HP, ",bMP, "MP,")
    print(cName,": ",cHP, "HP, ",cMP, "MP,")
    print(dName,": ",dHP, "HP, ",dMP, "MP.\n")
    print("******"")
    esuna = 2
    if enemySleep == 1:
        print("The boss is asleep!")
        enemySleep = 0
    if enemyPoison == 1:
        bossHP = bossHP-round(bossHP/64)
        print("The boss took", round(bossHP/64), "poison damage.")
        esuna = random.randint(1,2)
    if esuna == 1:
        z = 1
    elif esuna == 2:
        if bossHP >= bossHPmax/50:
            z = random.randint(2,4)
        elif bossHP < bossHPmax/50 and heartlessAmmo == 1:
            z = 5
            heartlessAmmo = 0

    
    boss(z)
    print("******")    
    
          teamHP = aHP + bHP + cHP + dHP
Print("Game Over.")