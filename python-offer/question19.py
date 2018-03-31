#正则表达式匹配

def match(string, pattern):
    if string == None or pattern == None:
        return False
    string += ' '
    pattern += ' '
    return match_core(string, pattern)

def match_core(string, pattern):
    if string == ' ' and pattern == ' ':
        return True
    if string != ' ' and pattern == ' ':
        return False
    if pattern[1] == '*':
        if (pattern[0] == string[0]) or (pattern[0] == '.' and string[0] != ' '):
            return match_core(string[1:],pattern[2:]) or match_core(string[1:], pattern) or match_core(string, pattern[2:])
        else:
            return match_core(string, pattern[2:])
    if (string[0] == pattern[0]) or (pattern[0] == '.' and string != ' '):
        return match_core(string[1:], pattern[1:])
    return False

if __name__ == "__main__":
    print(match('aaa','ab*ac*a'))
    print(match('aaa','aa.a'))
    print(match('aaa','ab*a'))
