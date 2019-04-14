#!/usr/bin/env python
# coding: utf-8

# In[1]:

import time
import sys


'''reading the sudoku problem from file'''

count = 0

def read_problem(arq):

    arq = open(arq, 'r')
    sudoku = arq.readlines()

    N = int(sudoku[0])

    grid = {}
    for i in range(N):
        grid[i] = []

    begin = 1
    end = 10
    for j in range(N):
        for i in range(begin, end):
            grid[j].append(sudoku[i].split())
        begin = end
        end = end + 9

    arq.close()
    
    return grid


def show_grid(grid):
    for i in range(len(grid)):          
        print(grid[i])

def show_grids(grid):
        
    for j in range(len(grid)):
        for i in range(len(grid[j])):          
            print(grid[j][i])
        print("\n")
    


# In[2]:


'''generate the list with the blank spaces of the grid '''

def empty_list(grid):
    
    empty = {}
    k = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == "0"):
                empty[k] = [i,j]
                k = k + 1
            
    return empty
    


# In[3]:


'''verification of lin, col, subgrids'''

def check_lin(grid, i, chosen):
    
    if(chosen in grid[i]):
        return False
    else:
        return True
    
def check_col(grid, j, chosen):
    
    for i in range(len(grid)):
        if(chosen == grid[i][j]):
            return False
    
    return True

def check_subgrid(grid, i, j, chosen):
    
    subl = i - i%3
    subc = j - j%3
    aux = subc    
        
    for subl in range(subl, subl+3):
        for subc in range(subc, subc+3):
            if(grid[subl][subc] == chosen):
                return False
         
        subc = aux
        
    return True

# In[4]:


'''foward verification functions'''

def ver_values_lin(grid, i, pvalues):
    
    newpvalues = []
    
    for j in range(len(pvalues)):
        if(pvalues[j] not in grid[i]): 
            newpvalues.append(pvalues[j])
            
                
    newpvalues = [x for x in pvalues if x in newpvalues] 
    
    return newpvalues

def ver_values_col(grid, j, pvalues):
    
    col_values = []
    newpvalues = []
    
    for k in range(len(grid)):
        col_values.append(grid[k][j])
        
    for i in range(len(pvalues)):
        if(pvalues[i] not in col_values):
            newpvalues.append(pvalues[i])
    
    newpvalues = [x for x in pvalues if x in newpvalues]
        
    return newpvalues

def ver_values_subgrid(grid, lin , col, pvalues):
    
    subl = lin - lin%3
    subc = col - col%3
    aux = subc  
    
    newpvalues = []
    subgrid_values = []
    
    for subl in range(subl, subl+3):
        for subc in range(subc, subc+3):
            subgrid_values.append(grid[subl][subc])
        subc = aux
                    
    for i in range(len(pvalues)):
        if(pvalues[i] not in subgrid_values):
            newpvalues.append(pvalues[i])
        
    newpvalues = [x for x in pvalues if x in newpvalues]
    
    return newpvalues
        

def foward_verification(grid, spoti, spotj):
    
    tvalues = {}
          
        
    pvalues = ["1","2","3","4","5","6","7","8","9"]
        
    pvalues = ver_values_lin(grid, spoti, pvalues)
    pvalues = ver_values_col(grid , spotj, pvalues)
    pvalues = ver_values_subgrid(grid, spoti , spotj, pvalues)
            
    return pvalues


# In[5]:


''' mvs algorithm '''

def mvs(grid, empty):
    
    spoti = 0
    spotj = 0
    
    min = foward_verification(grid, empty[0][0], empty[0][1])
    spoti = empty[0][0]
    spotj = empty[0][1]
    
    for i in range(1, len(empty)):
        aux = foward_verification(grid, empty[i][0], empty[i][1])
        if(len(min) > len(aux)):
            min = foward_verification(grid, empty[i][0], empty[i][1])
            spoti = empty[i][0]
            spotj = empty[i][1]
            
    return min, spoti, spotj
    


# In[6]:


''' backtrack with flags, heur values = None, fv, mvs  '''

def backtrack(grid, heur):
    
    global count
    
    empty = empty_list(grid)
    
    if (empty == {}):
        return True
            
    spoti, spotj = empty[0][0], empty[0][1]
    
    if(heur == "fv"):
        pvalues = foward_verification(grid, spoti, spotj)
        if(pvalues == []):
            return False
    elif(heur == "mvs"):
        pvalues, spoti, spotj = mvs(grid, empty)
        if(pvalues == []):
            return False
    
    begin = 0
    end = 0
    if(heur == "fv" or heur == "mvs"):
        begin = 0
        end = len(pvalues)
    else:
        begin = 1
        end = 10

    for i in range(begin,end):
        
        count = count + 1

        if(count > 10**6):
        	return "Número de atribuições excede limite máximo!"
        
        if(heur == "fv" or heur == "mvs"):
            chosen = str(pvalues[i])
        else:
            chosen = str(i)
        
        
        if(check_lin(grid, spoti, chosen) == True and check_col(grid, spotj, chosen) == True and   
           check_subgrid(grid, spoti, spotj, chosen) == True):

            grid[spoti][spotj] = chosen

            result = backtrack(grid, heur)

            if(result == False):
                grid[spoti][spotj] = "0"
            else:
                return True
        

    return False    


# In[7]:


''' calls backtrach for each sudoku problem '''

def solve_sudoku(arq, heur):
    
    global count

    grid = read_problem(arq)

    out = open(arq + "_solution", "w")
    out.write(str(len(grid)))
    out.write("\n")
    
    for i in range(len(grid)):
        
        inicio = time.time()
        count = 0
        print("\n")
        show_grid(grid[i])
        backtrack(grid[i], heur)
        print("\n" + "Quantidade de atribuições do Sudoku " + str(i+1) + ": " + str(count) + "\n")
        show_grid(grid[i])
        fim = time.time()
        print("\n" + "Tempo: " + str(fim - inicio))
        print("\n" + "-----------------------------------------------")

        write_solution(grid[i], out)

    out.close()

''' write result on txt '''

def write_solution(grid, out):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if(j == len(grid) - 1):
				out.write(str(grid[i][j]))
			else:
				out.write(str(grid[i][j]) + " ")
		out.write("\n")
        
''' main '''

if __name__ == "__main__":
    arq = sys.argv[1]
    heur = sys.argv[2]
        
    solve_sudoku(arq, heur)


