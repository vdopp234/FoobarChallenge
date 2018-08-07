from fractions import Fraction
from fractions import gcd

def answer(m):

    #Construct P
    sums = []
    for i in range(len(m)):
        sum_i = sum(m[i])
        for j in range(len(m)):
            if sum_i == 0:
                m[i][j] = Fraction(0)
            else:
                m[i][j] = Fraction(-m[i][j], sum_i)
        sums.append(sum_i)
    for i in range(len(m)):
        m[i][i] = 1 + m[i][i]


    #finding terminal states
    terms = []
    for i in range(len(sums)):
        if sums[i] == 0:
            terms.append(i)

    #Solves for absorption rates
    inv = inverse(m)

    output = []
    a = len(terms)
    for i in range(len(terms)):
        vec = [0 for j in range(len(m))]
        vec[terms[i]] = 1
        h = mat_mul(inv, vec)
        output.append(h[0])

    #GCD's everything
    lst = [i.denominator for i in output]
    l = lcm(lst)
    output = [int(l*output[i]) for i in range(len(output))]
    output.append(int(l))
    return output

def inverse(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse

def mat_mul(mat, vec):
    out = []
    for i in range(len(mat)):
        s = 0
        for j in range(len(mat)):
            s += mat[i][j]*vec[j]
        out.append(s)
    return out

def lcm(lst):
    curr = lst[0]
    next = 1
    while(next < len(lst)):
        curr = gcd(curr,lst[next]) * (curr/gcd(curr, lst[next]))*(lst[next]/gcd(curr, lst[next]))
        next += 1
    return curr
