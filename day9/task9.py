from collections import Counter
import copy

#  Mutable 
print("Mutable Example")

list1 = [10, 20, 30]
list2 = list1

print("Before Change")
print("list1:", list1)
print("list2:", list2)

list2.append(40)

print("\nAfter Change")
print("list1:", list1)
print("list2:", list2)

print("Memory Address of list1:", id(list1))
print("Memory Address of list2:", id(list2))


#  Immutable 
print("\n Immutable Example")

num1 = 100
num2 = num1

print("Before Change")
print("num1:", num1)
print("num2:", num2)

num2 = 200

print("\nAfter Change")
print("num1:", num1)
print("num2:", num2)

print("Memory Address of num1:", id(num1))
print("Memory Address of num2:", id(num2))


#  Copy 
print("\n Copy Example ")

original = [1, 2, 3]

shallow = original.copy()
deep = copy.deepcopy(original)

original.append(4)

print("Original :", original)
print("Shallow Copy :", shallow)
print("Deep Copy :", deep)


# Collections Module 
print("\n Collections Counter")

skills = ["Python", "Java", "Python", "C", "Python", "Java"]

count = Counter(skills)

print(count)


#  pip and venv 

print("\n pip and venv")

print("pip is used to install Python packages.")
print("Example: pip install numpy")

print("venv is used to create a virtual environment.")
print("Example:")
print("python -m venv myenv")