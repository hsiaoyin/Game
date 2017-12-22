#Insurance Parameter
OrigwInsurance=12 #Number of block
OrigProb=0.05
Times=5
Prob=OrigProb/(OrigwInsurance+Times)
Prob2=Prob*Times
Premium=1.5
WinsP=12.5
OrigMoney=20

def DrawBridge(i,color):
    pygame.draw.line(screen, color, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)


def TommyFigure(screen,moving_x,moving_y,Press):
    pygame.draw.ellipse(screen,BLACK,[65+moving_x,15+moving_y,50,50])
    #Body
    pygame.draw.rect(screen,RED,[65+moving_x,65+moving_y,50,100])
    #Arm
    pygame.draw.line(screen, BLACK, [65+moving_x,105+moving_y], [50+moving_x,5+moving_y], 10)
    pygame.draw.line(screen, BLACK, [115+moving_x,105+moving_y], [120+moving_x,5+moving_y],10)
    #leg
    pygame.draw.line(screen, BLACK, [75+moving_x,165+moving_y], [60+moving_x,200+moving_y], 10)
    pygame.draw.line(screen, BLACK, [105+moving_x,165+moving_y], [110+moving_x,200+moving_y], 10)
    pygame.draw.ellipse(screen,MONEY_C,[50+moving_x,+moving_y,80,20])

def Introduction(Case):
    if Case==1:
        a=RuleText
    else:
        a=IntroText
    return(a)

def Background():
    screen.fill(WHITE)
    screen.blit(TommyText,HeadPosition)
    pygame.draw.line(screen, BLACK, [0,230+space], [1150,230+space], 5)
    pygame.draw.line(screen, BLACK, [0,370+space], [1150,370+space], 5)
    pygame.draw.rect(screen, GREEN, [0,0,165,7000])
    pygame.draw.rect(screen, GREEN, [1100,0,7000,7000])

    for i in range(13):
        DrawBridge(i,BRIDGE_C)
    DrawBridge(3,GRAY_C)
    DrawBridge(0,GREEN)




class Setup():

    def __init__(self):
        self.moving_x=18
        self.moving_y=250
        self.Fall=0
        self.Press=False
        self.Bomp=False
        self.Count=0
        self.money=OrigMoney
        self.Buy=0
        self.InsuranceList=list()
        self.InYN=False



import sqlite3
import pygame_textinput
import pygame
import random
nameID=input("please enter your student ID")
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (154, 214, 137)
RED = (255, 0, 0)
MONEY_C=(250,234,5)
BRIDGE_C=(107,57,0)
GRAY_C=(237,177,97)
InsBridge_C=(100,111,115)
DarkRed=(173,52,78)
pygame.init()

# Set the width and height of the screen [width, height] and other game parameters
size = (7000, 7000)
Left=200
SecondLeft=1110
HeadPosition=[Left+20,30]
SecondPosition=[Left,800]
SecondTop=[Left,140]
TopPosition=[Left, 80]

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
Speed=80
FallSpeed=-30
pygame.display.set_caption("Tommy Crossing Bridge")
font = pygame.font.SysFont('Calibri', 25, True, False)
font1 = pygame.font.SysFont('Calibri', 50, True, False)
Space1=500
Space2=Space1-150

#Words
TommyMoney="When Tommy arrives, "
TommyMoney=font.render(TommyMoney,True,BLACK)
TommyMoney2="you will get "
TommyMoney2=font.render(TommyMoney2,True,BLACK)
BuyInsurance=". To buy for the next one, press UP"
InsurSale="One block costs CHF"
InsurSale= font.render(InsurSale+str(Premium)+BuyInsurance,True,RED)
BompText="No!!! Broken bock! You lose all the money!!"
BompText= font1.render(BompText,True,RED)
FinText="Success! Congrats that Tommy has managed to bring you CHF"
RuleText=\
"Tommy is bringing your money. \n\
You will get this money when Tommy crosses the bridge. \n\
However, this bridge, made up of 12 blocks, \nhas averagely " +str(100*OrigProb)+"% probability \
that it may break. \nThe third block is rotten (marked as light brown on the bridge). \n\
Non-rotten blocks have equal breaking probability\n\
while the rotten block has "+str(Times)+" times more likely to break than the unrotten ones. \n\
If the bridge breaks, Tommy will fall and you lose all your money. \n\
You can pay CHF " +str(OrigMoney-WinsP)+ " for insurance protecting Tommy from falling.\n\
In this case, you will get paid CHF "+str(WinsP)+". \n\
If you want to take the risk, \n\
you can still buy individual block insurance separately when Tommy is on the bridge.\n\
This insurance per block costs CHF "+str(Premium)+". \n\
Press DOWN to continue"
BackText="You can check on the right side the money you will earn when Tommy crosses the bridge"
RuleText=RuleText.splitlines()
IntroText=\
" Press UP if you prefer an insurance. (In this case, you will get paid CHF "+str(WinsP)+"!) \n \
Otherwise press RIGHT to help Tommy cross the bridge. \n\
(You can buy insurance per block on the way)!"
IntroText=IntroText.splitlines()
TommyText="Tommy is going to bring you the money"
TommyBridge="Tommy is going to bring you the money but the bridge may fall with 5% probability"
TommyText= font.render(TommyText,True,BLACK)
TommyBridge=font.render(TommyBridge,True,BLACK)
Practice="Practice Demo-- Please follow the step:"
Practice= font.render(Practice,True,InsBridge_C)
InsNoBomp= font1.render("The block is safe but you are insured anyway" ,True,RED)
InsBomp= font1.render("The block is broken but luckily you are insured" ,True,RED)

