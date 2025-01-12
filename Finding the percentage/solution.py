if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    #a = student_marks[name][0]
    #b = student_marks[name][1]
    #c = student_marks[name][2]
    #
    d = len(student_marks[name])
    
    s = 0
    for i in student_marks[query_name]:
        s =i+s
    e = s/d
    print('%.2f'% e)
