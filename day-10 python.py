def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("anele", "nenngwekhulu")
print(formatted_string)


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else :
                return False
        else:
             return True
    else:
        return False

print(is_leap_year(1989))

print("""
  _________________________
 |  _____________________  |
 | |                     | |
 | |       1234.56       | |
 | |_____________________| |
 |  ___ ___ ___   ___ ___  |
 | | 7 | 8 | 9 | | + | C | |
 | |___|___|___| |___|___| |
 | | 4 | 5 | 6 | | - | % | |
 | |___|___|___| |___|___| |
 | | 1 | 2 | 3 | | x | √ | |
 | |___|___|___| |___|___| |
 | | 0 | . | = | | ÷ | ^ | |
 | |___|___|___| |___|___| |
 |_________________________|
""")

def calculator(num1, operator, num2):
    num1 = int(input("What's the first number? "))
    operations = "*\n-\n+\n/\n"
    print(operations)
    operator = input("Pick an operation: ")
    num2 = int(input("What's the next number? "))

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "You are missing inputs"



    calculation = True
    while calculation:
        contin = input("Type 'y' to continue calculating with number , or type 'n' to start new calculation:")
        if contin == 'y':
            calculator()
        elif contin == 'n':
            calculation = False
    return "done"


print(calculator(1,"+",2))