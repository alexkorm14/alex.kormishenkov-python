def make_dir(name):
	from os import getcwd, chdir, mkdir, listdir
	path = getcwd()
	chdir(path)
	str(name)
	list_dir = listdir()
	if name in listdir():
		print ("невозможно создать")
	else:
		mkdir(name)
		print ("Успешно создано")

def show_dir():
	from os import getcwd, chdir, listdir
	path=getcwd()
	chdir(path)
	print(listdir())

def remove_dir(name):
	from os import getcwd, chdir, listdir, rmdir
	path = getcwd()
	str(name)
	chdir(path)
	list_dir = listdir()
	if name in listdir():
		rmdir(name)
		print ("Успешно удалено")
	else:
		print ("Невозможно удалить")

def change_dir(name):
	from os import getcwd, chdir, listdir
	path=getcwd()
	chdir(path)
	str(name)
	list_dir = listdir()
	if name in listdir():
		chdir(name)
		print ("Успешно перешел")
	else:
		print ("Невозможно перейти")

def cp(file_name):
    import shutil
    import os
    path = os.getcwd()
    os.chdir(path)
    str(file_name)
    list_dir = os.listdir()
    if file_name in list_dir:
        copy = f'{file_name}.копия'
        shutil.copyfile(f'{path}/{file_name}',  f"{path}/{copy}")
        print('Успешно создана копия')
    else:
    	print ('Указанного файла нет в директории')

def rm(file_name):
	import os
	path = os.getcwd()
	os.chdir(path)
	str(file_name)
	list_dir = os.listdir()
	if file_name in list_dir:
		os.remove(f"{path}/{file_name}")
		print('Успешно удалено')
	else:
		print('Невозможно удалить')
def ls():
	import os
	path = os.getcwd()
	os.chdir(path)
	print (path)

def file_description(file_name):
	import os
	path=os.getcwd()
	os.chdir(path)
	if file_name in os.listdir():
		os.chdir(file_name)
		path= os.getcwd()
		print ('Время создания',os.path.getctime(path) )
		print ('Время изменения', os.path.getmtime(path))
		print ('Размер файла',os.path.getsize(path) )
	else:
		print ("Невозможно перейти")
def operation_system():
	import os
	print ('Информация об ОС',os.uname())
	print ('Переменные окружения',os.environ)
	print ('Текущий id процесса ',os.getpid())
	print ('имя пользователя - ',os.getlogin())

















