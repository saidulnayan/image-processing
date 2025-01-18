data = open("input","r")
data = data.read()       # input value
data = data.split()

sata = open("data","r")
sata = sata.read()

dec=[]    # unicode value
ans=[]      # compressed value
back=[]       # decompressed value
out=[]          # output value

n=len(data)

print("Input value:\t",data)

for i in range(0,n):
    dec.append(ord(data[i]))

print("Unicode value:\t",dec)

ans.insert(0,dec[0])
for j in range(1,n):
    ans.insert(j,dec[j]-dec[j-1])

print("Compressed value:\t",ans)

back.append(ans[0])
for k in range(1,n):
    back.append(back[k-1]+ans[k])

print("Decompressed value:\t",back)

for h in range(0,n):
    out.append(chr(back[h]))

print("Output value:\t",out)

with open("output","w") as file:
    for item in out:
        file.write('%s\n' % item)

print("\n\n",sata)


