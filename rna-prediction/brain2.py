# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:42:03 2017

@author: rohankoodli
"""

import os
from readData import read_movesets_pid
from encodeRNA import encode_movesets, encode_movesets_style
import numpy as np
import pandas as pd
import ast
import copy

#filepath = os.getcwd() + '/movesets/move-set-11-14-2016.txt'
#data, users = read_movesets_pid(filepath,6892348)
#encoded = (encode_movesets_style(data))
#
#moveset_dataFrame = pd.read_csv(filepath, sep=" ", header="infer", delimiter='\t')
#puzzles_pid = (moveset_dataFrame.loc[moveset_dataFrame['pid'] == 6892348])
##print puzzles_pid
#
#plist = list(puzzles_pid['move_set'])
##print plist
#bf_list = []
#for i in plist:
#  s1 = (ast.literal_eval(i))
#  s2 = s1['begin_from']
#  bf_list.append(s2)
#
#
##print bf_list[0]
#
#encoded_bf = [] # this is input for getting structure from Vienna webserver
#
#for start in bf_list:
#    enc = []
#    for i in start:
#        if i == 'A':
#            enc.append(1)
#        elif i == 'U':
#            enc.append(2)
#        elif i == 'G':
#            enc.append(3)
#        elif i == 'C':
#            enc.append(4)
#    encoded_bf.append(enc)

#print encoded_bf[0]
#print (encoded[0])

X,y = [],[]

'''
for i,j in (zip(encoded_bf,encoded)):
    #print i
    for m in j:
        #print m[1]
        X.append(i)
        y.append(m)
        loc = m[1] - 1
        #i = i[loc].replace(m[0])
        i[loc] = m[0]

for move in ((encoded)):
    for i in move:
        pass
'''
X = [[[1,1,1,1],[1,1,1,1]],[[1,2,3,1],[1,2,3,1]],[[1,1,1,3,4],[1,1,1,3,4]]]
ebf = [[1,1,1,1],[1,2,3,1],[1,1,1,3,4]]
ecd = [[[4,2],[3,2],[1,1]],[[4,1],[3,4]],[[1,4],[2,2],[3,1],[4,4]]]
#
#for i,j in zip(ebf,ecd):
#    #print X
#    temp = copy.deepcopy(i)
#    X.append(temp)
#    #print X
#    for m in j:
#        y.append(m)
#        loc = m[1] - 1
#        temp[loc] = m[0]
#        #print 'temp',temp
#        #print X
#        #X.append(temp)
# #       print X
#
#print X
#print y

#X,y = [],[]
for i,j in zip(ebf,ecd):
    #print X
    #print i
    #X.append(i*len(j))
    pass

#for i,j in zip(ebf,ecd):
#    temp = copy.deepcopy(i)
#    X.append([temp] * len(j))

print "Trying a diff loop"
Z = []
Z1 = []
for i in ecd:
    Z = []

    for j in range(0,len(i)):
        temp = copy.deepcopy(ebf[ecd.index(i)])
        Z.append(temp)
    print Z
    Z1.append(Z)

print "Z1 = "
print Z1    


print X

#print X

#for i in X:
#    i[1] = 4
y0 = []
for i in ecd:
    for j in i:
        y0.append(j)

print ecd

#print ecd


#for i in range(len(X)):
#    try:
#        print i
#        loc = y0[i][1] - 1
#        X[i+1][loc] = y0[i][0]
#        print X
#    except IndexError:
#        break
#    
#print '\n',X

for i in (Z1):
    for j in range(len(i)):
        try:
            print j
            loc = ecd[Z1.index(i)][j][1] - 1
            print loc
            #print 'index',i[j+1][loc]
            print i[j+1]
            i[j+1][loc] = ecd[Z1.index(i)][j][0]
            print Z1
        except IndexError:
            continue

print '\n',Z1,'\n'
print ecd

#print X
#print y
#print X[110]
#print X[114]
#print len(X)
#print len(y)


#from Bio import SeqIO
#
#sequences = ['AAAAA','ACCA','GGGGAAAAAGGGG']
#
#
#with open("example.fasta", "w") as output_handle:
#    SeqIO.write(sequences, output_handle, "fasta")
import tflearn

X = np.array([[[1,2,3,4],[0,1,0,1],[1,1,1,1],[-3,0,0,0]],[[4,3,2,1],[1,0,1,0],[0,0,0,0],[9,0,0,0]]])
Y = np.array([[4,2],[3,3]])

tflearn.init_graph(num_cores=1)

net = tflearn.input_data(shape=[None, 2,4,4])
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net)
model.fit(X, Y)
