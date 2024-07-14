with open("onepiece.txt",'r') as t:
    text=t.read()
l=list(text.split("Episode"))
for i in range(1,len(l)):
    print(i+1,len(l[i]))