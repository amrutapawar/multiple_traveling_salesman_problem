# -*- coding: utf-8 -*-
"""


@author: Amruta Pawar
"""

import matplotlib.pyplot as pl
import numpy as np
import pylab as py
import math 

def Distance(R1,R2):
    return np.sqrt((R1[0]-R2[0])**2+(R1[1]-R2[1])**2)

   

def totaldistanceforeachcluster(sman,cluster):
    dist =0
    clusterdist = [sman]
    clusterdist += [cluster[sman][i] for i in range(len(cluster[sman]))]
    clusterdist = np.array(clusterdist)
    
    for i in range(len(cluster[sman])):
        dist+=Distance(clusterdist[i],clusterdist[i+1])
    dist+=Distance(clusterdist[-1],clusterdist[0])    
    return dist

    
def Ploteachcluster(cluster,distance):
    colours = ['c','crimson','green','black','blue']
    markers = ['o']
    k=0
    m=0
    
    p1 = pl.Rectangle((0,0),0.1,0.1,fc=colours[0])
    p2 = pl.Rectangle((0,0),0.1,0.1,fc=colours[1])
    p3 = pl.Rectangle((0,0),0.1,0.1,fc=colours[2])
    p4 = pl.Rectangle((0,0),0.1,0.1,fc=colours[3])
    p5 = pl.Rectangle((0,0),0.1,0.1,fc=colours[4])
    pl.legend((p1,p2,p3,p4,p5),('Salesman1','Salesman2','Salesman3','Salesman4','Salesman5'),loc='center right')
    
    for sman in cluster:
        Pt = [sman]
        Pt += [cluster[sman][i] for i in range(len(cluster[sman]))]
        Pt += [sman]
        Pt = np.array(Pt)
        
    
        pl.title('Total distance='+ str(distance))
        pl.xlim(xmin=0,xmax=310)
        pl.ylim(ymin=0,ymax=210)
        
        pl.plot(Pt[:,0],Pt[:,1],marker=markers[m],c=colours[k])
        k+=1
        
            
    pl.show()
    
 
def kmeans(S,R):
    print S
    print R
    
    cluster = {}
   
    for x in range(0,len(S)):
         key = tuple(S[x])
         cluster[key] = []
         
         
    for i in range(len(city)):
        min = 99999999
        min_s = []
        min_r = []
        for j in range(len(S)):
          
            print R[city[i]],S[j],Distance(R[city[i]],S[j])
            if(min > Distance(R[city[i]],S[j])):
                min = Distance(R[city[i]],S[j])
                min_s = S[j]
                min_r = R[city[i]]
           
        tmp_arr = cluster[tuple(min_s)]
        tmp_arr.append(min_r)
        cluster[tuple(min_s)] = tmp_arr
        
    
    distance = []            
    for sman in cluster:
        dist = totaldistanceforeachcluster(sman,cluster) 
        distance.append(dist)
        
        Ploteachcluster(cluster,distance) 
    distance=np.array(distance)    
    print distance
    Ploteachcluster(cluster,distance)
    SA_new(cluster)
  
    
def swap(cluster,nsman):
    
    x = len(cluster[nsman])
    r1 = np.random.randint(0,x)
    r2 = np.random.randint(0,x)
    r3 = np.random.randint(0,x)
    r4 = np.random.randint(0,x)

    temp = cluster[nsman][r1]
    cluster[nsman][r1] = cluster[nsman][r2]
    cluster[nsman][r2] = temp
    temp = cluster[nsman][r3]
    cluster[nsman][r3] = cluster[nsman][r4]
    cluster[nsman][r4] = temp
   
    return cluster[nsman]
     

def SA_new(cluster):
    new_cluster = {}
    solution = {}
    
    for x in range(0,len(S)):
        key1 = tuple(S[x])
        solution[key1] = []    
    
    
    for x in range(0,len(S)):
         key = tuple(S[x])
         new_cluster[key] = []    
    
    count=0
    
    temperature = 1e+10
    cooling_rate = 0.95
    temperature_end = 0.000000001
    
    while temperature > temperature_end:   
        count +=1
        
        print count        
        for nsman in cluster:
            new_cluster[nsman] = []
                    
            dist = totaldistanceforeachcluster(nsman,cluster)  
           
            
            next_order = swap(cluster,nsman)
            """next_order = np.random.permutation(cluster[nsman])"""
            
            
            new_cluster[nsman] = next_order
           
            dist_new = totaldistanceforeachcluster(nsman,new_cluster)
            print "total distance is " + str(dist_new), nsman
            
            difference = dist_new - dist
            
            
            if difference < 0 or math.e**(-difference/temperature) > np.random.rand():
                   
                solution[nsman] = new_cluster[nsman]
                
                """print "solution is " + str(solution)"""
                final_dist = dist_new   
                print "final total distance is " + str(final_dist), nsman
                """Ploteachcluster(solution,final_dist)"""
                
            temperature = temperature * cooling_rate
        
        """Ploteachcluster(solution,final_dist)"""
        Ploteachcluster(new_cluster,dist_new)
        """if(count == 117):
            restart_SA(new_cluster,finalcount=4)"""

def restart_SA(new_cluster,finalcount):
    print "restarting" 
    solution = new_cluster
    new_cluster1 = {}
    
    for x in range(0,len(S)):
         key = tuple(S[x])
         new_cluster1[key] = []    
    
    count1=0
    
    temperature1 = 1e+10
    cooling_rate1 = 0.95
    temperature_end1 = 0.000000001
    
    while temperature1 > temperature_end1:   
        count1 +=1
        
        print count1
    
        for nsman1 in solution:
            new_cluster1[nsman1] = []
        
         
            
            dist1 = totaldistanceforeachcluster(nsman1,solution)  
            
            next_order1 = swap(new_cluster,nsman1)
            new_cluster1[nsman1] = next_order1
            
            dist_new1 = totaldistanceforeachcluster(nsman1,new_cluster1)
            print "Total distance is " + str(dist_new1), nsman1
            
            difference1 = dist_new1 - dist1
           
            
            if difference1 < 0 or math.e**(-difference1/temperature1) > np.random.rand():
                solution1 = {}
                
                for x in range(0,len(S)):
                    key1 = tuple(S[x])
                    solution1[key1] = []
                          
                solution1[nsman1] = new_cluster1[nsman1]
                
                
                final_dist1 = dist_new1   
                print "final total distance is " + str(final_dist1), nsman1
                """Ploteachcluster(solution,final_dist)"""
               
            temperature1 = temperature1 * cooling_rate1
        if(count1==50 and finalcount !=0 ):
             finalcount -= 1
            
             restart_SA(new_cluster1,finalcount)
        
        Ploteachcluster(new_cluster1,final_dist1)        
    

    
if __name__=='__main__':
    n=0
    
    
        
    """#150 cities"""
    
    R = []
    for i in range(150):
        x=np.random.randint(1,200)
        y=np.random.randint(1,200)
        
        R.append([x,y])
    R = np.array(R)
    pl.plot(R[:,0],R[:,1],'-o')
    print "Cities are " + str(R)
  
    S = []
    for i in range(5):
        
        s1= np.random.randint(1,200)
        s2= np.random.randint(1,200)
        S.append([s1,s2])
    S = np.array(S)
    pl.plot(S[:,0],S[:,1],'-o')    
    
    print "Salesperson are " + str(S)

    city = range(150)

    kmeans(S,R)
    
    
    

    
   


