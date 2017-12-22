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
    pygame.draw.rect(screen, GREEN, [1150,0,7000,7000])

    for i in range(13):
        if i==3:
            pygame.draw.line(screen, GRAY_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)
        elif i==0:
            pygame.draw.line(screen, GREEN, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)
        else:
            pygame.draw.line(screen, BRIDGE_C, [100+i*Speed,400+space], [130+i*Speed,200+space], 60)

OrigwInsurance=12 #Number of block

class Setup():

    def __init__(self):
        self.moving_x=18
        self.moving_y=250
        self.Fall=0
        self.Press=False
        self.Bomp=False
        self.Count=0
        self.OrigMoney=OrigMoney
        self.money=OrigMoney
        self.Buy=0
        self.InsuranceList=list()
        self.InYN=False
