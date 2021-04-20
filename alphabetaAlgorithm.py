import sys
import math


class alphabeta:
    def __init__(self,max_depth,max_player):
        self.max_depth_reached = 0
        self.max_depth = max_depth
        self.visited_nodes_count = 0
        self.evaluated_nodes_count = 0
        self.max_player = max_player 
        self.best_move = None
        self.best_score = 0

    def run(self, node, depth, alpha, beta, maximizingPlayer):
        self.max_depth_reached = max(self.max_depth_reached, depth)
        self.visited_nodes_count += 1
        if ((self.max_depth_reached == self.max_depth) and not self.max_depth == 0 ) or node.is_terminal():
            self.evaluated_nodes_count += 1
            self.best_score
            return node.get_score(maximizingPlayer), self.best_move

        # maxmizingPlayer always wants to return max value
        if maximizingPlayer:
            maxEval = -math.inf
            bestMove = None
            for child in node.get_children():
                eval, oldChild = self.run(child, depth + 1, alpha, beta, False)
                if eval>self.best_score:
                    bestMove = child
                    self.best_move = child
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval, bestMove

        # minimizingPlayer always wants to return min value
        else:
            minEval = math.inf
            bestMove = None
            for child in node.get_children():
                eval, oldChild = self.run(child, depth + 1, alpha, beta, True)
                if eval< self.best_score:
                    bestMove = child
                    self.best_score = eval
                    self.best_move = child
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval, bestMove

