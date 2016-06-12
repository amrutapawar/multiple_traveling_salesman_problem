# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:36:56 2016

@author: Amruta Pawar
"""
import numpy as np
import copy


"""font 1 """
inputA = [[-1, -1, -1, -1,  1, -1, -1, -1, -1],
          [-1, -1, -1, -1,  1, -1, -1, -1, -1],
          [-1, -1, -1,  1, -1,  1, -1, -1, -1],
          [-1, -1,  1,  1,  1,  1,  1, -1, -1],
          [-1, -1,  1, -1, -1, -1,  1, -1, -1],
          [-1, -1,  1, -1, -1, -1,  1, -1, -1],
          [ 1,  1,  1,  1, -1,  1,  1,  1,  1]]
         
"""font 1 """
inputB = [[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1,  1,  1,  1,  1,  1,  1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [ 1,  1,  1,  1,  1,  1,  1,  1, -1]]
          
"""font 1"""
inputC = [[-1, -1,  1,  1,  1,  1,  1,  1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
          [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
          [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1, -1,  1,  1,  1,  1,  1,  1,  1]]

"""font 1"""
inputD = [[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [ 1,  1,  1,  1,  1,  1,  1,  1, -1]]
          
"""font 1"""
inputE = [[ 1,  1,  1,  1,  1,  1,  1,  1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1,  1, -1, -1, -1, -1, -1],
          [-1,  1,  1,  1, -1, -1, -1, -1, -1],
          [-1,  1, -1,  1, -1, -1, -1, -1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [ 1,  1,  1,  1,  1,  1,  1,  1,  1]]
          
"""font 1"""
inputJ = [[-1, -1, -1, -1,  1,  1,  1,  1,  1],
          [-1, -1, -1, -1, -1, -1,  1, -1, -1],
          [-1, -1, -1, -1, -1, -1,  1, -1, -1],
          [-1, -1, -1, -1, -1, -1,  1, -1, -1],
          [-1, -1,  1, -1, -1, -1,  1, -1, -1],
          [-1, -1,  1, -1, -1, -1,  1, -1, -1],
          [-1, -1, -1,  1,  1,  1, -1, -1, -1]]
          
"""font 1"""
inputK = [[ 1,  1,  1, -1, -1,  1,  1, -1, -1],
          [-1,  1, -1, -1,  1, -1, -1, -1, -1],
          [-1,  1, -1,  1, -1, -1, -1, -1, -1],
          [-1,  1,  1, -1, -1, -1, -1, -1, -1],
          [-1,  1, -1,  1, -1, -1, -1, -1, -1],
          [-1,  1, -1, -1,  1, -1, -1, -1, -1],
          [ 1,  1,  1, -1, -1,  1,  1, -1, -1]]
          
          
outputA = [1,-1,-1,-1,-1,-1,-1]
outputB = [-1,1,-1,-1,-1,-1,-1]
outputC = [-1,-1,1,-1,-1,-1,-1]
outputD = [-1,-1,-1,1,-1,-1,-1]
outputE = [-1,-1,-1,-1,1,-1,-1]
outputJ = [-1,-1,-1,-1,-1,1,-1]
outputK = [-1,-1,-1,-1,-1,-1,1]


theta = 0.8
bias = -1
alpha = 0.03

inputs = []
weights = []

appendwt = []
for x in range(0,7):
    weightz = []
    for y in range(0,7):
        newwt = []
        for z in range(0,63):
            weight = round(np.random.rand(),2)
            newwt.append(weight)
        newwt.append(theta)
        weightz.append(newwt)
        
    weights.append(weightz)
print "weightz is " + str(weights)


for p in range(len(weights)):
    for q in range(len(weights)):
        weights[p][q] = copy.deepcopy(weights[0][0])
print weights 


x1 = []
for j in range(0,7):
    for k in range(0,9):
       x = inputA[j][k]
       x1.append(x)
x1.append(bias)
"""print x1"""

x2 = []
for l in range(0,7):
    for m in range(0,9):
       x = inputB[l][m]
       x2.append(x)
x2.append(bias)
"""print x2"""

x3 = []
for a in range(0,7):
    for b in range(0,9):
       x = inputC[a][b]
       x3.append(x)
x3.append(bias)
"""print x3"""

x4 = []
for c in range(0,7):
    for d in range(0,9):
       x = inputD[c][d]
       x4.append(x)
x4.append(bias)
"""print x4"""

x5 = []
for e in range(0,7):
    for f in range(0,9):
       x = inputE[e][f]
       x5.append(x)
x5.append(bias)
"""print x5"""

x6 = []
for g in range(0,7):
    for h in range(0,9):
       x = inputJ[g][h]
       x6.append(x)
x6.append(bias)
"""print x6"""

x7 = []
for n in range(0,7):
    for o in range(0,9):
       x = inputK[n][o]
       x7.append(x)
x7.append(bias)
"""print x7"""

inputs.append(x1)
inputs.append(x2)
inputs.append(x3)
inputs.append(x4)
inputs.append(x5)
inputs.append(x6)
inputs.append(x7)
inputs=np.array(inputs)
print inputs

output = []
output.append(outputA)
output.append(outputB)
output.append(outputC)
output.append(outputD)
output.append(outputE)
output.append(outputJ)
output.append(outputK)
output = np.array(output)
print output

iteration = 0
done = False

"""training """
while not done:

    done = True
   
    """deltaw =[0,0,0,0,0,0,0] """
    deltaw = []
    for f in range(0,64):
        deltaw.append(0)        
            
        
        
    deltanew = []
    finaloutput = []
    
    iteration += 1
    print "iter is " + str(iteration)
    for inpu,out in zip(range(len(inputs)),range(len(output))):
                
        x=[]
        deltanew.append(deltaw)
        print deltanew
        print "new weights are " + str(inpu),str(out)
        
        for k in range(0,64):
                x1 = inputs[inpu][k]
                x.append(x1)
        x.append(bias)
        print x
        
        outputobtained = []
        totalweight = []
        finaloutput = []
        for j in range(len(output[out])):
            count = 0
            weightsum=0
            for inp in range(0,64):
                count +=1 
                weightsum = weightsum + (x[inp]*weights[out][j][inp] )
                weightsum = round(weightsum,2)
            totalweight.append(weightsum)
            
            if weightsum > 0 :
                y = 1
                outputobtained.append(y)
            else:
                y = -1
                outputobtained.append(y)
        outputobtained = np.array(outputobtained)
        print totalweight, output[out], outputobtained
        
      
       
        for n in range(len(output[out])):
            deltaw =[]              
            if output[out][n] != outputobtained[n]:
               
                
                for m in range(0,64):
                    delta = alpha * (output[out][n] - outputobtained[n]) * inputs[inpu][m]
                    """print "deltaw is " + str(delta)
                    print "weights[0][0] on for is " + str(out),str(n),str(m)"""
                    weights[out][n][m] = delta + weights[out][n][m]
                    weights[out][n][m] =  round(weights[out][n][m],2)
                    deltaw.append(delta)
                deltaw = np.array(deltaw)
                """print deltaw"""
                
            else:
                for m in range(0,64):
                    delta = alpha * (output[out][n] - outputobtained[n]) * inputs[inpu][m]
                    """print "deltaw is " + str(delta)"""
                    weights[out][inpu][m] = delta + weights[out][inpu][m]
                    weights[out][inpu][m] = round(weights[out][inpu][m],2)
                    deltaw.append(delta)
                deltaw = np.array(deltaw)
                """print deltaw"""
                
    deltanew.append(deltaw)
    """print "deltanew is " + str(deltanew), str(len(deltanew)) """
    count2 =0
    for z in range(len(deltanew)):
        if(min(deltanew[z])==0 and max(deltanew[z])==0):
            count2 += 1
            
            if count2 == len(deltanew):
                done = True
                print "final weights for input A are " + str(inputs[0]),str(weights[0])
                print "final weights for input B are " + str(inputs[1]),str(weights[1])                 
                print "output obatined is " + str(outputobtained)
                print "target output is " + str(output[0]),str(output[1]),str(output[2]),str(output[3]),str(output[4]),str(output[5]),str(output[6])
                print "final weights of input A is " + str(inputs[0]),str(weights[0][0])
                print "final weights of input B is " + str(inputs[1]),str(weights[1][1]) 
                print "final weights of input C is " + str(inputs[2]),str(weights[2][2])
                print "final weights of input D is " + str(inputs[3]),str(weights[3][3])
                print "final weights of input E is " + str(inputs[4]),str(weights[4][4])
                print "final weights of input J is " + str(inputs[5]),str(weights[5][5])
                print "final weights of input K is " + str(inputs[6]),str(weights[6][6])
                
                break
        else:
            done = False
            continue    
    


print "Testing letters...."    


"""font 1 with noise"""
test_inputA = [[-1, -1, -1,  1,  1, -1, -1, -1, -1],
               [-1, -1, -1,  1,  1, -1, -1, -1, -1],
               [-1, -1, -1,  1, -1,  1,  1, -1, -1],
               [-1, -1,  1,  1,  1,  1,  1, -1, -1],
               [-1, -1,  1, -1,  1, -1,  1, -1, -1],
               [-1, -1,  1, -1, -1, -1,  1, -1, -1],
               [ 1, -1,  1,  1, -1,  1,  1, -1,  1]]

"""10 pixels changed"""              
test_inputA10=[[-1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1,  1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1,  1, -1,  1,  1, -1, -1],
              [-1, -1,  1, -1, -1, -1,  1, -1, -1],
              [-1, -1,  1, -1, -1, -1,  1, -1, -1],
              [-1, -1, -1,  1, -1,  1, -1,  1,  1]]

"""5 pixels changed"""              
test_inputA5=[[-1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1,  1, -1, -1, -1, -1],
              [-1, -1, -1,  1, -1,  1, -1, -1, -1],
              [-1, -1,  1,  1, -1,  1, -1, -1, -1],
              [-1, -1,  1, -1, -1, -1,  1, -1, -1],
              [-1, -1, -1, -1, -1, -1,  1, -1, -1],
              [ 1,  1,  1,  1, -1,  1, -1,  1,  1]]

"""with extra ink"""              
test_inputAink = [[-1, -1, -1, -1,  1, -1, -1, -1, -1],
                  [-1, -1, -1,  1,  1, -1, -1, -1, -1],
                  [-1, -1,  1,  1, -1,  1, -1, -1, -1],
                  [-1, -1,  1,  1,  1,  1,  1,  1, -1],
                  [-1, -1,  1, -1,  1, -1,  1, -1, -1],
                  [-1, -1,  1, -1,  1, -1,  1, -1, -1],
                  [ 1,  1,  1,  1, -1,  1,  1,  1,  1]]
  
"""font2"""         
test_inputA1 = [[-1, -1, -1, -1,  1, -1, -1, -1, -1],
               [-1, -1, -1, -1,  1, -1, -1, -1, -1],
               [-1, -1, -1,  1, -1,  1, -1, -1, -1],
               [-1, -1, -1,  1, -1,  1, -1, -1, -1],
               [-1, -1,  1,  1,  1,  1,  1, -1, -1],
               [-1, -1,  1, -1, -1, -1,  1, -1, -1],
               [-1, -1,  1, -1, -1, -1,  1, -1, -1]]    
"""font3"""
test_inputA2 = [[-1, -1, -1, -1,  1, -1, -1, -1, -1],
               [-1, -1, -1, -1,  1, -1, -1, -1, -1],
               [-1, -1, -1,  1, -1,  1, -1, -1, -1],
               [-1, -1, -1,  1, -1,  1, -1, -1, -1],
               [-1,  1,  1,  1,  1,  1,  1,  1, -1],
               [-1,  1, -1, -1, -1, -1, -1,  1, -1],
               [-1,  1,  1, -1, -1, -1,  1,  1, -1]] 
               
test_inputB1 = [[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
               [ 1, -1, -1, -1,  1, -1, -1, -1,  1],
               [ 1, -1, -1, -1, -1, -1, -1, -1,  1],
               [ 1,  1,  1,  1,  1,  1,  1,  1, -1],
               [ 1, -1, -1, -1, -1, -1, -1, -1,  1],
               [ 1, -1, -1, -1, -1, -1, -1, -1,  1],
               [ 1,  1,  1,  1,  1,  1,  1,  1, -1]] 

"""font 1 with noise"""              
test_inputB =[[-1,  1,  1,  1,  1, -1,  1,  1, -1],
              [-1, -1,  1, -1, -1, -1, -1, -1,  1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [ 1,  1,  1, -1, -1, -1,  1,  1, -1],
              [-1,  1,  1, -1,  1, -1, -1, -1,  1],
              [-1, -1, -1, -1, -1, -1, -1, -1,  1],
              [ 1,  1, -1,  1,  1, -1,  1,  1, -1]]
              
"""with noise - 10 pixels """
test_inputB10 =   [[ 1, -1,  1, -1,  1, -1,  1,  1, -1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [-1,  1, -1,  1, -1,  1, -1, -1,  1],
              [-1, -1,  1, -1,  1, -1,  1,  1, -1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [ 1,  1, -1,  1, -1,  1, -1, -1, -1]]

"""with noise - 5 pixels"""             
test_inputB5 =[[ 1,  1, -1,  1,  1,  1,  1,  1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1,  1, -1,  1, -1, -1, -1],
          [-1,  1,  1,  1,  1, -1,  1,  1, -1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [-1,  1, -1, -1, -1, -1, -1, -1,  1],
          [ 1,  1,  1,  1,  1, -1, -1,  1, -1]]

"""extra ink"""         
test_inputBink =     [[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
                      [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                      [-1,  1, -1,  1, -1,  1,  1, -1,  1],
                      [-1,  1,  1,  1,  1,  1,  1,  1,  1],
                      [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                      [ 1,  1, -1, -1, -1, -1, -1, -1,  1],
                      [ 1,  1,  1,  1,  1,  1,  1,  1, -1]]
              
"""font 1 with noise"""
test_inputC = [[-1, -1,  1,  1,  1,  1,  1,  1,  1],
               [-1,  1, -1, -1,  1, -1, -1, -1,  1],
               [ 1,  1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1],
               [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1,  1, -1, -1,  1, -1, -1, -1,  1],
               [-1, -1,  1,  1,  1,  1,  1,  1,  1]] 

               
test_inputC10 =  [[-1, -1,  1, -1,  1,  1, -1,  1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1,  1],
                  [-1, -1, -1,  1,  1, -1,  1, -1,  1]]
                  
test_inputC5 =   [[-1, -1,  1,  1,  1, -1,  1,  1,  1],
                  [-1, -1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1,  1,  1,  1, -1,  1,  1,  1]]
                  
test_inputCink = [[ 1, -1,  1,  1,  1,  1,  1,  1,  1],
                  [ 1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [ 1,  1,  1, -1, -1, -1, -1, -1, -1],
                  [ 1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1,  1,  1, -1, -1, -1, -1, -1,  1],
                  [ 1, -1,  1,  1,  1,  1,  1,  1,  1]]
               
"""font 1 with noise"""
test_inputD =[[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
              [-1,  1, -1,  1, -1, -1, -1, -1, -1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [-1,  1,  1, -1, -1, -1, -1, -1, -1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [-1,  1,  1, -1, -1, -1, -1, -1,  1],
              [ 1,  1,  1,  1,  1,  1,  1,  1, -1]]
              
test_inputD10 =  [[-1,  1,  1,  1, -1,  1, -1,  1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1, -1,  1, -1,  1, -1,  1,  1, -1]]
                  
test_inputD5 =   [[ 1, -1,  1,  1, -1,  1,  1,  1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1,  1,  1,  1, -1,  1,  1,  1, -1]]
                  
test_inputDink = [[ 1,  1,  1,  1,  1,  1,  1,  1, -1],
                  [ 1,  1, -1, -1, -1, -1,  1,  1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1,  1, -1,  1, -1,  1],
                  [ 1,  1,  1,  1,  1,  1,  1,  1, -1]]                  
              
"""font 1 with noise"""
test_inputE =[[ 1,  1, -1,  1,  1,  1,  1,  1,  1],
              [-1,  1, -1, -1, -1, -1, -1, -1,  1],
              [-1,  1, -1,  1, -1, -1, -1, -1, -1],
              [-1,  1, -1,  1,  1, -1, -1, -1, -1],
              [-1,  1, -1,  1, -1, -1, -1, -1, -1],
              [ 1,  1, -1, -1, -1, -1, -1, -1,  1],
              [ 1,  1,  1,  1,  1,  1,  1,  1,  1]]
              
test_inputE10 =  [[ 1, -1,  1, -1,  1, -1, -1,  1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1, -1,  1, -1, -1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1,  1,  1, -1,  1, -1,  1,  1]]
                  
test_inputE5 =   [[ 1,  1,  1, -1,  1,  1,  1,  1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1,  1],
                  [ 1,  1,  1,  1, -1,  1,  1, -1,  1]]
                  
test_inputEink = [[ 1,  1,  1,  1,  1,  1,  1,  1,  1],
                  [-1,  1, -1,  1, -1, -1, -1, -1,  1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1,  1,  1, -1, -1, -1, -1, -1],
                  [ 1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [ 1,  1, -1,  1, -1,  1, -1, -1,  1],
                  [ 1,  1,  1,  1,  1,  1,  1,  1,  1]]
              
"""font 1 with noise"""
test_inputJ =[[-1, -1, -1, -1,  1,  1, -1, -1,  1],
              [-1, -1, -1, -1, -1,  1,  1, -1, -1],
              [-1, -1, -1, -1, -1,  1,  1, -1, -1],
              [-1, -1, -1, -1, -1,  1,  1, -1, -1],
              [-1,  1,  1, -1, -1,  1, -1, -1, -1],
              [-1, -1, -1,  1, -1,  1,  1, -1, -1],
              [-1, -1, -1,  1,  1,  1, -1, -1,  1]]
              
test_inputJ5 =  [[-1, -1, -1, -1,  1, - 1, -1,  1,  1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1,  1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1, -1,  1,  1, -1, -1, -1, -1]]             
              

test_inputJink = [[-1, -1,  1,  1,  1,  1,  1,  1,  1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1,  1, -1, -1, -1,  1, -1, -1],
                  [-1, -1, -1, -1, -1, -1,  1, -1, -1],
                  [-1, -1,  1, -1,  1, -1,  1, -1, -1],
                  [-1, -1,  1, -1, -1,  1,  1, -1, -1],
                  [-1, -1,  1,  1,  1,  1, -1, -1, -1]]

          
"""font 1 with noise"""
test_inputK =[[ 1, -1,  1, -1, -1,  1,  1,  1, -1],
              [-1,  1, -1, -1,  1, -1, -1, -1, -1],
              [-1,  1, -1,  1, -1, -1, -1, -1, -1],
              [-1,  1,  1, -1, -1, -1, -1, -1, -1],
              [-1,  1, -1,  1,  1,  1, -1, -1, -1],
              [-1,  1,  1, -1,  1, -1, -1, -1, -1],
              [ 1,  1, -1, -1, -1,  1,  1, -1, -1]]
              
test_inputK5 =  [[ 1,  1,  1, -1, -1,  1,  1, -1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1,  1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1, -1, -1, -1, -1, -1, -1, -1],
                  [ 1, -1,  1, -1, -1,  1,  1, -1, -1]]
          
          
test_inputKink = [[ 1,  1,  1, -1, -1,  1,  1, -1, -1],
                  [ 1,  1, -1,  1,  1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1,  1, -1, -1, -1, -1, -1, -1],
                  [-1,  1, -1,  1, -1, -1, -1, -1, -1],
                  [-1,  1,  1,  1,  1, -1, -1, -1, -1],
                  [ 1,  1,  1, -1, -1,  1,  1,  1, -1]]          

test_F = [[ 1,  1, 1,  1, 1,  1, 1,  1, 1],
          [ 1,  1,-1,  1,-1, -1,-1, -1, 1],
          [ 1, -1,-1, -1,-1, -1,-1, -1,-1],
          [ 1,  1, 1,  1, 1, -1,-1, -1,-1],
          [ 1, -1,-1, -1,-1, -1,-1, -1,-1],
          [ 1, -1,-1, -1,-1, -1,-1, -1,-1],  
          [ 1,  1,-1, -1,-1, -1,-1, -1,-1]]


def test_perceptron(test_input):
    
    test_weights = []
    test_weights.append(weights[0][0])
    test_weights.append(weights[1][1])
    test_weights.append(weights[2][2])
    test_weights.append(weights[3][3])
    test_weights.append(weights[4][4])
    test_weights.append(weights[5][5])
    test_weights.append(weights[6][6])
    """print test_weights"""
    
    x_in = []
    for j in range(0,7):
        for k in range(0,9):
            x2 = test_input[j][k]
            x_in.append(x2)
    x_in.append(bias)
    """print x_in"""
    
    testtotalweight = []
    testoutput = []
    for j in range(len(test_weights)):
            count = 0
            testweightsum=0
            for inps in range(0,64):
                count +=1 
                testweightsum = testweightsum + (x_in[inps]*test_weights[j][inps] )
                testweightsum = round(testweightsum,2)
            testtotalweight.append(testweightsum)
           
            
            if testweightsum > 0 :
                y = 1
                """print j"""
            else:
                y = -1
                """print j"""
                
            if y == 1 and j==0:
                print "The letter is A"
            elif (y==1 and j==1) :
                print "The letter is B"
            elif (y==1 and j==2) :
                print "The letter is C"
            elif (y==1 and j==3) :
                print "The letter is D"
            elif (y==1 and j==4) :
                print "The letter is E"
            elif (y==1 and j==5) :
                print "The letter is J"
            elif (y==1 and j==6) :
                print "The letter is K" 
           
               
    for f in range(len(test_input)):
         for g in range(len(test_input[f])):
                    
                if(test_input[f][g] == 1):
                    print test_input[f][g],
                else:
                    print " ",
         print
    
   
          
print "Testing for A ..... "
print "Testing A with more than 50 % noise "                         
test_perceptron(test_inputA)
print "testing A with noise - 10 pixels"
test_perceptron(test_inputA10)
print "testing A with noise - 5 pixels"
test_perceptron(test_inputA5)
print "testing A with extra ink"
test_perceptron(test_inputAink)
print
print "Testing for B ..... "
print "Testing B with more than 50 % noise " 
test_perceptron(test_inputB)
print "testing B with noise - 10 pixels"
test_perceptron(test_inputB10)
print "testing B with noise - 5 pixels"
test_perceptron(test_inputB5)
print "testing B with extra ink"
test_perceptron(test_inputBink)
print 
print "Testing for C ..... "
print "Testing C with more than 50 % noise " 
test_perceptron(test_inputC)
print "testing C with noise - 10 pixels"
test_perceptron(test_inputC10)
print "testing C with noise - 5 pixels"
test_perceptron(test_inputC5)
print "testing C with extra ink"
test_perceptron(test_inputCink)
print
print "Testing for D ..... "   
print "Testing D with more than 50 % noise "
test_perceptron(test_inputD)
print "testing D with noise - 10 pixels"
test_perceptron(test_inputD10)
print "testing D with noise - 5 pixels"
test_perceptron(test_inputD5)
print "testing D with extra ink"
test_perceptron(test_inputDink)
print 
print "Testing for E ..... "
print "Testing E with more than 50 % noise "
test_perceptron(test_inputE)
print "testing E with noise - 10 pixels"
test_perceptron(test_inputE10)
print "testing E with noise - 5 pixels"
test_perceptron(test_inputE5)
print "testing E with extra ink"
test_perceptron(test_inputEink)
print
print "Testing for J ..... "
print "Testing J with more than 50 % noise "
test_perceptron(test_inputJ) 
print "testing J with noise - 5 pixels"
test_perceptron(test_inputJ5)
print "testing J with extra ink"
test_perceptron(test_inputJink)
print  
print "Testing for K ..... "
print "Testing K with more than 50 % noise "
test_perceptron(test_inputK) 
print "testing K with noise - 5 pixels"
test_perceptron(test_inputK5)
print "testing K with extra ink"
test_perceptron(test_inputKink)    
print "testing with letter other than A,B,C,D,E,J,K. The result is" 
test_perceptron(test_F)      
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

        

      
          

      
    
