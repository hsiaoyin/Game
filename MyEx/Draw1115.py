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




# Set the width and height of the screen [width, height]
size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tommy Crossing Bridge")
font = pygame.font.SysFont('Calibri', 25, True, False)

done = False
BuyInsurance="If you want to buy insurance for the next block, press B"
BuyInsurance= font.render(BuyInsurance,True,RED)
TommyMoney="Now Tommy has now CHF"
InsurSale="One block costs CHF"
BompText="No!!!... Bomp...You lose all the money!!"
BompText= font.render(BompText,True,RED)
FinText="Success! Congrats that Tommy has managed to bring you CHF"
RuleText=\
" Tommy needs to cross to bridge with your CHF20 \n \
There is 5% probability that the bridge may break.\n \
If the bridge breaks, Tommy will fall down and you will lose all the money.\n \
Each dark-brown block has the same probability to break\n \
Moreover, the light-brown block has 2 times the chance to break.\n \
You can choose to buy an insurance for CHF8 for the whole bridge. \n \
You will then get CHF12 for certain.\n \
Otherwise, you can buy insurance for each block (CHF2 per block)\n "
RuleText=RuleText.splitlines()

IntroText=\
" Press b if you prefer an insurance. \n \
Otherwise press the right key. (You can buy insurance per block on the way)!"
IntroText=IntroText.splitlines()

TommyText="Tommy is going to bring you the money!!"
TommyText= font.render(TommyText,True,BLACK)
Practice="Practice Demo-- "
InsNoBomp= font.render("The block is safe but you are insured anyway" ,True,RED)
InsBomp= font.render("The block is broken but luckily you are insured" ,True,RED)

# Used to manage how fast the screen updates

clock = pygame.time.Clock()
moving_x=18
moving_y=150
Speed=80
Fall=0
Press=False
Bomp=False
Prob=0.05/12
Prob2=Prob*2
Count=0
OrigMoney=20
money=OrigMoney
Premium=2
x=0
Buy=0
InsuranceList=list()
done0=False
done1=False
InYN=False






Case=1
# -------- Main Program Loop -----------
# Loop until the user clicks the close button.
while not done0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done0= True
            done1 = True

        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_RIGHT:
                done0=True
            elif event.key ==pygame.K_KP_ENTER:



    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,230+250], [1000,230+250], 5)
    pygame.draw.line(screen, BLACK, [0,370+250], [1000,370+250], 5)
    pygame.draw.rect(screen, GREEN, [0,0,40,700])
    pygame.draw.rect(screen, GREEN, [900,0,1000,700])


    #Draw Bridge
    for i in range(11):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [50+i*Speed,400+250], [80+i*Speed,200+250], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [50+i*Speed,400+250], [80+i*Speed,200+250], 60)


    TommyFigure(screen,moving_x,moving_y+250,Press)

    screen.blit(TommyText,[300, 0])

    tempText=Introduction(Case)
    for i in range(len(tempText)):
        text7= font.render(tempText[i],True,RED)
        screen.blit(text7, [150, 50+i*40])

    #screen.blit()
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)
#####################################################Practice Demo#############

while not done1:
    # --- Main event loop
    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done1 = True


    # User pressed down on a key

        # Figure out if it was an arrow key. If so
        # adjust speed.
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_RIGHT and (Count==0 or Buy==1 or Count>3):
                moving_x=moving_x+Speed
                Press=True
                Count=Count+1
                print(Count)
                if Count==3:
                    Bomp=True
                    Fall=-5

                elif Count==1:
                    Bomp==False
                    InYN=True
                elif Count==2:
                    Bomp=False
                    InYN=False

                Buy=0


                #elif event.key == pygame.K_LEFT:
                #    moving_x=moving_x-Speed

            elif event.key == pygame.K_b and (Count==1 or Count==2):
                Buy=1
                money=money-Premium
                InsuranceList.append(Count+1)


    # User let up on a key
        #elif event.type == pygame.KEYUP:


        # If it is an arrow key, reset vector back to zero
    #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #        x_speed = 0
    #    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #        y_speed = 0St
    # --- Game logic should go here

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,230], [1000,230], 5)
    pygame.draw.line(screen, BLACK, [0,370], [1000,370], 5)
    pygame.draw.rect(screen, GREEN, [0,0,40,700])
    pygame.draw.rect(screen, GREEN, [900,0,1000,700])
