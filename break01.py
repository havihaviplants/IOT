#for 문과 break 문을 활용해 1에서 20까지 합이 100보다 가장 가깝고 작은 합을 구하자

sum, i = 0, 0

for i in range(1, 20, 1):
    sum += i
    if sum > 100:
        break;
sum -= i

print("%d" % sum)
print("-----------")

#while문과 break 문을 이용해 입력한 1에서 숫자만큼 합을 구하시오.

sum, i = 0,0
j = int(input("숫자를 입력합니다. "))

while True:
    if i < j:
        i = i+1
        sum += i;
    elif i == j:
        break
print("1에서 %d까지의 합은 %d입니다." % (j, sum))