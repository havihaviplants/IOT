def mydef01(): #인수 없는 함수 선언
    print("함수를 선언합니다.")
mydef01() # 함수 호출

def mydef02(str="인수함수를 선언합니다."): #인수 있는 함수 선언
    print(str)
mydef02()
mydef02("인수를 넣습니다.")
