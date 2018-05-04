#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import numpy as np


def process_line(line, hist):
    words = []

    line = strip_punctuation(line)
    for word in line.split():
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
    with open(filename, encoding='utf-8', mode='r') as f:
        for line in f:
            process_line(line, hist)
    return hist


def most_common(hist, num):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t[:num]


def wtire_to_file(data):
    with open('IMDB-vocab.txt', encoding='utf-8', mode='w') as f:
        index = 1
        for t in data:
            print(t[1])
            a = "{:<15}  {:<15} {}\n".format(t[1], str(index), str(t[0]))
            f.write(a)
            # f.write(t[1]+"\t\t"+str(index)+'\t'+str(t[0])+'\n')
            index = index + 1


def getlist():
    highFre = []
    with open('IMDB-vocab.txt', encoding='utf-8', mode='r') as f:
        for line in f:
            words = line.split()
            highFre.append(words[0])
    return highFre


def getmatric(list, file, file2, file3, file4):
    mat = []
    byline = []
    cl = []
    mat2 = []
    with open(file, encoding='utf-8', mode='r') as f:

        for line in f:
            line = strip_punctuation(line)
            vector = np.zeros(10, dtype=np.int8)
            vector2 = np.zeros(10, dtype=np.int8)
            bylinesub = []
            for word in line.split():
                word = word.lower()
                if word in list:
                    vector[list.index(word)] = 1
                    vector2[list.index(word)] = vector2[list.index(word)] + 1
                    bylinesub.append(list.index(word) + 1)
            bylinesub.append(int(line[-2]))
            bylinesub = np.array(bylinesub)
            byline.append(bylinesub)
            cl.append(int(line[-2]))

            mat.append(vector)
            mat2.append(vector2)

    np.savetxt(file2, byline, '%5s')
    np.savetxt(file3, cl, fmt="%d", delimiter=",")
    np.savetxt(file4, mat2, fmt="%d", delimiter=",")
    return mat


from string import punctuation


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


def run():
    hist = process_file('IMDB-train.txt')
    data = most_common(hist, 10)

    wtire_to_file(data)
    list = getlist()
    trainmat = getmatric(list, 'IMDB-train.txt', 'IMDB-trainbyline.txt', 'IMDB-trainclasss.txt', 'IMDB-trainmatbag.txt')
    testmat = getmatric(list, 'IMDB-test.txt', 'IMDB-testbyline.txt', 'IMDB-testclasss.txt', 'IMDB-testmatbag.txt')
    validmat = getmatric(list, 'IMDB-valid.txt', 'IMDB-validbyline.txt', 'IMDB-validclasss.txt', 'IMDB-validmatbag.txt')
    np.savetxt('IMDB-trainmat.txt', trainmat, fmt="%d", delimiter=",")
    np.savetxt('IMDB-testmat.txt', testmat, fmt="%d", delimiter=",")
    np.savetxt('IMDB-validmat.txt', validmat, fmt="%d", delimiter=",")

    print(data)


if __name__ == '__main__':
    run()

