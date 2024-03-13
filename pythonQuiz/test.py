"""
What is the output of this code ?
"""

#___1
# def calculate(num1, num2=4):
#  num2 = 4 means if no value provided then it will be 4
#    res = num1 * num2
#    print(res)

# calculate(5, 6)

# 30
#_____2
# for x in range(0.5, 5.5, 0.5):
#  print(x)

#you cant use range with floating numbers so the out come it Error

#we can use loop instead


 #x = 36 / 4 * (3 +  2) * 4 + 2
#print(x)

#182


#var = "James" * 2  * 3
# print(var)
# JamesJamesJamesJamesJamesJames

# str = "pynative"
# print (str[1:3])
#yn

# valueOne = 5 ** 2
# valueTwo = 5 ** 3

# print(valueOne)
# print(valueTwo)
#25 125


# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

#TypeError: set.add() takes exactly one argument (2 given)

# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)

#12000 , 8000 first the function then the global 

# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)

#true false



# var= "James Bond"
# print(var[2::-1])

# var[2::-1] is slicing the string var starting from index 2 (which is the letter "m") and going backwards by steps of -1, which means it will reverse the string from index 2 to the beginning of the string.

# p, q, r = 10, 20 ,30
# print(p, q, r)
#102030

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)
# TypeError: list.append() takes exactly one argument (2 given)



for i in range(10, 15, 1):
  print( i, end=', ')
