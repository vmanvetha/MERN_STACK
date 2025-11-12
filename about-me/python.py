print('HELLO MANVETHA')
name = 'manvetha'
age = 18
print(f'MY NAME IS {name}, Iam {age} years old')
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
print('sum =', a + b)
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
print('sub =', a - b)
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
print('mul =', a * b)
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
print('divison=', a / b)
a = 5
b = 2
a,b = b,a
print(a)
print(b)
a = 25
if (a%2==0):
    print("even")
else:
    print("odd")
a = input('Enter something:')
print(type(a))
name  = 'manvetha'
age = 18
color = 'Blue'
print(f'MY NAME IS {name} Iam {age} years old, My fav Color is {color} and I want to become a cyber forensic anylast')
a = 10
b = 20
average = (a + b) / 2
print("Average:", average)
a = [1,5,8,9,25]
b = sum(a) / len(a)
print(b)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3
print("Average:", round(average, 2))
import statistics

data = [5, 10, 15, 20, 25]
average = statistics.mean(data)
print("Average using statistics:", average)

