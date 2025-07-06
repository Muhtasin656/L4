tr=input("enter a word:")
char=input("enter a character:")
i=0
count=0
while(i<len(tr)):
    if(tr[i]==char):
        count=count+1
    i=i+1
print(f"number of time {char} has occured is {count} ")