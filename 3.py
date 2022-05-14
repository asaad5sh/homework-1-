imfile =open ("r.txt",'r')
question= [x.rstrip()for x in imfile]

l=0
for i in question:
    print(i [:i.index("=")+1])
    
    p=input('enter the  answer')
    if p==i[i.index("=")+1]:
     l+=1
     
name=input ('enter your name pleas:')
print(name,l)
