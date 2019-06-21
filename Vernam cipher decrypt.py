#Дешифруем шифр Вернама - но все в порядке, ведь нам известно, что ключ был использован более чем один раз

T='37cabdb99b806cfa654ec1ea84d8d5d1ce0cce791572deded473fba49b96a321d23ecddc0234cdf2bd9fd478fd2a42dbb9d0c7dfcdcf5f8f6d193efbded56bb2bd99c28221ca3ecddc022ddbf2a697d46ff96f0adaa582c3d5828b41da780472e396c975f9ea99c2ca70cc35c7d90229d6f2bd9fd33bf76f5ec5af95de90d5c443cb785033f99a807de0a58ad38421d531c9ce0234cab7ea89cf74f1790ad3b89590dccddd49c3725c72f39fd270b2ea91d88e21dd35c7db022dcda0af91d67ee7260adfa39cd5c382df438f6c1f72f59bc674e0afd0ffca72d535c7db0228cda5af88c569b92a6392a291c6d5828b5cdd641d3be49bd33be6a5d0dd8f64c970cbdf02'.decode("hex")

def count_items (T):     # Счет элементов в массиве
	r={}
	for i in T:
		if i not in r:
			r[i]=1.0 
		else:
			r[i]=r[i]+1.0 
	return r 

def item_flegs (T): # Счет частоты букв
	counts=count_items (T)
	for i in counts:
		counts [i]=counts [i]/len(T)
	return counts 
	
def vigenere(T,K): # Функция расшифровки
	ret=''
	n=0
	for c in T:
		ret=ret+chr(ord(c)^ord(K[n]))
		n+=1 
		if n >= len(K):
			n=0
	return ret

E = {
'a': 0.07167,
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
'l': 0.054,
'm': 0.02406,
'n': 0.06749,
'o': 0.07507,
'p': 0.01929,
'q': 0.00095,
'r': 0.05987,
's': 0.06527,
't': 0.09056,
'u': 0.02758,
'v': 0.00978,
'w': 0.02360,
'x': 0.00150,
'y': 0.01974,
'z': 0.00074,
' ':0.20,
'.':0.002,
',':0.02
}

Key=37 # Длина ключа, равна колличеству символов в каждом сообщении

# Нахождениеключа
K='' # Ключик
for n in range (Key):
	Mas={} # Массив с вероятностями
	t=T[n::Key] # Построение среза зашифрованной функции n-ым символом
	for i in range(256):
		S=chr(i)
		text=vigenere(t,S) # расшифровка среза
		Ver=item_flegs (text) # находим вероятности символов
		M=0.0
		m=10.0
		for j in Ver:
			if j in E:
				M += abs(Ver[j]-E[j])
			else:
				M += abs(Ver[j])
		Mas[S]=M 
	for l in Mas:
		if Mas[l]<m:
			m=Mas[l]
			ind=l
	K += ind # Получение ключика

#K2 = K[0]+vigenere(T[3], 'h')+K[2:7]+vigenere(T[7], 'o')+K[8:20]+vigenere(T[20], 'd')+K[21]+vigenere(T[22], 'I')+K[23:25]+vigenere(T[25], 'h')+K[26:32]+vigenere(T[32], 'k')+K[33:35]+vigenere(T[35], 'w')+K[36:38]
K2 =vigenere(T[74],'M')+vigenere(T[149], 'h')+K[2:7]+vigenere(T[7], 'o')+K[8:19]+vigenere(T[93], 's')+ K[20:22] + vigenere(T[22], 'I')+K[23:25]+ vigenere(T[25], 'h') + K[26:32] + vigenere(T[32],'k') + K[33] + vigenere(T[34],'o') + vigenere(T[35],'w') + vigenere(T[36],'.')

# Расшифровка текста
Text=vigenere(T,K2)
print repr(T) 
print('\n-->\n')
y=0
for h in xrange(7):
  H=Text[y:y+37]
  y+=37
  print H