#To begin
done0=False
done1=False
done2=False
done=False

######################################################################################################
InitialSetup=Setup()

Case=1

space=Space1
Enter=0
while not done0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done0= True
            done1 = True
            done2= True
            done=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and Case==2:
                done0=True
            elif event.key ==pygame.K_DOWN:
                Case=2
            elif event.key ==pygame.K_UP and Case==2:
                done0=True
                done1=True
                done2=True
                money=OrigwInsurance



    Background()

    TommyFigure(screen,InitialSetup.moving_x,InitialSetup.moving_y+space-100,InitialSetup.Press)

    tempText=Introduction(Case)
    for i in range(len(tempText)):
        text7= font.render(tempText[i],True,DarkRed)
        screen.blit(text7, [Left, space-400+i*40])


    pygame.display.flip()

#######################################################################################################
space=Space2
result=0
while not done1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done1 = True
            done2= True
            done=True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and (InitialSetup.Count==0 or InitialSetup.Buy==1 or InitialSetup.Count==3):# or result==0):
                print(InitialSetup.Count,InitialSetup.Buy,result)
                if result==0:
                    result=1
                    InitialSetup.Buy=0
                else:
                    InitialSetup.Count=InitialSetup.Count+1
                    InitialSetup.moving_x=InitialSetup.moving_x+Speed
                    InitialSetup.Press=True
                    result=0

                    if InitialSetup.Count==4:
                        InitialSetup.Bomp=True
                        InitialSetup.Fall=FallSpeed
                        InitialSetup.money=0

                    elif InitialSetup.Count==2:
                        InitialSetup.Bomp==False
                        InitialSetup.InYN=True

                    elif InitialSetup.Count==3:
                        InitialSetup.Bomp=False
                        InitialSetup.InYN=False

            elif event.key == pygame.K_UP and (InitialSetup.Count==1 or InitialSetup.Count==2) and  InitialSetup.Buy==0:
                InitialSetup.Buy=1
                InitialSetup.money=InitialSetup.money-Premium
                InitialSetup.InsuranceList.append(InitialSetup.Count+1)
                result=1

            elif event.key ==pygame.K_DOWN and InitialSetup.Count==4:
                done1=True

            elif event.key==pygame.K_LEFT and InitialSetup.Count==4:
                InitialSetup=Setup()

    Background()


    text4= font1.render(" CHF"+str(InitialSetup.money),True,RED)

    extrainfo=""
    screen.blit(TommyMoney, [SecondLeft,200])
    screen.blit(TommyMoney2, [SecondLeft,250])
    screen.blit(text4, [SecondLeft,300])
#Draw Bridge
    for i in InitialSetup.InsuranceList:
        DrawBridge(i,InsBridge_C)

    TommyFigure(screen,InitialSetup.moving_x,InitialSetup.moving_y+space-100,InitialSetup.Press)
    InitialSetup.moving_y -=InitialSetup.Fall

    extrainfo="Crossing without insurance "
    extrainfo1="Press RIGHT"


    if result==0:
        extrainfo=BackText
        extrainfo1="press RIGHT to continue:"#

    if InitialSetup.Count==1:

        extrainfo="Next: to acquire individual insurance"
        extrainfo1="Press UP to get insured and RIGHT to continue:"

    elif InitialSetup.Count==2:
        if result==0:
            screen.blit(InsNoBomp,SecondPosition)
        else:
            extrainfo="Next: You are insured while the block is broken"
            extrainfo1="press UP to get insured and RIGHT to continue:"

    elif InitialSetup.Count==3:
        if result==0:
            InitialSetup.Bomp=True
            screen.blit(InsBomp,SecondPosition)
        else:
            extrainfo="Next: Crossing while the block is broken"

    elif InitialSetup.Count==4:
        InitialSetup.Bomp=False
        screen.blit(BompText, SecondPosition)
        extrainfo="End of Demo, Press DOWN to start the game"
        extrainfo1="Or press LEFT to replay the demo again"

    text8= font.render(extrainfo,True,DarkRed)
    text9= font.render(extrainfo1,True,RED)

    screen.blit(Practice, TopPosition)
    screen.blit(text8,[Left,130])
    screen.blit(text9,[Left,160])
    pygame.display.flip()

