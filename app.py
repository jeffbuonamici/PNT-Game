import sys
import math
import copy
from alphabetaAlgorithm import alphabeta

class Node:
    def __init__(self, tokens, lastTokenTaken, parent):
        self.tokens = tokens
        self.lastTokenTaken = lastTokenTaken
        self.parent = parent
        open("PNT_analysis.txt", "w")
       
    def get_children(self, printing = False):
        children = list()
        #print(self.tokens)
        if self.lastTokenTaken == None:
            for i in range(len(self.tokens)):
                if self.tokens[i]<(len(self.tokens)/2) and self.tokens[i] % 2 == 1:
                    new_list = copy.deepcopy(self.tokens)
                    new_list.remove(self.tokens[i])
                    children.append(Node(new_list, self.tokens[i], self))
        else:
            for i in range(len(self.tokens)):
                if printing:
                    print ("last: "+str(self.lastTokenTaken)+" , token: "+str(self.tokens[i])+" , multiple: "+str(is_multiple_or_factor(self.lastTokenTaken, self.tokens[i])))
                if is_multiple_or_factor(self.lastTokenTaken, self.tokens[i]):
                    new_list = copy.deepcopy(self.tokens)
                    new_list.remove(self.tokens[i])
                    children.append(Node(new_list, self.tokens[i], self))
                # Return children
        return children

    def is_terminal(self):
        return len(self.get_children()) == 0

    def is_prime(self, token):
        if int(token) < 2:
            return False
        return all(int(token) % i for i in range(2, int(token)))

    def get_score(self, isMaxPlayer):
        if self.is_terminal():
            score = 1.0
        else:
            if 1 in self.tokens:
                return 0
    
            elif self.lastTokenTaken == 1:
                if len(self.get_children()) % 2 == 1:
                    score = 0.5
                else:
                    score = -0.5    

            elif self.is_prime(self.lastTokenTaken):
                if self.count_prime_succession(self.lastTokenTaken)%2 == 1:
                    score = 0.7
                else:
                    score = -0.7
            else:
                if self.count_prime_succession(self.largest_prime_factor())%2 == 1:
                    score = 0.6
                else:
                    score = -0.6
                
        if isMaxPlayer:
            return score
        else:
            return score * -1.0
    
    def largest_prime_factor(self):
        temp = int(self.lastTokenTaken)
        while not temp == 0:
            if self.is_prime(temp) and self.lastTokenTaken % temp == 0:
                break
            temp -= 1
        return temp

    def count_prime_succession(self, prime_token):  
        succession = self.get_children()
        count = 0
        for child in succession:
            if int(child.lastTokenTaken) % int(prime_token) == 0:
                count = count + 1       
        return count

def is_multiple_or_factor(lastTokenTaken, possibleToken):
    if int(lastTokenTaken) % int(possibleToken) == 0:
        return True
    if int(possibleToken) % int(lastTokenTaken) == 0:
        return True
    else:
        return False

def list_diff(list1, list2):
    return (list(list(set(list1)-set(list2)) + list(set(list2)-set(list1))))
    
if __name__ == '__main__':
    # Get input
    num_tokens = int(sys.argv[1])
    num_taken_tokens = int(sys.argv[2])
    taken_tokens = list()
    for i in range(num_taken_tokens):
        taken_tokens.append(int(sys.argv[3+i]))
    max_depth = int(sys.argv[-1])

    # Gets the last token that was taken
    lastTokenTaken = None if num_taken_tokens == 0 else int(sys.argv[-2])

    # Create list of tokens
    all_tokens = list()
    for i in range(1, num_tokens+1):
        all_tokens.append(i)
    
    # Remove tokens that have already been taken
    all_tokens = list_diff(all_tokens,taken_tokens)
    
    # Create a node with the input information
    node = Node(all_tokens, lastTokenTaken, None)

    # Check if it is first move or not
    if num_taken_tokens == 0:
        isFirstMove = True
    else:
        isFirstMove = False
    children = (node.get_children())
    ab = alphabeta(max_depth,num_taken_tokens%2==0)
    score, node = ab.run(node, 0 , -math.inf, math.inf, num_taken_tokens%2==1 )
    a = open("PNT_analysis.txt", "a")
    a.write("Move: "+ str(ab.best_move.lastTokenTaken))
    a.write("\nValue: "+score)
    a.write("\nNumber of Nodes Visited: " + str(ab.visited_nodes_count))
    a.write("\nNumber of Nodes Evaluated: "+ str(ab.evaluated_nodes_count))
    a.write("\nMax Depth Reached: "+ str(ab.max_depth_reached))
    a.write("\nAvg Effective Branching Factor: ")

    
    