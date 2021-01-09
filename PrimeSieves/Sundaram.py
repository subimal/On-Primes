def PrimeList(N):
    '''
    Returns a list of prime nimbers from i to N calculated using Sundaram's sieve.

    Input
    -----
    N   An integer. The upper bound of the prime numbers in the list to be returned.


    '''
    ans = list(range(1, (N-1)//2+1))
    remove=[]
    k=0
    for j in range(1, N+1):
        for i in range(1, j+1):
            k=(i+j+2*i*j)
            if k>N:
                break
            remove.append(k)
    ans = list(set(ans).difference(set(remove)))
    ans.sort()
    ans_final = [2]
    for i in ans:
        j = 2*i+1
        if (j) <= N:
            ans_final.append(j)
        else:
            break

    return ans_final

if __name__=='__main__':
    N = 1000000
    l = PrimeList(N)
    print(len(l), " primes in 1 < ", N, "\n")
