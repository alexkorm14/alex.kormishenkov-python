# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os 
path = os.getcwd()
os.chdir(path)
def name_dir(i):
	name = f"dir_{i}"
	return str(name)
#dirs = [ os.mkdir(name_dir(i))for i in range(1,10)] #--> создает папки


#rmdirs = [ os.rmdir(name_dir(i)) for i in range(1,10)] #--> удаляет созданные папки

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
path = os.getcwd()
os.dir(f'{path}/')
#os.chdir("1 курс")
print (os.getcwd())


#print(os.listdir())



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
path = os.getcwd()
name = 'lesson_5_easy.py'
copy_name = 'lesson_5_easy_copy'
shutil.copyfile(f'{path}/{name}',  f"{path}/{copy_name}")
if os.path.isfile(f"{path}/{copy_name}"):
	os.remove(f"{path}/{copy_name}") --> чтобы удалить сразу, не заимать ваше место на компьютере





