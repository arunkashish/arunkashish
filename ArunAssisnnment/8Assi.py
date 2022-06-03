a=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
c=[]
for x in a:
    b=round(x)
    c.append(b)
print(c)
le=len(c)
f=0
for i in range(0,le):
    f=f+c[i]
print(f*le)