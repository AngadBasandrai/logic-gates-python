from os import system

def save(a):
    func = ""
    dispname = input("Name of the chip: ")
    name = input("Name of the function for the chip: ")
    if name == "back":
        return
    func += "def "
    func += name
    func += "("

    vals = a.count("a0")
    if vals >= 1:
        vals = 1    
    bvals = a.count("a1")
    if bvals >=1:
        vals += 1

    for i in range(vals - 1):
        func += "i"
        func += str(i)
        func += ", "

    func += "i"
    func += str(vals - 1)
    func += "):\n\treturn "

    func += "\n\n"
    f = open("logicgates.py", "a")
    f.write(func)
    f.close()
    f2 = open("disp.txt", "a")
    f2.write(dispname + " --> " + name + "(")
    for i in range(vals - 1):
        f2.write("i" + str(i) + ",")
    f2.write("i" + str(vals - 1))
    f2.write(")\n\n")
    f2.close()

while True:
    from logicgates import *
    system("cls")
    with open('disp.txt', 'r') as f:
        print(f.read())
    x = input("Function: ")
    try:
        px = x.replace("a0", "True")
        px = px.replace("a1", "False")
        r = eval(px)
    except:
        raise Exception("Invalid Function!")

    print(x + " = " + str(r))
    y = input("Save(Y/N)?")
    y = y.lower()
    if y == "y":
        save(x)
    elif y == "n":
        pass
    else:
        raise Exception("Invalid Input!")
    z = input("Continue(Y/N)?")
    if z == "y":
        pass
    elif z == "n":
        quit()
    else:
        raise Exception("Invalid Input!")