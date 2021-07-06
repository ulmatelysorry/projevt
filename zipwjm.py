def reverseNumber(num):
    t = num
    t1 = 0
    while num:
        t1 *= 10
        t1 += num % 10
        num //= 10
    '''if t1 == t:
        return True
    return False'''
    print(t1,t,type(t1),type(t))

reverseNumber(123)