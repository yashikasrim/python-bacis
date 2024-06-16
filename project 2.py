for i in range(5):
    name=input("enter the name:")
    total=0
    for i in range(5):
        mark=int(input("enter the mark"))
        total+=mark
    print("the total mark of the student",name ,"is:",total)