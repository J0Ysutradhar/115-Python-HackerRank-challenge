def swap_case(s):
    output=''
    for c in s:
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper()
        output+=c
            
        
    return output
