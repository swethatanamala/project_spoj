def wordbreak(string, dictionary):
    print("super", string)
    n = len(string)
    if n == 0:
        return True
    for i in range(1, n + 1):
        print(string[:i], string[i:])
        if string[:i] in dictionary and wordbreak(string[i:], dictionary):
            return True
    return False

temp_dict = ["i", "like", "sam", "sung", "samsung",
             "mobile", "ice", "cream", "icecream",
             "man", "go", "mango"]

string = "ilikesamsung"
print(wordbreak(string, temp_dict))
