bill= open(r'bill.text','r')
# data=bill.readline()
data=bill.readlines()
bill.close()
del data[0]
isdduration = 0
custid = ''
stdcallduration = 0
stdcount = 0
isdcount = 0
freecount = 0
freecallduration = 0
for x in data:
    x=x.strip('\n')
    xx=x.split('#')
    # print(xx[3])
    custid=xx[0]
    calltype=xx[-1]
    # print(xx)
    if(calltype=="std"):
        stdcount +=1
        stdcallduration +=int(xx[3])
    elif (calltype == "isd"):
        isdcount += 1
        isdduration += int(xx[3])
    elif (calltype == "free"):
        freecount += 1
        freecallduration = 0
print("std call =",stdcount,stdcallduration)
print("isd call =",isdcount,isdduration)
print("free call =",freecount,freecallduration)
stdtotalmints=stdcallduration/60
stdtotalmintss=round(stdtotalmints)
# print("totalminutes:",stdtotalmintss)
totalprice=stdtotalmintss*2
print("stdtotalincome:",totalprice)
isdtotalmints=isdduration/60
isdtotalmintss=round(isdtotalmints)
# print("totalminutes:",stdtotalmintss)
isdtotalprice=isdtotalmintss*2
print("isdtotalincome:",isdtotalprice)













