# 문제1) 사용자가 입력한 단수를 출력하는 코드 (구구단)
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i} = {dan*i}")


# 문제2) 2단부터 9단까지 출력(중첩 for문)
# for i
#     for j
#         for k
for i in range(2, 10):             # 큰 반복
    for j in range(1, 10):         # 작은 반복
        print(f"{i}x{j} = {i*j}")  # 작은 반복 먼저 끝나면 큰 반복


# 문제 3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a의 길이 => len(a)
total = 0
for num in a:
    total = total + num  # total += num  # 총합 계산
result = total/len(a)

# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2))   # 평균값

# 문제4) 숙제@@ list b에서 최솟값 찾기
b = [22, 1, 4, 7, 98]

print(num_min)  # 1 출력