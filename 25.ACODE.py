
def decode(inp, map, hardcoded_dict):
    if inp in map:
        return map[inp]
    else:
        if len(inp) > 1:
            map[inp] = decode(inp[1:], map, hardcoded_dict)
            if inp[:2] in hardcoded_dict:
                map[inp] += decode(inp[2:], map, hardcoded_dict)
        else:
            map[inp] = 1
        return map[inp]

while True:
    input_str = input()
    if input_str.strip() == '0':
        break
    if len(input_str.strip()) == 0:
        print(0)
    else:
        map = {}
        hardcoded_dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G',
                        '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N',
                        '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U',
                        '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
        total_decodes = decode(input_str, map, hardcoded_dict)
        print(total_decodes)
        
