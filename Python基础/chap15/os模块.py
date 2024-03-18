import os
#os.system('notepad.exe')
#os.system('calc.exe')
#os.startfile('D:\\QQ\\Bin\\QQScLauncher.exe')

print(os.getcwd())
lst=os.listdir('..//chap15')
print(lst)
os.mkdir('newdir')
os.makedirs('A/B/C')
#os.rmdir('newdir')
#os.removedirs('A/B/C')
#os.chdir(E://...)