def start(_list):
    for sentence in _list:
        check = []
        is_valid = True
        for char in sentence:
            if char == '(' or char == '[':
                check.append(char)
            elif char == ')' or char == ']':
                if not check:
                    is_valid = False
                    break
                last_open = check.pop()
                if (char == ')' and last_open != '(') or (char == ']' and last_open != '['):
                    is_valid = False
                    break
        if is_valid and not check:
            print("yes")
        else:
            print("no")
            
_list = []
while True:
    _str = input()
    if _str == '.':
        start(_list)
        break
    else:
        _list.append(_str)