#Text
    text4= font.render(TommyMoney+str(money),True,RED)
    text5= font.render(InsurSale+str(Premium),True,RED)
    text6= font.render(FinText+str(money),True,RED)
    extrainfo=""

    screen.blit(TommyText,[300, 0])
    screen.blit(text4, [400,50])
#Draw Bridge
    for i in range(11):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [50+i*Speed,400], [80+i*Speed,200], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [50+i*Speed,400], [80+i*Speed,200], 60)

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [50+i*Speed,400], [80+i*Speed,200], 60)

    TommyFigure(screen,moving_x,moving_y,Press)

    moving_y -=Fall

    extrainfo=""
    if Count==1:
        Bomp=False
        extrainfo="Crossing while the block is safe"
        screen.blit(BuyInsurance, [50, 500])
        screen.blit(text5, [400,550])

    elif Count==2:
        extrainfo="You are insured while the block is broken, Press B"
        screen.blit(BuyInsurance, [50, 500])
        screen.blit(text5, [400,550])

    elif Count==3:
        Bomp=True
        extrainfo="You are insured while the block is safe, Press B"
        screen.blit(BuyInsurance, [50, 500])
        screen.blit(text5, [400,550])

    elif Count==4:
        Bomp=False
        screen.blit(BompText, [400, 500])
        extrainfo="Crossing while the block is broken, Press Right Key"


    text8= font.render(Practice+extrainfo,True,RED)

# Put the image of the text on the screen at 250x250

    screen.blit(text8, [50, 50])
    #if moving_x+10>990:
    #    moving_x=590



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

clock = pygame.time.Clock()
moving_x=18
moving_y=150
Speed=80
Fall=0
Press=False
Bomp=False
Prob=0.05/12
Prob2=Prob*2
Count=0
OrigMoney=20
money=OrigMoney
Premium=2
x=0
Buy=0
InsuranceList=list()
done0=False
done1=False
InYN=False
#################FIRST Game##################Demo##################
while not done1:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done1 = True

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
                    Fall=-5

            #elif event.key == pygame.K_LEFT:
            #    moving_x=moving_x-Speed

            elif event.key == pygame.K_b and Count<11:
                Buy=1
                money=money-Premium
                InsuranceList.append(Count+1)


    # User let up on a key
        #elif event.type == pygame.KEYUP:


        # If it is an arrow key, reset vector back to zero
    #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #        x_speed = 0
    #    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #        y_speed = 0St
    # --- Game logic should go here


    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0,230], [1000,230], 5)
    pygame.draw.line(screen, BLACK, [0,370], [1000,370], 5)
    pygame.draw.rect(screen, GREEN, [0,0,40,700])
    pygame.draw.rect(screen, GREEN, [900,0,1000,700])
#Text
    text4= font.render(TommyMoney+str(money),True,RED)
    text5= font.render(InsurSale+str(Premium),True,RED)
    text6= font.render(FinText+str(money),True,RED)

# Put the image of the text on the screen at 250x250
    screen.blit(TommyText,[300, 0])
    screen.blit(text4, [400,50])
#Draw Bridge
    for i in range(11):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [50+i*Speed,400], [80+i*Speed,200], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [50+i*Speed,400], [80+i*Speed,200], 60)

    for i in InsuranceList:
        pygame.draw.line(screen, InsBridge_C, [50+i*Speed,400], [80+i*Speed,200], 60)

    TommyFigure(screen,moving_x,moving_y,Press)


    if Bomp==True:
        screen.blit(BompText, [400, 500])

    elif Count==11:
        screen.blit(text6, [50, 500])

    elif Count in InsuranceList:
        if InYN==True:
            screen.blit(text9, [50, 500])
        else:
            screen.blit(text9, [50, 500])
    elif Press==True:
        screen.blit(BuyInsurance, [50, 500])
        screen.blit(text5, [400,550])



    moving_y -=Fall




    #if moving_x+10>990:
    #    moving_x=590


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()