InitialSetup=Setup()

    ######################################################################################################
while not done2:
    Enter=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done2 = True
            done=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and InitialSetup.Count<12:
                InitialSetup.moving_x=InitialSetup.moving_x+Speed
                InitialSetup.Press=True
                InitialSetup.Count=InitialSetup.Count+1
                x=random.random()

                if InitialSetup.Count==3:
                    InitialSetup.Bomp=x<Prob2
                else:
                    InitialSetup.Bomp=x<Prob

                if InitialSetup.Buy==1:
                    if InitialSetup.Bomp==True:
                        InitialSetup.InYn=True
                    else:
                        InitialSetup.InYn=False
                    InitialSetup.Bomp=False
                    InitialSetup.Buy=0

                print(x,InitialSetup.Bomp,Prob,InitialSetup.Count,InitialSetup.InsuranceList,InitialSetup.Buy)
                if InitialSetup.Bomp==True:
                    InitialSetup.Fall=FallSpeed
                    InitialSetup.money=0

            elif event.key == pygame.K_UP and InitialSetup.Count<11:
                InitialSetup.Buy=1
                InitialSetup.money=InitialSetup.money-Premium
                InitialSetup.InsuranceList.append(InitialSetup.Count+1)

            elif event.key ==pygame.K_DOWN and InitialSetup.Count>=11:
                done2=True


    Background()

    text4= font1.render(" CHF"+str(InitialSetup.money),True,RED)
    text6= font1.render(FinText+str(InitialSetup.money)+"!" ,True,RED)
    text5= font1.render("Press DOWN to continue" ,True,BLACK)

    screen.blit(TommyMoney, [SecondLeft,200])
    screen.blit(TommyMoney2, [SecondLeft,250])
    screen.blit(text4, [SecondLeft,300])


    for i in InitialSetup.InsuranceList:
        DrawBridge(i,InsBridge_C)

    TommyFigure(screen,InitialSetup.moving_x,InitialSetup.moving_y+space-100,InitialSetup.Press)


    if InitialSetup.Bomp==True:
        screen.blit(BompText, SecondPosition)

    elif InitialSetup.Count==12:
        screen.blit(text6,SecondPosition)
        screen.blit(text5, SecondTop)

    elif InitialSetup.Count==2:
        text= font1.render("Light brown block is twice the breaking probability" ,True,RED)
        screen.blit(text, TopPosition)
        screen.blit(InsurSale, SecondTop)
        if InitialSetup.Count in InitialSetup.InsuranceList:
            if InitialSetup.InYn==True:
                screen.blit(InsBomp,SecondPosition)
            else:
                screen.blit(InsNoBomp,SecondPosition)



    elif InitialSetup.Press==True:
        screen.blit(InsurSale, TopPosition)
        if InitialSetup.Count in InitialSetup.InsuranceList:
            if InitialSetup.InYn==True:
                screen.blit(InsBomp,SecondPosition)
            else:
                screen.blit(InsNoBomp,SecondPosition)


    InitialSetup.moving_y -=InitialSetup.Fall


    pygame.display.flip()
##########################################################################################################
textinput = pygame_textinput.TextInput()

while not done:
    # --- Main event loop
    if Enter==1:
        money=InitialSetup.money
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [0,0,10000,7000])

    text4= font.render("End of the game. Thanks for the participation. Please confirm the following information",True,BLACK)
    text3= font1.render("Your ID number is "+nameID,True,RED)
    text5= font1.render("You won CHF"+str(money),True,RED)


    screen.blit(text4,HeadPosition)
    screen.blit(text3,TopPosition)
    screen.blit(text5, SecondTop)


    TommyFigure(screen,100,500,False)


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:

            done=True

    ###########For the text
    #text4= font.render("Please enter your name, and tell us that you have completed",True,BLACK)
    #screen.blit(text4,[100,400])

    #pygame.draw.line(screen, WHITE, [0,300], [7000,300], 50)
    #textinput.update(events)
    #name=textinput.get_text()
    #screen.blit(textinput.get_surface(), (50, 300))
    pygame.display.update()
    clock.tick(60)
    #screen.blit(text4,[50,200])
conn=sqlite3.connect('tempdb.sqlite')
cur=conn.cursor() #handle
Insurance=str(InitialSetup.InsuranceList)
try:
    cur.execute('''CREATE TABLE Users2 (ID Text, ResultMoney numeric, Insurance, text )''')
except:
    a=0
    cur.execute('''insert into Users2 (ID,ResultMoney,Insurance) values (?,?,?)''',(nameID,money,Insurance))


conn.commit()
