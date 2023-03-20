from itertools import chain

import networkx as nx

# Read in the file input
with open('mlb.txt', 'r') as fin:
    data = fin.read().splitlines(True)

# Strip each team
stripped = (line.strip('\n') for line in data[1:])

# In each team, split its information
lines = (line.split() for line in stripped if line)

# Number of teams
teams = int(data[0])

# Get the team's wins and remaining games
rows = list(lines)
wins = [int(row[1]) for row in rows]
remain = [int(row[3]) for row in rows]

eliminated = []
max_wins = max(wins)
leader = []

# Scenario #1: Trivial Elimination
# Loop through every team and grab the leading teams with the most wins
for team in range(teams):
    if wins[team] == max_wins:
        leader.append(team)

if (sum(remain) == 0):
    for team in range(teams):
        eliminated.append(team)
    for team in range(len(leader)):
        eliminated.remove(leader[team])
    for team in eliminated:
        print(team, end=" ")
else:
    team = 0
    n = 5
    layer1_values = []
    for team in range(teams - 1):
        y = rows[team]
        layer1_values.append(y[n:])
        n = n + 1
    Layer1_capacities = list(chain.from_iterable(layer1_values))
    layer_id = 'L1'
    layer_1_ids = []
    for team in range(0, len(Layer1_capacities)):
        node_id = layer_id + str(team)
        layer_1_ids.append(node_id)
    layer_id = 'L2'
    layer_2_ids = []
    for team in range(0, teams):
        node_id = layer_id + str(team)
        layer_2_ids.append(node_id)

    def ford_fulkerson(graph, source, sink, i):
        flow, path = 0, True

        while path:
            # search for path with flow reserve
            path, reserve = depth_first_search(graph, source, sink)
            flow += reserve

            # increase flow along the path
            for v, u in zip(path, path[1:]):
                if graph.has_edge(v, u):
                    graph[v][u]['flow'] += reserve
                else:
                    graph[u][v]['flow'] -= reserve

        the_Sum = sum(Layer1_capacities)
        if flow != the_Sum:
            eliminated.append(i)

    def depth_first_search(graph, source, sink):
        undirected = graph.to_undirected()
        explored = {source}
        stack = [(source, 0, dict(undirected[source]))]

        while stack:
            v, _, neighbours = stack[-1]
            if v == sink:
                break

            # search the next neighbour
            while neighbours:
                u, e = neighbours.popitem()
                if u not in explored:
                    break
            else:
                stack.pop()
                continue

            # current flow and capacity
            in_direction = graph.has_edge(v, u)
            capacity = e['capacity']
            flow = e['flow']
            neighbours = dict(undirected[u])

            # increase or redirect flow at the edge
            if in_direction and flow < capacity:
                stack.append((u, capacity - flow, neighbours))
                explored.add(u)
            elif not in_direction and flow:
                stack.append((u, flow, neighbours))
                explored.add(u)

        # (source, sink) path and its flow reserve
        reserve = min((f for _, f, _ in stack[1:]), default=0)
        path = [v for v, _, _ in stack]

        return path, reserve

    for n in range(0, teams):
        graph = nx.DiGraph()
        graph.add_node('S')
        graph.add_nodes_from(layer_1_ids)
        graph.add_nodes_from(layer_2_ids)
        graph.add_node('T')
        Twins = [wins[n] + remain[n]]
        for team in range(0, len(layer_1_ids)):
            graph.add_edges_from(
                [('S', layer_1_ids[team], {'capacity': Layer1_capacities[team], 'flow': 0})])
        k = 0
        for team in range(0, teams):
            for j in range(team, teams - 1):
                graph.add_edges_from(
                    [(layer_1_ids[k], layer_2_ids[team], {'capacity': Layer1_capacities[k], 'flow': 0})])
                graph.add_edges_from(
                    [(layer_1_ids[k], layer_2_ids[j + 1], {'capacity': Layer1_capacities[k], 'flow': 0})])
                if (k < (((teams * (teams - 1)) / 2) - 1)):
                    k = k + 1
        for team in range(0, teams):
            if (team == n):
                graph.add_edges_from(
                    [(layer_2_ids[team], 'T', {'capacity': remain[team], 'flow': 0})])
            else:
                graph.add_edges_from(
                    [(layer_2_ids[team], 'T', {'capacity': Twins - wins[team], 'flow': 0})])
        ford_fulkerson(graph, 'S', 'T', n)

    for team in eliminated:
        print(team, end=" ")

if __name__ == '__main__':
    for team in test.teams:
        if test.isEliminated(team):
            R = test.certificateOfElimination(team)
            if type(R) == list:
                R = ' '.join(test.certificateOfElimination(team))
            print('{} is eliminated by the subset R = '.format(
                team) + '{' + R + '}')
        else:
            print('{} is not eliminated'.format(team))
