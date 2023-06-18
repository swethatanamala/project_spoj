def decode(inp_str, hardcoded_dict):
    count = [0 for i in range(len(inp_str) + 1)]
    count[0] = 1
    count[1] = 1
    for i in range(2, len(inp_str) + 1):
        if int(inp_str[i - 1]) != 0:
            count[i] = count[i - 1]
            temp_str =  inp_str[i - 2] + inp_str[i - 1]
            if temp_str in hardcoded_dict:
                count[i] = count[i] + count[i - 2]
        else:
            count[i] = count[i - 2]
    return count[-1]

while True:
    input_str = input()
    if input_str.strip() == '0':
        break
    else:
        hardcoded_dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G',
                        '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N',
                        '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U',
                        '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
        count = decode(input_str, hardcoded_dict)
        print(count)
        
