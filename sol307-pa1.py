import math
def binarySearch(L,v):
    count = 0 #init depth counter to 0
    ret = False #init return store to false
    midpoint = 99 #Dummy init
    while (midpoint > 0) and (ret == False):
        midpoint = int(len(L) / 2)
        if L[midpoint] == v:
            ret = (True, count)
        else:
            if (L[midpoint] < v):
                L = L[midpoint + 1:] #this function says take all the elements after the midpoint'th element inclusive which is why we add 1
                count += 1
            else:
                L = L[:midpoint] #This says take all the elements up to the midpoint'th element not inclusive which is why we do not need to subtract 1
                count +=1

    if ret == False:
        return (False, count)
    else:
        return ret

def mean(L):
    total = 0.0 #Initialize to floating point
    for i in L: #Iterates through each element in the list L
        total += i #Adds the current list element to the total counter
    return total/len(L) #Returns the total divided by the number of elemens | Mean

def median(L):
    if len(L)%2 == 0: #Case where list has an even number of elemements
        total = L[len(L)/2] + L[(len(L)/2) -1] #Takes the two elements in the middle of the list and sums them
        return total / 2.0 #Takes the sum of the two elements in the middle of the list and returns their average
    else: #Case where list has an odd number of elements
        return L[len(L)/2] #Returns the element in the middle of the list.

A = [4, [10, [33, [2, [3],[4]]], [2]], [3], [14, [12]], [1,[3,[37],[42]]]]
def bfs(tree,elem): #approach essentially uses the input list(tree) as a queue. Children are extracted and appended to the end of the lists.
    while tree: #Runs until the queue(tree) is empty
        val = tree.pop(0) #Take the first element of the tree
        if type(val) == int: #Check to see if it is an int or a list
            print str(val)
            if val == elem: #If int check to see if it matches the element being searched for
                return True #Return true
        else: #else it is a list
            print str(val[0])
            if val[0] == elem: #Each list first element is the parent. Check to see if the parent is equal to elem
                return True #Return true if it is
            for i in val[1:]: #Take the CDR of the current list and append to the tree. Essentially enqueing the children to the end of the list
                tree.append(i) #append the children of the node to the end of the queue.
    return False #elem was not found during the BFS

def dfs(tree,elem): #approach essentially uses the input list(tree) as a queue. Children are extracted and appended to the end of the lists.
    while tree: #Runs until the queue(tree) is empty
        val = tree.pop(0) #Takes the first element of the queue(tree) out of the list.
        if type(val) == int: #Checks to see if it is an int or a list
            print val #prints value before evaluation
            if val == elem: #checks to see if the value is equal to the sought element
                return True
        else: #its a list
            print val[0] #prints value before evaluation
            if val[0] == elem: #Checks to see if the parent node value is equal to the sought element
                return True
            val = val[1:] #takes the cdr since the first was already checked
            val.reverse() #reverses the list to make it easier to prepend it to the queue
            #effectively prioritizing the children of the node currently visited at so that the search goes deep
            for i in val: #iterates trhough the children of the parent node
                tree.insert(0,i) #prepends the childrend to the queue(tree)
    return False

#print dfs(A,42)

class TTTBoard:
    """A Tic Tac Toe Board"""
    def __init__(self):
        self.data = ['*','*','*','*','*','*','*','*','*']
    def __str__(self):
        string = ""
        count = 0;
        for i in self.data:
            if count%3 is not 0:
                string += str(i) + " "
                count +=1
            else:
                string += "\n" + str(i) + " "
                count+=1
        return string
    def makeMove(self, player, pos):
        self.data[pos] = player
    def hasWon(self,player):
        winning = [[0,1,2],[0,3,6],[3,4,5],[1,4,7],[6,7,8],[2,5,8],[0,4,8],[6,4,2]]
        for i in winning:
            if player in [self.data[x] for x in i]:
                if '*' not in [self.data[x] for x in i]: #uses the predefined winning combination indices to see if the values are all non '*' as that could lead to false conclusion of game over
                    if (self.data[i[0]] == self.data[i[1]] == self.data[i[2]]): #Checks to see if the non '*' charachters are all matching
                        return True #Returns true if the winning locations match.
        return False
    def gameOver(self):
        winning = [[0,1,2],[0,3,6],[3,4,5],[1,4,7],[6,7,8],[2,5,8],[0,4,8],[6,4,2]]
        if '*' not in self.data: #if "*" is absent that means that the board is full
            return True #Return true. Game over. Board is full
        for i in winning:
            if '*' not in [self.data[x] for x in i]: #uses the predefined winning combination indices to see if the values are all non '*' as that could lead to false conclusion of game over
                if (self.data[i[0]] == self.data[i[1]] == self.data[i[2]]): #Checks to see if the non '*' charachters are all matching
                    return True #Returns true if the winning locations match.
        return False #Returns false if the board is not full and there is no winning matching
    def clear(self):
        self.data = ['*','*','*','*','*','*','*','*','*']

import string
import random

test = TTTBoard()
#print test
test.makeMove('O', 0)
test.makeMove('X', 1)
test.makeMove('O', 2)
test.makeMove('O', 5)
test.makeMove('O', 8)
print test.hasWon('O')
print test
#for i in range(0,8):
#    test.makeMove(random.choice(string.letters),i)

#print test.gameOver()
#print test
#str(test)