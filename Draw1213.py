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
    pygame.draw.line(screen, BLACK, [0,230+space], [1000,230+space], 5)
    pygame.draw.line(screen, BLACK, [0,370+space], [1000,370+space], 5)
    pygame.draw.rect(screen, GREEN, [0,0,90,7000])
    pygame.draw.rect(screen, GREEN, [1050,0,7000,7000])

    for i in range(13):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)


import json
import pygame_textinput
import pygame
import random
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
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
moving_x=18
moving_y=250
Speed=80
Fall=0
Press=False
Bomp=False
Count=0
HeadPosition=[100,30]
SecondPosition=[130,800]
SecondTop=[130,140]
TopPosition=[130, 80]
BotPosition=[1100,250]
FallSpeed=-30
pygame.display.set_caption("Tommy Crossing Bridge")
font = pygame.font.SysFont('Calibri', 25, True, False)
font1 = pygame.font.SysFont('Calibri', 50, True, False)
Space1=500
Space2=Space1-150

#Parameter for insurance
OrigwInsurance=12
OrigProb=0.05
Times=5
Prob=OrigProb/(OrigwInsurance+Times)
Prob2=Prob*Times
OrigMoney=20
money=OrigMoney
Premium=1.5
WinsP=12.5

#To begin
x=0
Buy=0
InsuranceList=list()
done0=False
done1=False
done2=False
done=False
InYN=False
done = False


#Words
TommyMoney="When Tommy arrives, you will get "
TommyMoney=font.render(TommyMoney,True,BLACK)
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
that it may break. The third block is rotten. \n\
Non-rotten blocks have equal breaking probability\n\
while the rotten block has "+str(Times)+" times more likely to break than the rest \
individual blocks. \n\
If the bridge breaks, Tommy will fall and you lose all your money. \n\
You can pay CHF " +str(OrigMoney-WinsP)+ " for insurance protecting Tommy from falling.\n\
In this case, you will get paid CHF "+str(WinsP)+". \n\
This insurance per block costs CHF "+str(Premium)+". \n\
If you want to take the risk, \n\
you can still buy individual block insurance separately when Tommy is on the bridge.\n\
Press DOWN to continue"
BackText="You can check on the right side the money you will earn when Tommy crosses the bridge"

#
RuleText=RuleText.splitlines()

IntroText=\
" Press UP if you prefer an insurance. (In this case, you will get paid CHF "+str(WinsP)+"!) \n \
Otherwise press the RIGHT. \n\
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

# Used to manage how fast the screen updates




Case=1
# -------- Main Program Loop -----------
# Loop until the user clicks the close button.

space=Space1

while not done0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done0= True
            done1 = True
            done2= True
            done=True
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
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

    TommyFigure(screen,moving_x,moving_y+space-100,Press)
    #screen.blit(TommyBridge,HeadPosition)

    tempText=Introduction(Case)
    for i in range(len(tempText)):
        text7= font.render(tempText[i],True,DarkRed)
        screen.blit(text7, [150, space-400+i*40])

    #screen.blit()
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)
#####################################################Practice Demo#############
space=Space2
result=0
while not done1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done1 = True
            done2= True
            done=True


        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_RIGHT and (Count==0 or Buy==1 or Count==3):# or result==0):
                print(Count,Buy,result)
                if result==0:
                    result=1

                    Buy=0
                else:
                    Count=Count+1
                    moving_x=moving_x+Speed
                    Press=True
                    result=0

                    if Count==4:
                        Bomp=True
                        Fall=FallSpeed
                        money=0

                    elif Count==2:
                        Bomp==False
                        InYN=True

                    elif Count==3:
                        Bomp=False
                        InYN=False





                #elif event.key == pygame.K_LEFT:
                #    moving_x=moving_x-Speed

            elif event.key == pygame.K_UP and (Count==1 or Count==2) and  Buy==0:
                Buy=1
                money=money-Premium
                InsuranceList.append(Count+1)
                result=1

            elif event.key ==pygame.K_DOWN and Count==4:
                done1=True

            elif event.key==pygame.K_LEFT and Count==4:
                moving_x=18
                moving_y=250
                Fall=0
                Press=False
                Bomp=False
                Count=0
                money=OrigMoney
                Buy=0
                InsuranceList=list()
                InYN=False


    Background()

    text4= font1.render(" CHF"+str(money),True,RED)

    #text6= font.render(FinText+str(money),True,RED)
    extrainfo=""
    screen.blit(TommyMoney, BotPosition)
    screen.blit(text4, [1100,300])
