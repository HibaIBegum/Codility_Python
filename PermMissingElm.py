#Code PermMissingElm
def solution(A):
    total=sum(A)
    N=len(A)
    Expected=(N+1)*(N+2)//2
    return Expected-total