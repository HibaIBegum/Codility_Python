#numTimesBlue
def solution(A):

    R=-1
    C=0
    N=len(A)
    for i in range(N):
        if A[i]>R:
            R=A[i]
        if R==i+1:
            C+=1
    return C            