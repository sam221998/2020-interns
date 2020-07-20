import json
from matplotlib import pyplot as plt
data=json.load(open('/home/sameer/data.json'))
d={}
d1=1
dates=[]
rupees=[]
gbp=[]
while d1<10:
    for k,v in data.items():
        for k1 in v:
            if k1=='2019-01-0'+str(d1):
                dates.append(k1)
                d=v[k1]
                for (k2,v2) in d.items():
                    if k2=="INR":
                            rupees.append(v2)
                    if k2=="GBP":
                        gbp.append(v2)

    d1+=1


while d1<32:
    for p_id, p_info in data.items():
        for key in p_info:
            if key=='2019-01-'+str(d1):
                dates.append(key)
                d=p_info[key]
                for (k,v) in d.items():
                    if k=="INR":
                        rupees.append(v)
                    if k=="GBP":
                        gbp.append(v)

    d1+=1
      

date1=[]
for x in dates:
    a=x.split('-')
    y=a[0]
    m=a[1]
    dates=a[2]
    date1.append(int(dates))

x=date1
y=rupees
z=gbp
plt.xlabel('Datewise Currency Exchange jan 2019')
plt.ylabel('Exchange Rate')
plt.title('INR and GBP ALSO exchange by 1 Euro')
plt.plot(x,y,label="INR")
plt.plot(x,y,'ro')
plt.plot(x,z,label="GBP")
plt.plot(x,z,'ro')
plt.legend()
plt.show()


    






        
                
