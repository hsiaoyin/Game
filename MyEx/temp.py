RuleText=\
" Tommy needs to cross to bridge with your CHF20 \n \
There is 5: probability that the bridge may break.\n \
if the bridge breaks, Tommy will fall down and you will lose CHF.\n \
Each dark-brown block has a same probability to fall\n \
    while light-brown block has 2 times the chance to fall.\n \
You can choose to buy an insurance for CHF8 for the whole bridge. You will then get CHF12 for certain.\n \
Press b if you prefer an insurance. Otherwise press right key."



temp=RuleText.splitlines()
type(temp)

for i in range(len(temp)):
    print(temp[i])
