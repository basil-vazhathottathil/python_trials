def sum(a,b):
    return (a+b)

def diff(a,b):
    return a-b

def prod(a,b):
    return a*b

def div(a,b):
    if b==0:
        print ("not divisible")
    else:
        return a/b
    

operations={
    "+":sum,
    "-":diff,
    "*":prod,
    "/":div,
}

choice="y"
while choice=="y":
    a=int (input("enter a number : "))
    b=int (input("enter the second number : "))

    for symbol in operations:
        print(symbol)

    oper_sym=input("enter the operation ")

    calc=operations[oper_sym]

    calc(a,b)

    print (f"{a} {oper_sym} {b} = {calc(a,b)}")

    choice=input ("do you want to another calculation(y/n)").lower()