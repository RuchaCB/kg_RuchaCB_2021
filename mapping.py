"""
contains 2 functions
mapping() which is called inside validate()
"""
def mapping(string1, string2):
    """ To check whether the string1 can be mapped to string2 or not"""
    dict1 = {}
    if len(string2) < len(string1):
        flag = "false"
    else:
        for i, char in enumerate(string1):
            if char not in dict1:
                dict1[char] = string2[i]
                flag = "true"
            elif dict1[char] == string2[i]:
                flag = "true"
            else:
                flag = "false"
    return flag

def validate():
    """To take valid user input"""
    try:
        string1, string2 = input().split()
        output = mapping(string1, string2)
    except ValueError:
        output = "Please enter a valid input"
    return output
