import sys

class Node:
    def __init__(self, tokens, depth, parent):
        self.tokens = tokens
        self.depth = depth
        self.parent = parent
    


def alphabeta(node, depth):
    return None


def max_value(node, depth, alpha, beta):
    return None

def min_value(node, depth, alpha, beta):
    return None







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

