import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
#
###ZESTAW 1

# #zad1
#
# wartosc = [100, 70, 75, 25, 50]
# wartosc2 = [20, 10, 35, 10, 50]
# arument = (0 ,1, 2, 3, 4)
#
# fig, ax= plt.subplots(figsize=(7,5))
#
# x = np.array([120,120,120,120,120,120])
# ax.plot(x)
# ax.bar(arument, wartosc, color = ['teal','darkgreen','khaki','pink',])
# ax.bar(arument, wartosc2, color = ['darkorchid','lightblue','olive','deepskyblue','lime'])
# ax.set(xticks=np.arange(0,6,1),
#       yticks= np.arange(0,141,20))
# ax.set_title('tytuł')
#
# plt.savefig('wykres.pdf')
# plt.show()
#
# #zad2
#
# xlsx = pd.ExcelFile('mieszkania1.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# dane = df.pivot(index='Formy budownictwa', columns='Rok', values='Wartość')
# dane.plot(kind='bar', figsize=(10,8), width=0.9)
# plt.text(0, 68000 , '167555',verticalalignment='baseline',horizontalalignment='right')
# plt.annotate('mój index', xy=(0,68000), xytext=(0,69000))
# plt.title("Ceny mieszkań w zależności od formy budownictwa")
# plt.grid(True)
# plt.show()

##ZESTAW 2

# fig, (ax) = plt.subplots(figsize=(8,5))
# x = np.arange(-6.5,7,0.1)
# y= 20*np.sin(x)
# y1=(2*x/5)-2
# y2=7-x
# ax.plot(x, y, 'r--',x,y1,'y--',x,y2,'g-')
# ax.set(xticks=np.arange(-6,7, 2),
#        yticks=np.arange(-30,31,10))
# ax.legend(labels=['y=20*sin(x)', 'y=(2x/5)-2','y=7-x'], loc='lower left')
# ax.set_title('Tytuł ABCD')
# # plt.show()

# data = pd.ExcelFile('mieszkania2.xlsx')
# df = pd.read_excel(data)
# seria= df[df['Rok']==2015].drop('Zakres przedmiotowy',axis=1)
#
# fig, ax = plt.subplots(figsize=(10,5))
#
# ax.pie(seria['Wartość'],labels=seria['Wartość'],
#        wedgeprops={'edgecolor':'black'})
#
# ax.legend(seria['Formy budownictwa'])
# ax.set_title("Wartość mieszkań w zależności od formy budownictwa w 2015 roku")
# plt.show()

##ZESTAW 3

#zad 1

miesiace=['Styczeń','Luty', 'Marzec', 'Kwiecień','Maj','Czerwiec']
gry = [22,32,42,77,66,50]
filmy=[50,41,39,21,22,25]

fig, ax = plt.subplots(figsize=(7,5))
ax.plot(miesiace,gry,'g-')
ax.plot(miesiace,filmy,'b--')
ax.set(yticks=np.arange(0,101,20), xlabel='Miesiąc',ylabel='Zyski',
       title='Zyski z filmów i gier')
ax.legend(labels=['Gry','Filmy'],loc='upper left')
ax.grid()
plt.show()
plt.savefig('wykres11.pdf')
##zad 2

xlsx = pd.ExcelFile('lasy11.xlsx')
df=pd.read_excel(xlsx)
seria = df[['Rok','Wartość']]

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(seria['Rok'],seria['Wartość'],width=1,color='green',edgecolor='white')
ax.set(yticks=np.arange(0,2500001,150000),xlabel='Lata',
       ylabel='Grunty leśne w mln. Ha', title='Zmiany powierzchni gruntów leśnych w latach 2015-2020')
ax.yaxis.grid()

ax.text(2015, 2250000,'167555',verticalalignment='baseline',horizontalalignment='right')
plt.show()