def replace_blank(string):
    """替换空格"""
    if isinstance(string,str):
        return(string.replace(" ","%20"))
    else:
        return False


if __name__ == "__main__":
    print(replace_blank("We are happy."))
    print(replace_blank(" We are happy."))
    print(replace_blank("We are happy. "))
    print(replace_blank("We are  happy."))
    print(replace_blank(3))
