def PrimeList(N):
    '''
    Returns a list of prime nimbers from i to N calculated using the Erastothenes sieve.

    Input
    -----
    N   An integer. The upper bound of the prime numbers in the list to be returned.


    '''
    ans = list(range(2, N+1))
    i = 0
    p = ans[i]
    while p<ans[-1]:
        ans = list(set(ans).difference(set(range(2*p, ans[-1]+1, p )) ))
        ans.sort()
        i = i+1
        p = ans[i]

    return ans

if __name__=='__main__':
    N = 10000
    l = PrimeList(N)
    print(len(l), " primes in 1 < ", N, "\n", l)
