# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    square = ""
    x = 1 

    while x <= n:
        if x == 1 or x == n:
            square += ("*" * n + "\n")
        else:
            square += ("*" + (" " * (n - 2)) + "*" + "\n")
        x += 1

    return (square.strip())

# 1
# 12
# 123
# 1234
def number_pattern(n):
    pattern = ""
    x = 1

    while x <= n:
        i = 1
        while i <= x:
            pattern += str(i)
            i += 1
        pattern += "\n"
        x += 1
         
    return (pattern.strip())

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0

    for i in range(n + 1):
        result += i
    
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n - i - 1):
            result += " "
        for k in range(2 * i + 1):
            result += "*"

        result += "\n"

    return result.rstrip()

