# -*- coding: utf-8 -*-
import string

def process_line(line, hist):
    words = []
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        words.append(word)
    for word in words:
        hist[word] = hist.get(word, 0) + 1
        # if word not in hist:
        #     hist[word] = 1
        # else:
        #     hist[word] = hist[word] + 1

def process_file(filename):
    hist = {}
    with open(filename, 'r') as f:
        for line in f:
            process_line(line, hist)
    return hist


def most_common(hist, num):
    t = []
    for key,value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t[:num]


def wtire_to_file(data):
    with open('IMDB-vocab.txt','w') as f:
        index = 1
        for t in data:
            print(t[1])
            a="{:<15}  {:<15} {}\n".format(t[1],str(index),str(t[0]))
            f.write(a)
            # f.write(t[1]+"\t\t"+str(index)+'\t'+str(t[0])+'\n')
            index = index+1

def run():
    hist = process_file('IMDB-train.txt')
    data = most_common(hist,10000)
    wtire_to_file(data)
    print(data)

if __name__ == '__main__':
    run()


