string=input('enter a string :-')
i=0
while i<len(string):
    if not('A'<=string[i]<='Z'or'a'<=string[i]<='Z'or '0'<=string[i]<=9):
    out =out+('_')
else:
    out=out+string[i]
    i+=1
print(out)