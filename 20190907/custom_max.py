def custom_max(input_list):
    output = input_list[0]

    for element in input_list :
        if output < element :
            output = element
    return output

print(custom_max([32, 32, 923, 2, 123]))