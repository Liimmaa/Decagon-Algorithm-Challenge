def solution(A):
        X = A.pop()
        Y = A.insert(1, X)
        print(Y)

solution([3,8,9,7,6])