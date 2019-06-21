#Расшифровываем шифр Виженера - частотный анализ
#Подсчет количества повторений каждого символа строки "a":
def count_items(a):
		r={}
		for i in a:
			if i not in r:
				r[i]=1.0
			else:
				r[i]=r[i]+1.0
		return r

#Подсчет частоты встречающихся в строке "а" символов:
def item_freqs(a):
	counts=count_items(a)
	for i in counts:
		counts[i]=counts[i]/len(a)
	return counts

#функция шифровки-дешифровки:	
def vigenere(a,b):
	ret=''
	n=0
	for c in a:
		ret=ret+chr(ord(c)^ord(b[n]))
		n+=1
		if n>=len(b):
			n=0
	return ret

#Частота букв в английском языке:
english = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
    ' ':0.15
    }

#Исходная строка:
a='f443d306cad09d91d86e0aed7a851cc7ccca83966b46ce4ddc1c8fcedc9bd32a42d84fce06c1c49d9cd965419949dd0cc6d7d49ed12a5dd058cd4fc9d6cf99d97f599958dc1fc6cddad0d7644e9941c00ec1cad397da6f59ca0cca01cad09d91d86e0ac349d700dc83db9ccf6344de0cc40cddccce83967e42dc0cd60cddc6d89e982a7ed149dc4fc2c2d69596624bda47cc01c883d19fd9610ad545ce0a8fd0d29dd37e42d042c24fdbcbdc84967345cc0ccd0ed9c69d84d92a48dc0cd61adfc6cfd0c5674bcb58851bc083d195d77844970cf107cada9d9dd7614f9944c40cc4cad397966645d6478503c6c8d8d0db6b4dd04f8b'.decode("Hex")

print('Дан шифротекст:\nf443d306cad09d91d86e0aed7a851cc7ccca83966b46ce4ddc1c8fcedc9bd32a42d84fce06c1c49d9cd965419949dd0cc6d7d49ed12a5dd058cd4fc9d6cf99d97f599958dc1fc6cddad0d7644e9941c00ec1cad397da6f59ca0cca01cad09d91d86e0ac349d700dc83db9ccf6344de0cc40cddccce83967e42dc0cd60cddc6d89e982a7ed149dc4fc2c2d69596624bda47cc01c883d19fd9610ad545ce0a8fd0d29dd37e42d042c24fdbcbdc84967345cc0ccd0ed9c69d84d92a48dc0cd61adfc6cfd0c5674bcb58851bc083d195d77844970cf107cada9d9dd7614f9944c40cc4cad397966645d6478503c6c8d8d0db6b4dd04f8b')
#Расчет вероятности длины ключа Р[N]:
P={}
N=4
while N<13:
	P[N]=0.0
	t=a[::N]
	itfr=item_freqs(t)
	for i in t:
		#суммируется разница между (частотой встречаемых в фрагменте символов) и (равномерной частотой символов в фрагменте):
		P[N]+=abs(itfr[i]-(1.0/26.0))
	N=N+1
	
#выбираем наибольшую из полученных вероятностей:	
N=max(P,key=P.get)


print('\nВероятности длины ключа от 4 до 12:')
print(P)
print('Наиболее вероятная длина ключа:')
print(N)


kluch=''
r={}
for n in xrange(N):
	test=a[n::N]				#срез текста начиная с n-го символа
	for i in xrange(256):
		c=chr(i)				#перебираем с=1..255
		decr=vigenere(test,c)	#расшифровываем срез с помощью ключа "с"
		decr_freqs=item_freqs(decr)		#считаем частоту символов в полученной расшифровке
		s = 0.0
		for j in decr_freqs:			#для каждого символа в расшифрованном тексте
			if j in english:			#считаем сумму разницy между частотой каждого символа
				s+=(english[j]-decr_freqs[j])**2		#если он есть в английском алфавите
			else:						#а если нет, то прибавляем просто частоту в срезе:
				s+=decr_freqs[j]
		r[c]=s
	c=min(r,key=r.get)		#выбираем такую букву, для которой эта сумма разниц минимальна

	kluch+=c				#и записываем ее в ключ

print('\nПолучился ключ:')
print repr(kluch)
print('\nРашифрованный текст:')
text=vigenere(a,kluch)
print text

#исправление только для этого шифротекста
print('\nВидно, что четвертый символ ключа подробран неверно. Исправленный ключ выглядит так:')
kluch2=kluch[0]+kluch[1]+kluch[2]+'o'+kluch[4]+kluch[5]+kluch[6]+kluch[7]+kluch[8]+kluch[9]+kluch[10]
text=vigenere(a,kluch2)
print repr(kluch2)
print('\nИ расшифрованный текст:')
print(text)
#исправление закончилось
