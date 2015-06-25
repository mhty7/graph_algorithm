#!/usr/bin/env python
'''
Created on Sep 3, 2013

@author: mhty7
'''
import re
MAX_WEIGHT = 100
class graph_ :
    def __init__(self):
        self.vertices =[]
        self.edges = []
    
    def add_v(self,v):
        self.vertices.append(v)
        
    def add_e(self,e):
        self.edges.append(e)
        e.v1.add_adj(e)
        
    def get_v(self):
        return self.vertices
    
    @classmethod
    def extract_min(cls,Q):
        prev=0
        for i in range(1,len(Q)):
            if Q[prev].dist>Q[i].dist:
                prev=i
        return Q.pop(prev)
        
class edge_ :
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
        
class vertex_:
    def __init__(self,label):
        self.label=label
        self.adj=[]
        self.dist = None
        self.prev = None
    def add_adj(self,v):
        self.adj.append(v);
    
    def get_adj(self):
        return self.adj
    
class dijkstra_ :
    def __init__(self,G,w,s,t):
        self.G=G
        self.w=w
        self.s=s
        self.t=t
        self.S=[]
        self.Q=[]
        self.PREV={}
    def compute(self):
        for key in self.w :
            if self.w[key] < 0:
                print 'There should not be negative weights.'
                return
        
        for v in self.G.get_v():
            if v==self.s:
                v.dist=0
            else:
                v.dist=MAX_WEIGHT
            v.prev=None
            self.Q.append(v)
            

        
        while not len(self.Q)==0:
            u=graph_.extract_min(self.Q)
            self.S.append(u)
            adj=u.get_adj()
            for edge in adj:
                v=edge.v2
                if self.w[edge]+u.dist<v.dist:
                    v.dist=self.w[edge]+u.dist
                    self.PREV[v]=u
        
        
        print 'The shortest path to Terminal is',
        v=self.t
        sp=[]
        while not v==None:
            sp.insert(0, v)
            v=self.PREV.get(v)
        
        for v in sp:
            print u'[%s] ' % v.label,
        
        print ''
        print u'The weight of such path is %d' % t.dist
            
if __name__ == "__main__":
    G = graph_()
    wt={}
    vt={}
    et={}
    f=open("input.txt",'r')
    whole=f.read()
    tmp=whole.split('v=')
    tmp=tmp[1].partition(';')
    vc=tmp[0]
    tmpp=vc.partition('[')[2]
    tmpp=tmpp.rpartition(']')[0]
    for v in tmpp.split(','):
        v=v.strip()
        vt[v]=vertex_(v)
        graph_.add_v(G,vt[v])
    
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
        et[h]=edge_(vt[v.group(1).strip()],vt[v.group(2).strip()])
        graph_.add_e(G,et[h])

              
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
        wt[e]=v
                
    whole=tmp[2]
    tmp=whole.split('s=')
    tmp=tmp[1].partition(';')
    sc=tmp[0]
    s=vt[sc.strip()]
    whole=tmp[2]
    tmp=whole.split('t=')
    tmp=tmp[1].partition(';')
    tc=tmp[0]
    t=vt[tc.strip()]
    
    f.close()

    main = dijkstra_(G,wt,s,t)
    main.compute()
