import matplotlib.pyplot as plt
import numpy as np

#수직 막대그래프
# x = np.arange(3)
# years = ['2022', '2023', '2024']
# values = [100,300,600]
#
# plt.bar(x,values,color='red')
# plt.xticks(x,years)
# plt.show()

#수평 막대그래프
# y=np.arange(3)
# years = ['22','23','24']
# values = [100,800,2200]
# plt.barh(y,values)
# plt.yticks(y,years)
# plt.show()

#기본 산점도 그래프
# np.random.seed(0)
# n = 50
# x = np.random.rand(n)
# y = np.random.rand(n)
# plt.scatter(x,y)
# plt.show()

#산점도 옵션 지정
# np.random.seed(0)
# n = 50
# x = np.random.rand(n)
# y = np.random.rand(n)
# area = (30*np.random.rand(n))**2
# colors = np.random.rand(n)
#
# plt.scatter(x,y,s=area,c=colors,alpha=0.5,cmap='Spectral')
# plt.colorbar()
# plt.show()

#히스토그램
# weight=[68,81,64,56,78,74,61,77,66,68,59,71,80,59,59,67,81,69,73,69,74,70,65]
# plt.hist(weight)
# plt.show()

#파이차트
# ratio = [34,32,16,18] # 총 100
# labels = ["AA","BB","CC","DD"]
# explode=[0,0.10,0,0.10]
# colors=['silver', 'silver', 'silver', 'gold']
# plt.pie(ratio,labels=labels,autopct='%.1f%%', startangle=10, explode=explode,shadow=True, colors=colors) #%를 사용하려면 %%로 사용해야 % 하나만 나온다. startangle은 시작 각도임.
# plt.show()

#히트맵
# arr = np.random.standard_normal((30,40))
# plt.matshow(arr)
# plt.colorbar()
# plt.show()

x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
#50개 균일간격 값 얻음 : linspace
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
#2행 1열 중 첫번째 배치
plt.plot(x1,y1,'o-') #o-는 나오는 마커의 형태
plt.title('title111')
plt.ylabel('testlabel')
plt.grid(True)
plt.subplot(2,1,2)
#2행 1열 두번째 위치에 배치
plt.plot(x2,y2,'.-')
plt.title('title2222') #그래프 제목
plt.xlabel('time')
plt.ylabel('2ylabel') #y축 레이블 명
plt.tight_layout()
#두개 겹치지 않게 레이아웃 처리

plt.show()
