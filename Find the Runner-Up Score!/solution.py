if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    joy=a[0]
    mn =a[0]
    for i in a:
        if(i>joy):
            joy = i
        if (i<mn):
            mn=i
    
    r1 = mn 
    for i in a :
        if(i>r1 and i<joy):
            r1 = i
    print(r1)      
