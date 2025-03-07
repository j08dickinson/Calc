import math

def calc(x,y):
    result = int(x) * int(y)
    return result
    
if __name__ == '__main__':
    num1 = input("Please provide 1st number:")
    num2 = input("Please provide 2nd number:")
    print(calc(num1, num2))
