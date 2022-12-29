def solution(lines):
    # 선분과 선분의 관계는 겹친다, 포함한다, 만나지 않는다 관계만 있다.
    
    # 선분에 속하는 숫자 생성(맨 마지막 숫자는 제외 [0,3]->{0,1,2})
    line1 = set([num for num in range(lines[0][0],lines[0][1]) ])
    line2 = set([num for num in range(lines[1][0],lines[1][1]) ])
    line3 = set([num for num in range(lines[2][0],lines[2][1]) ])
    lines = [line1, line2, line3]
    
    # 각 선분 사이에 겹치는 부분 추출
    result = line1 & line2 |line2 & line3 | line1 & line3
    return len(result)

print(solution([[0, 5], [3, 9], [1, 10]]))