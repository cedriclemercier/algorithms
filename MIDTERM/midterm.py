A = [1,2,3,4]
B = [5,-2,3,5]
C = [7,8,8,7]


def check_null(A, x):
    check = False
    if x not in A:
        check = True
    return check



def n3(A,B,C):
    count =0
    check=True
    for i in A:
        for j in B:
            for k in C:
                if k == i or k == j or j == i:
                    check = False
                count += 1
    
    return check, count
    
print(n3(A,B,C))

# Here we are nesting 3 loops to see if an element exists in all lists and count by 1 every loop
# count returns 64 which corresponds to 4 (n elements) ^ 3 (number of loops)


def n2(A,B,C):
    count =0
    check=True
    for i in A:
        for j in B:
            count += 1
            if j == i:
                check = False
                return check, count
            
    for i in B:
        for j in C:
            count += 1
            if j == i:
                check = False
                return check, count
            
    for i in A:
        for j in C:
            count += 1
            if j == i:
                check = False
                return check, count
    
    return check, count
    
print(n2(A,B,C))

# Here we return the function if the condition is satisfied so we check only n^2 times
# it should return close to 16 for 4 (n) ^2 (loops)
