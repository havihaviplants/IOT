a = 23
if a < 50: # if 문을 선언한다.
    print('50보다 작군요') # if문에 조건이 맞으면 출력한다.

#if else 문

if a < 20:
    print('20보다 작군요')
else:
    print('20보다 크군요')
#elif 문

age = int(input('현재 나이를 입력합니다. ')) # 사용자가 입력한 값을 정수로 리턴

if age < 10:
    print('유년층입니다.')
elif age < 20:
    print('10대입니다.')
elif age < 30:
    print('20대입니다.')
elif age < 40:
    print('40대입니다.')
else:
    print('장년층입니다.')