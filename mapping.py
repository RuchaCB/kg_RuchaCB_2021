
def mapping(string1, string2):
    dict1={}
    if len(string2)<len(string1):
        flag = "false"
    else:
        for i, char in enumerate(string1):
            if char not in dict1:
                dict1[char]=string2[i]
                flag = "true"
            elif dict1[char] == string2[i]:
                flag = "true"
            else:
                flag = "false"
    return flag

def validate():
    try:
        string1, string2 = input().split() 
        print(mapping(string1,string2))
    except ValueError:
        return ("Please enter a valid input")
    except NameError:
        return ("Please enter a valid input")
