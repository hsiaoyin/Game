def TommyFigure(screen,moving_x,moving_y,Press):
    pygame.draw.ellipse(screen,BLACK,[15+moving_x,15+moving_y,50,50])
    #Body
    pygame.draw.rect(screen,RED,[15+moving_x,65+moving_y,50,100])
    #Arm
    pygame.draw.line(screen, BLACK, [15+moving_x,105+moving_y], [moving_x,5+moving_y], 10)
    pygame.draw.line(screen, BLACK, [65+moving_x,105+moving_y], [70+moving_x,5+moving_y],10)
    #leg
    pygame.draw.line(screen, BLACK, [25+moving_x,165+moving_y], [10+moving_x,200+moving_y], 10)
    pygame.draw.line(screen, BLACK, [55+moving_x,165+moving_y], [60+moving_x,200+moving_y], 10)
    pygame.draw.ellipse(screen,MONEY_C,[+moving_x,+moving_y,80,20])

def Introduction(Case):
    if Case==1:
        a=RuleText
    else:
        a=IntroText
    return(a)

def Background():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,230+space], [1000,230+space], 5)
    pygame.draw.line(screen, BLACK, [0,370+space], [1000,370+space], 5)
    pygame.draw.rect(screen, GREEN, [0,0,40,7000])
    pygame.draw.rect(screen, GREEN, [900,0,1000,7000])

    for i in range(11):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)



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
HeadPosition=[20,30]
SecondPosition=[50,700]
SecondTop=[50,140]
TopPosition=[50, 80]
BotPosition=[500,850]
FallSpeed=-30
pygame.display.set_caption("Tommy Crossing Bridge")
font = pygame.font.SysFont('Calibri', 25, True, False)
Space1=350
Space2=Space1-150

#Parameter for insurance
OrigwInsurance=12
OrigProb=0.05
Prob=OrigProb/12
Times=5
Prob2=Prob*Times
OrigMoney=20
money=OrigMoney
Premium=2

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
TommyMoney="Now Tommy has CHF"
BuyInsurance=". To buy for the next one, press Up"
InsurSale="One block costs CHF"
InsurSale= font.render(InsurSale+str(Premium)+BuyInsurance,True,RED)
BompText="No!!!... Bomp...You lose all the money!!"
BompText= font.render(BompText,True,RED)
FinText="Success! Congrats that Tommy has managed to bring you CHF"
RuleText=\
" Tommy needs to cross to bridge with your CHF20 \n \
There is "+str(100*OrigProb)+"% probability that the bridge may break.\n \
If the bridge breaks, Tommy will fall down and you will lose all the money.\n \
Each dark-brown block has the same probability to break\n \
Moreover, the light-brown block has " +str(Times)+" times the chance to break.\n \
You can choose to buy an insurance for CHF"+str(Premium*4)+" for the whole bridge. \n \
You will then get CHF12 for certain.\n \
Otherwise, you can buy insurance for each block (CHF"+str(Premium)+" per block)\n \
Press DOWN to continue"
RuleText=RuleText.splitlines()

IntroText=\
" Press Up if you prefer an insurance. \n \
Otherwise press the Right. \n\
(You can buy insurance per block on the way)!"
IntroText=IntroText.splitlines()

TommyText="Tommy is going to bring you the money"
TommyBridge="Tommy is going to bring you the money but the bridge may fall with 5% probability"
TommyText= font.render(TommyText,True,BLACK)
TommyBridge=font.render(TommyBridge,True,BLACK)
Practice="Practice Demo-- Please follow the step:"
Practice= font.render(Practice,True,InsBridge_C)
InsNoBomp= font.render("The block is safe but you are insured anyway" ,True,RED)
InsBomp= font.render("The block is broken but luckily you are insured" ,True,RED)

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

    screen.blit(TommyText,HeadPosition)
    tempText=Introduction(Case)
    for i in range(len(tempText)):
        text7= font.render(tempText[i],True,RED)
        screen.blit(text7, [150, space-250+i*40])

    #screen.blit()
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)
#####################################################Practice Demo#############
space=Space2
while not done1:
    # --- Main event loop
    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done1 = True
            done2= True
            done=True


    # User pressed down on a key

        # Figure out if it was an arrow key. If so
        # adjust speed.
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_RIGHT and (Count==0 or Buy==1 or Count==3):
                moving_x=moving_x+Speed
                Press=True
                Count=Count+1
                print(Count)
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

                Buy=0


                #elif event.key == pygame.K_LEFT:
                #    moving_x=moving_x-Speed

            elif event.key == pygame.K_UP and (Count==1 or Count==2):
                Buy=1
                money=money-Premium
                InsuranceList.append(Count+1)

            elif event.key ==pygame.K_DOWN and Count==4:
                done1=True

            elif event.key==pygame.K_9:
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
#Text
    text4= font.render(TommyMoney+str(money),True,BLACK)

    #text6= font.render(FinText+str(money),True,RED)
    extrainfo=""

    screen.blit(TommyBridge,HeadPosition)
    screen.blit(text4, BotPosition)
#Draw Bridge

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)

    TommyFigure(screen,moving_x,moving_y+space-100,Press)

    pygame.draw.line(screen, InsBridge_C, [0,200], [1000,200], 3)
    moving_y -=Fall

    extrainfo="Crossing while the block is safe, Press Right:"
    extrainfo1=""
    if Count==1:
        Bomp=False
        #screen.blit(InsurSale, SecondPosition)
        extrainfo="Next: You are insured while the block is safe"
        extrainfo1="Press Up to insure and Right to continue:"

    elif Count==2:
        screen.blit(InsNoBomp,SecondPosition)
        extrainfo="Next: You are insured while the block is broken"
        extrainfo1="press Up to insure and Right to continue:"

    elif Count==3:
        Bomp=True
        screen.blit(InsBomp,SecondPosition)
        extrainfo="Next: Crossing while the block is broken, Press Right:"

        #screen.blit(BuyInsurance, [50, 500])
        #screen.blit(InsurSale, [200,550])

    elif Count==4:
        Bomp=False
        screen.blit(BompText, SecondPosition)
        extrainfo="End of Demo, Press down to continue"
        extrainfo1="Or press 9 to replay the demo again"

    text8= font.render(extrainfo,True,RED)
    text9= font.render(extrainfo1,True,RED)
# Put the image of the text on the screen at 250x250

    screen.blit(Practice, TopPosition)
    screen.blit(text8,[50,130])
    screen.blit(text9,[50,160])
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
            if event.key == pygame.K_RIGHT and Count<11:
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

    text4= font.render(TommyMoney+str(money),True,BLACK)
    text6= font.render(FinText+str(money)+"! Press Down to continue",True,RED)

    screen.blit(TommyBridge,[10, 10])
    screen.blit(text4, [500,650])

# Put the image of the text on the screen at 250x250
#Draw Bridge
    for i in range(11):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [50+i*Speed,400+space], [80+i*Speed,200+space], 60)

    TommyFigure(screen,moving_x,moving_y+space-100,Press)


    if Bomp==True:
        screen.blit(BompText, SecondPosition)

    elif Count==11:
        screen.blit(text6,SecondPosition)


    elif Count==2:
        text= font.render("Light brown block is twice the breaking probability. Getting insured?",True,RED)
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


    moving_x=250

    TommyFigure(screen,moving_x,moving_y+space-100,Press)
    moving_y=250

    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #    done = True

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(60)
















pygame.quit()
