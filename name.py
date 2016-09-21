def add(num1, num2):
    final = num1 + num2
    return final

def sub(num1, num2):
    final = num1 - num2
    return final

def mult(num1, num2):
    final = num1 * num2
    return final

def div(num1, num2):
    final = num1 / num2
    return final

print("enter thine numbers")
n1 = int(input())
n2 = int(input())
print("what function do you want to use")
print("addition")
print("subtraction")
print("multiplication")
print("division")
answer = input()
if answer == "addition":
    print(add(n1, n2))
elif answer == "subtraction":
    print(sub(n1 ,n2))
elif answer == "multiplication":
    print(mult(n1, n2))
elif answer == "division":
    print(div(n1 ,n2))
else:
    print("not an option")
