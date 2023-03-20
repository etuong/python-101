import networkx as nx
import numpy as np


class PlayoffElimination:
    def __init__(self, filename):
        # Read in all the lines in the text file
        with open(filename, 'r') as f:
            data = f.readlines()

        n = int(data[0].strip())
        self.number_of_teams = n
        self.teams = []
        self.wins = []
        self.losses = []
        self.remaining = []

        # Bracket of games is always a square
        self.g = np.arange(n ** 2).reshape(n, n)

        for i in range(n):
            team = data[i + 1].split()
            self.teams.append(team[0])
            self.wins.append(int(team[1]))
            self.losses.append(int(team[2]))
            self.remaining.append(int(team[3]))
            for j in range(n):
                self.g[i][j] = int(team[j + 4])

    def isEliminated(self, team):
        team_index = self.teams.index(team)
        number_of_teams = self.number_of_teams

        # Scenario 1: Trivial Elimination
        for i in range(number_of_teams):
            # The same team does not play with itself
            a = i != team_index

            # Does the current team stand a chance against the team with the most wins?
            b = self.wins[team_index] + \
                self.remaining[team_index] < self.wins[i]

            # If not, return that first team with the most wins
            if a & b:
                return self.teams[i]

        # Scenario 2
        directed_graph = nx.DiGraph()

        # Add the source and sink nodes
        directed_graph.add_node('s')
        directed_graph.add_node('t')

        for i in range(number_of_teams):
            if i != team_index:
                team_capacity = self.wins[team_index] + \
                    self.remaining[team_index] - self.wins[i]
                directed_graph.add_node(i)
                directed_graph.add_edge(i, 't', capacity=team_capacity)
                for j in range(i + 1, number_of_teams):
                    if j != team_index:
                        i_to_j = '{}-{}'.format(i, j)
                        directed_graph.add_node(i_to_j)
                        directed_graph.add_edge(
                            's', i_to_j, capacity=self.g[i][j])
                        directed_graph.add_edge(
                            i_to_j, i, capacity=float('inf'))
                        directed_graph.add_edge(
                            i_to_j, j, capacity=float('inf'))

        # Find all the team nodes on the source-side of the min-cut so
        # we can fully deduce the cause of a team’s elimination.
        min_cut = nx.minimum_cut(directed_graph, 's', 't')[1]
        nodes = []
        if 's' in min_cut[0]:
            for i in min_cut[0]:
                if type(i) == int:
                    nodes.append(i)
        else:
            for i in min_cut[1]:
                if type(i) == int:
                    nodes.append(i)
        R = []
        for i in nodes:
            R.append(self.teams[i])
        return R

    def start(self):
        for team in self.teams:
            R = self.isEliminated(team)
            if R:
                if type(R) == list:
                    R = ' '.join(R)
                    print(f'{team} is eliminated')
                else:
                    print(f'{team} has been trivially eliminated by {R}')
            else:
                print('{} is not eliminated'.format(team))


if __name__ == '__main__':
    playoff = PlayoffElimination('world_cup.txt')
    playoff.start()
