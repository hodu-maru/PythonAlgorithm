print('이름을 입력하세요: ',end='')
#print 함수에는 sep과 end를 인자로 줄 수 있음. sep은 , 자리에, end는 문자열 끝에 지정한 문자를 삽입.
#기본으로는 end='\n'이 들어가있어 해당 문자열출력 이후 개행이 됨.
#end=''은 개행 대신 아무것도 넣지 않으므로 문자열 출력 후 자동개행이 되지 않음

name = input()
#input()은 enter를 눌러야 입력이 완료

nonEndName = input('이름을 입력하세요')
print(f'안녕하세요? {name} 님.')
print('안녕하세요? {name} 님.')
#문자열 앞 f는 문자열 구성에 변수가 있다는 것. f를 안붙이면 걍 {변수명} 처럼 문자열이 찍혀나옴

print(int('13E5BA',16))