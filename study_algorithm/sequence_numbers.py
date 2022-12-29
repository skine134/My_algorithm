def solution(n, total):
    min_value = total/n - (n-1)/2
    return [i for i in range(int(min_value),int(min_value+n))]