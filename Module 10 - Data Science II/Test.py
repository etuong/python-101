import os

import networkx as nx
import numpy as np

# 建立类
class BaseballElimination:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            m = f.readlines()
        self.numberOfTeams = int(m[0].strip())  # 球队数
        n = self.numberOfTeams
        self.teams = []  # 球队名
        self.w = []  # 获胜场次
        self.l = []  # 失败场次
        self.r = []  # 剩余场次
        self.g = np.arange(n ** 2).reshape(n, n)  # 剩余场次矩阵
        for i in range(n):
            item = m[i + 1].split()
            self.teams.append(item[0])
            self.w.append(int(item[1]))
            self.l.append(int(item[2]))
            self.r.append(int(item[3]))
            for j in range(n):
                self.g[i][j] = int(item[j + 4])

    # 获得该team的获胜场次
    def wins(self, team):
        return self.w[self.teams.index(team)]

    # 获得该team的失败场次
    def losses(self, team):
        return self.l[self.teams.index(team)]

    # 获得该team的剩余场次
    def remaining(self, team):
        return self.r[self.teams.index(team)]

    # 获得team1和team2的之间的剩余比赛场次
    def against(self, team1, team2):
        i = self.teams.index(team1)
        j = self.teams.index(team2)
        return self.g[i][j]

    # 判断该team是否无缘第一
    def isEliminated(self, team):
        x = self.teams.index(team)
        n = self.numberOfTeams
        for i in range(n):  # Trivial elimination
            if (i != x) & (self.w[x] + self.r[x] < self.w[i]):
                return True
        # 构建有向图
        G = nx.DiGraph()
        G.add_node('s')
        G.add_node('t')
        for i in range(n):
            if i != x:
                G.add_node(i)
                G.add_edge(i, 't', capacity=self.w[x] + self.r[x] - self.w[i])
                if i < n:
                    for j in range(i + 1, n):
                        if j != x:
                            i_j = '{}-{}'.format(i, j)
                            G.add_node(i_j)
                            G.add_edge('s', i_j, capacity=self.g[i][j])
                            G.add_edge(i_j, i, capacity=float('inf'))
                            G.add_edge(i_j, j, capacity=float('inf'))
        # 计算最大流
        max_flow_s = nx.maximum_flow(G, 's', 't')[1]['s']
        # 判断源点出去的flow是否均full
        Flag = 1
        for i_j in max_flow_s:
            i = int(i_j.split('-')[0])
            j = int(i_j.split('-')[1])
            if max_flow_s[i_j] != self.g[i][j]:
                Flag = 0
        return Flag == 0

    # 获得证明team无缘夺冠的集合R
    def certificateOfElimination(self, team):
        x = self.teams.index(team)
        n = self.numberOfTeams
        for i in range(n):
            if (i != x) & (self.w[x] + self.r[x] < self.w[i]):
                return self.teams[i]
        G = nx.DiGraph()
        G.add_node('s')
        G.add_node('t')
        for i in range(n):
            if i != x:
                G.add_node(i)
                G.add_edge(i, 't', capacity=self.w[x] + self.r[x] - self.w[i])
                if i < n:
                    for j in range(i + 1, n):
                        if j != x:
                            i_j = '{}-{}'.format(i, j)
                            G.add_node(i_j)
                            G.add_edge('s', i_j, capacity=self.g[i][j])
                            G.add_edge(i_j, i, capacity=float('inf'))
                            G.add_edge(i_j, j, capacity=float('inf'))
        # 计算最小割
        min_cut = nx.minimum_cut(G, 's', 't')[1]
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


# 测试
if __name__ == '__main__':
    test = BaseballElimination('mlb.txt')
    for team in test.teams:
        if test.isEliminated(team):
            R = test.certificateOfElimination(team)
            if type(R) == list:
                R = ' '.join(test.certificateOfElimination(team))
            print('{} is eliminated by the subset R = '.format(team) + '{' + R + '}')
        else:
            print('{} is not eliminated'.format(team))
