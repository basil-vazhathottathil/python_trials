print("sup ,this is a love calculator")
name1=input("what is your name  ")
name2=input("what is their name  ")

combine=name1+name2
lower_combine=combine.lower()

t= lower_combine.count("t")
r= lower_combine.count("r")
u= lower_combine.count("u")
e= lower_combine.count("e")

true= t+r+u+e

l= lower_combine.count("l")
o= lower_combine.count("o")
v= lower_combine.count("v")
e= lower_combine.count("e")

love = l+o+v+e

score=int(str(true)+str(love))

if (score<10) or (score>90):
    print(f"Your love score is {score}, you do together like coke and mentos")
elif (score>=40 and score<=50):
    print(f"Your love score is {score}, you are alright")
else:
    print (f"your love score is {score}")