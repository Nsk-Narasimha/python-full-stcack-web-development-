'''import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,12,3,41,5]
plt.plot(x,y)
plt.title("example")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
x=[2026,2025,2024,2023]
y=[40,70,50,40]
plt.plot(x,y)
plt.title("sales")
plt.xlabel("year")
plt.ylabel("count")
plt.show()
plt.bar(x,y,color='red',edgecolor='black')
plt.show()

import matplotlib.pyplot as plt

# Figure 1
plt.figure(1)
x = [1, 2, 3, 4, 5]
y = [1, 12, 3, 41, 5]
plt.plot(x, y)
plt.title("Example")
plt.xlabel("x")
plt.ylabel("y")

# Figure 2
plt.figure(2)
x = [2026, 2025, 2024, 2023]
y = [40, 70, 50, 40]
plt.plot(x, y)
plt.title("Sales")
plt.xlabel("Year")
plt.ylabel("Count")
plt.figure(5)
x = [2026, 2025, 2024, 2023]
y = [40, 70, 50, 40]
plt.scatter(x, y)
plt.title("Sales")
plt.xlabel("Year")
plt.ylabel("Count")
plt.figure(3)
sub=['python','java','c']
stu=[69,13,50]
plt.pie(stu,labels=sub,colors=['pink','purple','orange'],autopct='%1.1f%%')
plt.legend(sub)
plt.title('course')
plt.show()
# Show both figures together
plt.show()
'''
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C", "C++", "SQL"]
marks = [85, 78, 92, 74, 88]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(subjects, marks, marker='o')
plt.title("Line Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 2)
plt.bar(subjects, marks)
plt.title("Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 3)
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")

plt.subplot(2, 2, 4)
plt.scatter(subjects, marks)
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()

