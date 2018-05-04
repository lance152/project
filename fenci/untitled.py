import numpy as np
import string

list=[]
with open('yelp-vocab.txt',encoding='utf-8',mode='r') as f:
	for line in f:
		words = line.split()
		list.append(words[0])
list = list[:5]
mat=[]
byline=[]
with open('yelp-valid.txt',encoding='utf-8',mode='r') as f:
	for line in f:
		line = line.replace('-',' ')
		vector = np.zeros(len(list),dtype=np.int8)
		bylinesub=[]
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()

			if word in list:
				vector[list.index(word)]=1
				bylinesub.append(list.index(word))

			mat.append(vector)
		bylinesub.append(int(line[-2]))

		bylinesub = np.array(bylinesub,dtype=np.int8)
		print(type(bylinesub))
		print(type(vector))

		byline.append(bylinesub)
		#print(byline)
np.savetxt('results.txt',byline,'%s')
