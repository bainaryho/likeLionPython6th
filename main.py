print('1')
print('2', end='')
print('3', end='')
print('4')
#결과
#1
#234

data = [10, 20, -50, 21.3, 'LikeLion']
print(data, type(data)) #[10, 20, -50, 21.3, 'LikeLion'] <class 'list'>

#문자열 구분자 변경( sep= )
print("Like","Share","Lion") #Like Share Lion #띄어쓰기가 됨
print("Like","Share","Lion", sep='') #LikeShareLion #붙어서 출력
print("Like","Share","Lion", sep='$') #Like$Share$Lion

#줄바꿈
print("Like","Share","Lion", sep='$', end='\t') #Like$Share$Lion
print("Like","Share","Lion", sep='$', end='\t') #Like$Share$Lion
#Like$Share$Lion	Like$Share$Lion #tab키 만큼 줄바꿈
