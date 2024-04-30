"""
Simple Calculator
"""
# Provide your solution here
def calculate(a:int, b:int, operator:str) -> int and int and str:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/" and b == 0:
        print("Division by 0 is not allowed.")
    elif operator == "/":
        return a / b
    else:
        print("Invalid operator!")

print(calculate(9, 6, "/"))


"""
Reverse Word
"""
# Provide your solution here

def reverse_word(name: str) -> str:
    return name[::-1].capitalize()
print(reverse_word("SaRaH"))

"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

