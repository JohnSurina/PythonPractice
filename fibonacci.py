def fib(n):
    '''This method prints out the fibonacci sequence
    up to the supplied number'''
    a,b = 0,1
    if n <= 0:
        print('0')
        return()
    while b <= n:
        print(b)
        b_ = b
        b = a+b
        a = b_