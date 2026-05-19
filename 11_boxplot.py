import matplotlib.pyplot as plt 

division_a = [41, 44, 47, 49, 52, 53, 55, 57, 58, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 70]
division_b = [50, 51, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 71, 72, 74, 75, 77, 78, 79]
division_c = [61, 62, 64, 65, 67, 69, 70, 72, 73, 75, 77, 78, 80, 81, 83, 85, 86, 88, 89, 90]
division_d = [80, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 100]

plt.figure(figsize=(12,10))
plt.boxplot(x=[division_a,division_b,division_c,division_d],tick_labels=['A','B','C','D'])
# plt.xticks(ticks=['A','B','C','D'])
plt.xlabel('Division')
plt.ylabel('Marks')
plt.title("Box plot chart")
plt.grid()
plt.legend()
plt.show()
