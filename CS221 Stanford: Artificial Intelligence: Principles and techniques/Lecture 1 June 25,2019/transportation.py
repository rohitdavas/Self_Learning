### Search problem (modeling)
#problem statement - 

'''Street with blocks numbered 1 to n. Walking from s to s + 1 takes 1 minute. Taking a magic tram from s to 2s takes 2 minutes.
How to travel from 1 to n in the least time? '''

class SearchProblem(object):
    def startState(self):
        raise NotImplementedError

    def isEnd(self, state):
        # return boolean if state is end or not
        raise NotImplementedError

    def succAndCost(self, state):
        # return list of (action, newState, cost)
        raise NotImplementedError

class TransportationProblem(SearchProblem):
    def __init__(self, N):
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def succAndCost(self, state):
        result = []
        print(state)
        if state + 1 <= self.N:
            result.append(('walk', state + 1, 1))
        if 2 * state <= self.N:
            result.append(('tram', 2 * state, 2))
        return result


problem = TransportationProblem(400)
print problem.succAndCost(4)
print problem.succAndCost(25)