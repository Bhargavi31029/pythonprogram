a=eval(input('enter the word'))
i=0
count=0
while i<len(a):
    if a[i] in('0,9,8,7,6,5,4,3,2,1'):
        count+=1
        print(a[i])
    i+=1    

        
