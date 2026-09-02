import matplotlib.pyplot as plt
x=[12,13,14,15,16,22,77,45,65]
y1=[10,20,30,40,50,60,70,80,90]
y2=[12,12,14,16,18,20,22,24,26]
plt.plot(x,y1,linestyle='dashed',marker='D')
plt.plot(x,y2,linestyle='dashed',marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('Velocity m/s')
plt.ylabel('Time(s)')
plt.xlim(5,25)
plt.legend()
plt.show()
