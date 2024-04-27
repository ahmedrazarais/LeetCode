def evaluate_expression(s):
    # Remove whitespace from the input string
    s = s.replace(" ", "")

    # Initialize variables
    result_list = []
    num = 0
    sign = "+"

    # Iterate through the string
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if not char.isdigit() or i == len(s) - 1:
            if sign == "+":
                result_list.append(num)
            elif sign == "-":
                result_list.append(-num)
            elif sign == "*":
                result_list[-1] *= num
            elif sign == "/":
                # Check if it's integer division or regular division
                if result_list[-1] < 0:
                    result_list[-1] = -(-result_list[-1] // num)
                else:
                    result_list[-1] //= num
            sign = char
            num = 0

    # Sum up the values in the result_list to get the final result
    return sum(result_list)


s = "14-3/2"
print(evaluate_expression(s))  
