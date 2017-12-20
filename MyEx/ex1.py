name=input("Give your name please ?  ")
print("Hello", name)

hour=input("How many hours have you worked? ")
rate=input("What is the per hour rate? ")

def computepay(x,y):
    try: x=float(hour)
    except:
        print("you are joking")
        x=0
    try: y=float(rate)
    except:
        y=0
    if x*y==0:
        print("you are kidding...")
    else: print("you earn",x*y)


def calculater():
    sum=0
    x=input("give me a number (till you type done)")
    while x!="done":
        print(x)
        try: x=float(x)
        except:
            x=0
            print("NUMBER!!")
        sum=x+sum
        x=input("give me a number? ")
    print(sum)

calculater()
