import sys
import math

class Node:
    def __init__(self, tokens, depth, parent):
        self.tokens = tokens
        self.depth = depth
        self.parent = parent
    
    def get_children(self):
        # Return children
        return None

    def is_terminal(self):
        return len(self.get_children()) == 0



def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal():
        # Return score
        return None

    # maxmizingPlayer always wants to return max value
    if maximizingPlayer:
        maxEval = -math.inf
        for child in node.get_children():
            eval = alphabeta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    # minimizingPlayer always wants to return min value
    else:
        minEval = math.inf
        for child in node.get_children():
            eval = alphabeta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                breakpoint
        return minEval



if __name__ == '__main__':
    # Get input
    num_tokens = int(sys.argv[1])
    num_taken_tokens = int(sys.argv[2])
    taken_tokens = set()
    for i in range(num_taken_tokens):
        taken_tokens.add(int(sys.argv[3+i]))
    depth = int(sys.argv[-1])

    # Create list of tokens
    all_tokens = set()
    for i in range(1, num_tokens):
        all_tokens.add(i)
    
    # Remove tokens that have already been taken
    all_tokens = all_tokens.difference(taken_tokens)

