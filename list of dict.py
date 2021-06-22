n=input('enter a string:')
words=n.split()
d={}
for i in words:
    ch=i[0]
    if ch not in d:
        d[ch]=[]
    else:
        d[ch].append(i)
print(d)        
for k,v in d.items():
    print(k ,':', v)
