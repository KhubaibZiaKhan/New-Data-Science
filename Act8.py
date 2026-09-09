import matplotlib.pyplot as plt

Height_of_mens=[5.9,5.10,6.0,6.2,6.3,6.4,6.5,6.6,6.7,6.8]
Height_of_womens=[5.3,5.2,5.6,5.7,5.8,5.9,5.10]

type = [Height_of_mens, Height_of_womens] 
colors=['g','b']

label=['Womens', 'Mens']

bins=[5.0, 5.5, 6.0, 6.5, 7.0]
plt.xlabel("Heights in mens")
plt.ylabel("Heights in womens")

plt.hist(type,bins, rwidth=1,color=colors,label=label,orientation='vertical')

plt.title("Heights of Mens And Womens")
plt.legend()
plt.show()
