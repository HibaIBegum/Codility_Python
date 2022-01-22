#TapeEquilibrium
def solution(A):
    
    N = len(A)

    Total=sum(A)

    L = Total - A[N - 1]
    R = A[N - 1]
    d = abs(R - L)
    for ind in range(N - 2, 0, -1):
        L -= A[ind]
        R += A[ind]
        
        d = min(d, abs(R - L))

    return d  

if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))