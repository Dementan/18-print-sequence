#print line by line and in one line the sequence in which the user sets the beginning, end and step

a = int(input("Enter the beginning of the sequence: "))
b = int(input("Enter the end of the sequence: "))
c = int(input("Enter the step of the sequence: "))
for i in range(a, b + 1, c):
    print(i)        #line by line
for i in range(a, b + 1, c):
    print(i, end=" ")    #in one line
