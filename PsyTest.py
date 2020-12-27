import time
import random

print("Try to influence the direction of the X on this line")
print("----------X----------")
time.sleep(0.4)
direction = input("Type 'positive' for right or 'negative' for left\n")
direction.lower()
while direction !='positive' or direction !='negative': 
    if direction == 'positive':
        print()
        break
    elif direction == 'negative':
        print()
        break
    else:
        print("Try to influence the outcome of random numbers.")
        time.sleep(0.4)
        direction = input("Type 'positive' or 'negative'\n")

time.sleep(0.2)
print ("You chose", direction)
time.sleep(1)
print ("Visualize your", direction, "energy.")
time.sleep(1)
print ("Get Ready!")
time.sleep(0.5)
print("3") 
time.sleep(1)
print("2") 
time.sleep(1)
print("1")
time.sleep(1)
print("Go")

position = 10
line = '-'*21

def adjustLine(roll):
    time.sleep(0.3)
    global position
    global line    
    line = '-'*21
    line_list = list(line)
    position += roll
    line_list[ position] = 'X'
    line = "".join(line_list)
    return line

for x in range(10):
    print(adjustLine(1 if random.random() < 0.5 else -1))

time.sleep(0.4)
print("Calculating...")
time.sleep(1)
print("..")
time.sleep(1)
if direction == 'positive' and position > 10 or direction == 'negative' and position < 10:
    print("You did it!", "\nYour conscious efforts made the X move.")
else:
    print("Your psychic powers need improvement!")
    
