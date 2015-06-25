#!/usr/bin/env python
'''
Created on Sep 3, 2013

@author: mhty7
'''
import re
MAX_WEIGHT = 100
class graphmatrix_ :
    def __init__(self,n):
        self.nn=[[0 for j in range(n)] for i in range(n)]
    
    def init_matrix(self):
        i1=0
        i2=0
        for i1 in range(len(self.nn)) :
            n1=self.nn[i1]
            for i2 in range(len(n1)) :
                self.nn[i1][i2]=MAX_WEIGHT
                self.nn[i2][i2]=0
                
    def add_e(self,v1,v2,w):
        self.nn[v1-1][v2-1]=w
    
    def get_matrix(self):
        return self.nn
    
    @classmethod
    def show_matrix(cls,D,P):
        print P
        i1=0
        i2=0
        for i1 in range(-1,len(D)) :
            if i2==-1:
                print u'   v%1d ' % (i1+1),
            n1=D[i1]
            for i2 in range(-1,len(n1)) :
                if i1 == -1:
                    if i2 == -1:
                        print u' %4s ' % '',
                        continue
                    print u'   v%1d ' % (i2+1),
                    continue
                elif i2==-1:
                    continue
                print u'[%4d]' % D[i1][i2],
            print ''
            i2=-1
        print ''

class floydwarshall_ :
    def __init__(self,C):
        self.C=C
        self.D=None
    def compute(self):
        self.D=list(self.C.get_matrix())
        v_num=len(self.D)
        
        for k in range(v_num):
            for u in range(v_num) :
                for v in range(v_num) :
                    if self.D[u][k]+self.D[k][v]<self.D[u][v]:
                        self.D[u][v]=self.D[u][k]+self.D[k][v]
        
        graphmatrix_.show_matrix(self.D,'Matrix of weights of shortest paths, D /')
        
if __name__ == "__main__":
    v_num=0
    et={}
    f=open("input.txt",'r')
    whole=f.read()
    tmp=whole.split('v=')
    tmp=tmp[1].partition(';')
    vc=tmp[0]
    tmpp=vc.partition('[')[2]
    tmpp=tmpp.rpartition(']')[0]
    for v in tmpp.split(','):
        v_num+=1
    
    C = graphmatrix_(v_num)
    C.init_matrix()
    
    whole=tmp[2]
    tmp=whole.split('e=')
    tmp=tmp[1].partition(';')
    ec=tmp[0]
    tmpp=ec.partition('[')[2]
    tmpp=tmpp.rpartition(']')[0]
    
    p=re.compile(r'\[\s*(\d+),(\d+)\s*\]')
    h=0
    for v in p.finditer(tmpp):
        h+=1
        et[h]=[int(v.group(1).strip()),int(v.group(2).strip())]


    whole=tmp[2]
    tmp=whole.split('w=')
    tmp=tmp[1].partition(';')
    wc=tmp[0]
    tmpp=wc.partition('[')[2]
    tmpp=tmpp.rpartition(']')[0]
    
    h=0
    for v in tmpp.split(','):
        h+=1
        v=int(v.strip())
        e=et[h]
        C.add_e(e[0],e[1],v)
    
    f.close()

    
    graphmatrix_.show_matrix(C.get_matrix(),'Weighted adjacency matrix C /')
    
    main=floydwarshall_(C)
    main.compute()
    
    