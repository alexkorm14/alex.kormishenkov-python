#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих 
#переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode 
#и также проверить тип и содержимое переменных.

def inform_about_word(word):
	print ('тип переменной - {}'.format(type(word)))
	print ('содеражание переменной - {}'.format(word))
	return 'длина строки - {}'.format(len(word))
words = ['разработка', 'сокет', 'декоратор']

for word in words:
	print (inform_about_word(word))


words = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for word in words:
	print (inform_about_word(word))
	
#2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
#(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
words = [b'class', b'function', b'method']
for word in words:
	print (inform_about_word(word))

#3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Невозможно записать в байтовом типе слова: "класс", "функция", потому что эти слова не относятся к ASCII (они на киррилице, а не на латинице)

#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
words = ['protocol', 'standard', 'разработка', 'администрирование']
for word in words:
	enc_word=word.encode('utf-8')
	print ('{} - {}'.format(word, enc_word))
	dec_word = enc_word.decode('utf-8')
	print ('{}'.format(dec_word))

#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess

web_resource = ['ping', 'yandex.ru']

subproc_ping=subprocess.Popen(web_resource, stdout = subprocess.PIPE)
for line in subproc_ping.stdout:
	line = line.decode('MacCyrillic').encode('utf-8')
	print (line.decode('utf-8'))

web_resource = ['ping', 'youtube.com']

subproc_ping=subprocess.Popen(web_resource, stdout = subprocess.PIPE)
for line in subproc_ping.stdout:
	line = line.decode('MacCyrillic').encode('utf-8')
	print (line.decode('utf-8'))
 


#6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
import locale
words = ['сетевое программирование','сокет','декоратор']
with open("test_file.txt", 'a') as f:
	for word in words:
		f.write('{}\n'.format(word))
print (f)
#codirovrka = locale.getpreferredencoding()
with open("test_file.txt", 'r', encoding='utf-8') as f:
	for line in f:
		print (line)






















