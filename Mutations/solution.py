def mutate_string(string, position, character):
    s = string
    p=position
    c=character
    
    string =s[:p] + c + s[p+1:]
    return string

