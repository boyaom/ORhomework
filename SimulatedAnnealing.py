import random
import math
import copy

class SA():
    def __init__(self, n, w, d, init_with_shuffle=True, random_seed=42):
        random.seed(random_seed)
        self.w = w # weight matrix
        self.d = d # distance matrix
        self.n = n # problem size
        self.p = [i for i in range(0, n)] # permutation
        if init_with_shuffle: # shuffle this permutation
            random.shuffle(self.p)
            newd = [[0 for _ in range(n)] for __ in range(n)]
            for i in range(n):
                for j in range(n):
                    newd[i][j] = self.d[self.p[i]][self.p[j]]
            self.d = newd
        self.min_p = self.p[:]
        self.now_p_cost = self.calc_total_cost(self.p)
        self.min_p_cost = self.now_p_cost


    def get_two_random_node(self):
        # promise two nodes are different. And two nodes are in [0, n)
        a = random.randint(0, self.n - 1)
        b = a
        while a == b:
            b = random.randint(0, self.n - 1)
        return (b, a) if a > b else (a, b)

    def calc_total_cost(self, p, format_double=False):
        ret = 0.0 if format_double else 0
        for i in range(self.n):
            for j in range(self.n):
                ret += self.w[i][j] * self.d[p[i]][p[j]]
        return ret

    def solve(self, iterator_times, t0=10.0, d=0.9):
        """
        :param iterator_times: iterator_times
        :param t0: the first step of temperature
        :param d: 降温系数
        T = t0 * d^i
        :return: [ans_cost, ans_permutation]
        """
        T = t0
        for i in range(iterator_times):
            T *= d
            u, v = self.get_two_random_node()
            x = random.random()
            newp = copy.deepcopy(self.p)
            newp[u], newp[v] = newp[v], newp[u]
            total_cost = self.calc_total_cost(newp)
            delta_cost = self.now_p_cost - total_cost
            if delta_cost > 0 or x < math.exp(delta_cost / T):
                self.p = newp
                self.now_p_cost = total_cost
                if self.now_p_cost < self.min_p_cost:
                    self.min_p_cost = self.now_p_cost
                    self.min_p = self.p
            # if i % 10000 == 0:
            #     print(f"第 {i} 次循环中，跑出的总代价为 {total_cost}，目前状态的总代价为 {self.now_p_cost}，目前历史最佳总代价为 {self.min_p_cost}")
        return self.min_p_cost, self.min_p
