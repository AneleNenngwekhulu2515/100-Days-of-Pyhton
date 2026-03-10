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
