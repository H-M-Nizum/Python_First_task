def subtract(num1, num2):
    if num1 >= num2:
        return num1 - num2
    return num2 - num1

if __name__ == "__main__":
    num1 = int(input('Enter your First number : '))
    num2 = int(input('Enter your Second number : '))
    ans = subtract(num1, num2)
    print('Subtraction of two numbers : ', ans)