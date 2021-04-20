import sys
import math
import copy
from alphabetaAlgorithm import alphabeta

class Node:
    def __init__(self, depth, tokens, token,parent):
        self.parent = parent
        self.token = token
        self.score = None
        self.depth = depth
        self.tokens = tokens
        self.children = self.generate_children()
       
    def generate_children(self):
        children = list()
        if self.token == None:
            for i in range(len(self.tokens)):
                if self.tokens[i]<(len(self.tokens)/2) and self.tokens[i] % 2 == 1:
                    new_list = copy.deepcopy(self.tokens)
                    new_list.remove(self.tokens[i])
                    children.append(Node(self.depth+1, new_list, self.tokens[i], self))
        else:
            for i in range(len(self.tokens)):
                if self.is_multiple_or_factor(self.token, self.tokens[i]):
                    new_list = copy.deepcopy(self.tokens)
                    new_list.remove(self.tokens[i])
                    children.append(Node(self.depth+1, new_list, self.tokens[i],self))
        return children

    def is_terminal(self):
        return len(self.children) == 0

    def is_prime(self, token):
        if token < 2:
            return False
        return all(token % i for i in range(2, token))

    def get_score(self, isMaxPlayer):
        if self.is_terminal():
            score = -1.0
        else:
            if 1 in self.tokens:
                return 0
    
            elif self.token == 1:
                if len(self.children) % 2 == 1:
                    score = 0.5
                else:
                    score = -0.5    

            elif self.is_prime(self.token):
                if self.count_prime_succession(self.token)%2 == 1:
                    score = 0.7
                else:
                    score = -0.7
            else:
                if self.count_prime_succession(self.largest_prime_factor())%2 == 1:
                    score = 0.6
                else:
                    score = -0.6
        
                   
        if isMaxPlayer:
            self.score = score
        else:
            self.score = -score
                    
        return self.score
        
    def largest_prime_factor(self):
        temp = self.token
        while not temp == 0:
            if self.is_prime(temp) and self.token % temp == 0:
                break
            temp -= 1
        return temp

    def count_prime_succession(self, prime_token):  
        succession = self.children
        count = 0
        for child in succession:
            if child.token % prime_token == 0:
                count = count + 1       
        return count

    def is_multiple_or_factor(self,token, possibleToken):
        if token == 1 or possibleToken == 1:
            return True
        if token % possibleToken == 0:
            return True
        if possibleToken % token == 0:
            return True
        else:
            return False
        
if __name__ == '__main__':
    # Get input
    num_tokens = int(sys.argv[1])
    num_taken_tokens = int(sys.argv[2])
    taken_tokens = list()
    for i in range(num_taken_tokens):
        taken_tokens.append(int(sys.argv[3+i]))
    max_depth = int(sys.argv[-1])

    # Gets the last token that was taken
    token = None if num_taken_tokens == 0 else int(sys.argv[-2])

    # Create list of tokens
    all_tokens = list()
    for i in range(1, num_tokens+1):
        all_tokens.append(i)
    
    # Remove tokens that have already been taken
    all_tokens = (list(list(set(all_tokens)-set(taken_tokens)) + list(set(taken_tokens)-set(all_tokens))))
    
    # Create a node with the input information
    root_node = Node(0,all_tokens, token,None)
    ab = alphabeta(max_depth)
    score, node = ab.run(root_node, max_depth , -math.inf, math.inf, num_taken_tokens%2==0 )

    smallest_move = math.inf
    for child in root_node.children:
        if child.score == score and child.token < smallest_move:
            smallest_move = child.token
    
    a = open("PNT_analysis.txt", "w")
    a.write("\n\ninput: "+str(sys.argv))
    a.write("\nMove: "+ str(smallest_move))
    a.write("\nValue: "+str(score))
    a.write("\nNumber of Nodes Visited: " + str(ab.visited_nodes_count))
    a.write("\nNumber of Nodes Evaluated: "+ str(ab.evaluated_nodes_count))
    a.write("\nMax Depth Reached: "+ str(ab.max_depth_reached))
    a.write("\nAvg Effective Branching Factor: " + str(round(((ab.visited_nodes_count-1)/(ab.visited_nodes_count-ab.evaluated_nodes_count)), 1))+"\n")