#Draw Bridge

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)

    TommyFigure(screen,moving_x,moving_y+space-100,Press)
    pygame.draw.line(screen, InsBridge_C, [0,200], [1000,200], 3)
    moving_y -=Fall

    extrainfo="Crossing without insurance "
    extrainfo1="Press RIGHT"


    if result==0:
        extrainfo=BackText
        extrainfo1="press RIGHT to continue:"#

    if Count==1:

        extrainfo="Next: to acquire individual insurance"
        extrainfo1="Press UP to get insured and RIGHT to continue:"

    elif Count==2:
        if result==0:
            screen.blit(InsNoBomp,SecondPosition)
        else:
            extrainfo="Next: You are insured while the block is broken"
            extrainfo1="press UP to get insured and RIGHT to continue:"

    elif Count==3:
        if result==0:
            Bomp=True
            screen.blit(InsBomp,SecondPosition)
        else:
            extrainfo="Next: Crossing while the block is broken"

        #screen.blit(BuyInsurance, [50, 500])
        #screen.blit(InsurSale, [200,550])

    elif Count==4:
        Bomp=False
        screen.blit(BompText, SecondPosition)
        extrainfo="End of Demo, Press DOWN to continue"
        extrainfo1="Or press LEFT to replay the demo again"

    text8= font.render(extrainfo,True,DarkRed)
    text9= font.render(extrainfo1,True,RED)
# Put the image of the text on the screen at 250x250

    screen.blit(Practice, TopPosition)
    screen.blit(text8,[100,130])
    screen.blit(text9,[100,160])
    #if moving_x+10>990:
    #    moving_x=590



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
moving_x=18
moving_y=250
Fall=0
Press=False
Bomp=False
Count=0
money=OrigMoney
Buy=0
InsuranceList=list()
InYN=False

#################FIRST Game##################Demo##################
while not done2:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done2 = True
            done=True
    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_RIGHT and Count<12:
                moving_x=moving_x+Speed
                Press=True
                Count=Count+1
                x=random.random()

                if Count==3:
                    Bomp=x<Prob2
                else:
                    Bomp=x<Prob

                if Buy==1:
                    if Bomp==True:
                        InYN=True
                    else:
                        InYN=False
                    Bomp=False
                    Buy=0

                print(x,Bomp,Prob,Count,InsuranceList,Buy)
                if Bomp==True:
                    Fall=FallSpeed
                    money=0
            #elif event.key == pygame.K_LEFT:
            #    moving_x=moving_x-Speed

            elif event.key == pygame.K_UP and Count<11:
                Buy=1
                money=money-Premium
                InsuranceList.append(Count+1)

            elif event.key ==pygame.K_DOWN and Count>=11:
                done2=True


    Background()







    text4= font1.render(" CHF"+str(money),True,RED)
    text6= font1.render(FinText+str(money)+"!" ,True,RED)
    text5= font1.render("Press DOWN to continue" ,True,BLACK)

    screen.blit(TommyMoney, BotPosition)

    screen.blit(text4, [1100,300])

# Put the image of the text on the screen at 250x250
#Draw Bridge

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)

    TommyFigure(screen,moving_x,moving_y+space-100,Press)


    if Bomp==True:
        screen.blit(BompText, SecondPosition)

    elif Count==12:
        screen.blit(text6,SecondPosition)
        screen.blit(text5, SecondTop)

    elif Count==2:
        text= font1.render("Light brown block is twice the breaking probability" ,True,RED)
        screen.blit(text, TopPosition)
        screen.blit(InsurSale, SecondTop)
        if Count in InsuranceList:
            if InYN==True:
                screen.blit(InsBomp,SecondPosition)
            else:
                screen.blit(InsNoBomp,SecondPosition)



    elif Press==True:
        screen.blit(InsurSale, TopPosition)
        if Count in InsuranceList:
            if InYN==True:
                screen.blit(InsBomp,SecondPosition)
            else:
                screen.blit(InsNoBomp,SecondPosition)


    moving_y -=Fall




    #if moving_x+10>990:
    #    moving_x=590


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


textinput = pygame_textinput.TextInput()
##########################################Confirmation page
while not done:
    # --- Main event loop
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [0,0,10000,7000])

    text4= font.render("Thanks for the participation!",True,BLACK)
    text5= font.render("You won CHF"+str(money),True,RED)

    screen.blit(text4,TopPosition)
    screen.blit(text5, SecondTop)


    moving_x=100

    TommyFigure(screen,moving_x,500,Press)


    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #    done = True

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame

    # Blit its surface onto the screen
    text4= font.render("Please enter your name, and tell us that you have completed",True,BLACK)
    screen.blit(text4,[100,400])

    pygame.draw.line(screen, WHITE, [0,300], [7000,300], 50)
    textinput.update(events)
    screen.blit(textinput.get_surface(), (50, 300))
    pygame.display.update()
    screen.blit(text4,[50,200])
    clock.tick(60)
















pygame.quit()
