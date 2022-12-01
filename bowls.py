#     * * * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *

n = 6
# sum the number of bowls given the number of rows(n)
def sum_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        s = n + sum_bowls_recursive(n - 1)
        return s




def sum_bowls_loop(n):
    S = 0
    for i in range(1, n + 1):
        S = S + i
    return S




def sum_bowls_seq(n):
    return int(((1+n)/2)*n)




def time_func(func, n):
    t0 = time()
    print('Calling: {}'.format(func))
    print(func(n))
    t1 = time()
    elapsed = t1 - t0
    print('running {}, took: {}'.format(func, elapsed))



#n = 998



n = 20000000



time_func(sum_bowls_loop, n)
time_func(sum_bowls_seq, n)