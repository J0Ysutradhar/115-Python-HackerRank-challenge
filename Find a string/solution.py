def count_substring(string, sub_string):
    c =0
    l = len(sub_string)
    for i in range (len(string)):
        s = (string[i:l+i ])
        #print(s)
        if s == sub_string:
            c+=1
    return c

