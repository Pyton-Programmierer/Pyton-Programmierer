# ganz einfach den Zufallsgenerator von Python benutzt
import random
for i in range(15):
    print(random.randint(1,6)) 
 
def wuerfeln():
    return(random.randint(1,6))
wuerfeln()