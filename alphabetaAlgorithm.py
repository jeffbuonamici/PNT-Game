import sys
import math


class alphabeta:
    def __init__(self,max_depth):
        self.max_depth_reached = 0
        self.max_depth = max_depth
        self.visited_nodes_count = 0
        self.evaluated_nodes_count = 0
        self.best_move = None
        self.best_score = 0

    def run(self, node, depth, alpha, beta, maximizingPlayer):
        self.visited_nodes_count += 1

        if (self.max_depth != 0 and depth == 0 ) or node.is_terminal():
            self.evaluated_nodes_count += 1
            temp = node.get_score(maximizingPlayer)
            node.score = temp
            return temp, node

        # maxmizingPlayer always wants to return max value
        if maximizingPlayer:
            maxEval = -math.inf
            for child in node.children:
                if child.depth > self.max_depth_reached:
                    self.max_depth_reached = child.depth 
                eval, move = self.run(child, depth - 1, alpha, beta, False)
                child.score = eval
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval, move

        # minimizingPlayer always wants to return min value
        else:
            minEval = math.inf
            for child in node.children:
                if child.depth > self.max_depth_reached:
                    self.max_depth_reached = child.depth 
                eval, move = self.run(child, depth - 1, alpha, beta, True)
                child.score = eval
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval, move

