import json
from matplotlib import pyplot as plt
import requests
#data=json.load(open('/home/sameer/data.json'))
#data1=json.load(open('/home/sameer/latest-rates.json'))
sd='2019-01-01'
ed='2019-01-31'
u='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(sd,ed)
u1='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'

resp=requests.get(u)
f=resp.text
data=json.loads(f)

resp2=requests.get(u1)
f1=resp2.text
lr=json.loads(f1)


dates=[]
rupees=[]
gbp=[]

x=0 
for i in data['rates']:
    dates.append(i)
    rupees.append(data['rates'][i]['INR'])
    gbp.append(data['rates'][i]['GBP'])
    x+=1


md=list(zip(dates,rupees,gbp))
result = sorted(md, key = lambda x: x[0])

dates.clear()
rupees.clear()
gbp.clear()

dates,rupees,gbp = zip(*result)

a=max(rupees)
b=max(gbp)
y=max(a,b)


plt.xlabel('Datewise Currency Exchange jan 2019')
plt.ylabel('Exchange Rate')
plt.title('INR and GBP  exchange by 1 Euro and data taken by given website')
plt.plot(dates,rupees,label="INR")
plt.plot(dates,rupees,'ro')
plt.plot(dates,gbp,label="GBP")
plt.plot(dates,gbp,'ro')
plt.annotate('Current rate of INR:'+str(lr['rates']['INR']),(x-5,y),textcoords='offset points',xytext=(0,40),ha='center')
plt.annotate('Current rate of GBP:'+str(lr['rates']['GBP']),(x-5,y),textcoords='offset points',xytext=(0,30),ha='center')
plt.xticks(rotation=30)
plt.legend()
plt.show()


    






        
                
