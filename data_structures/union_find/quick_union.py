class QuickUnion:

    def __init__(self, size):
        self.id = [i for i in range(size)]

    def get_root(self, id_):
        while id_ != self.id[id_]:
            id_ = self.id[id_]

        return id_

    def calculate_weight(self, id_):
        weight = 1
        while self.id[id_] != id_:
            weight += 1
            id_ = self.id[id_]

        return weight

    def is_connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def union(self, p, q):
        i = self.get_root(self.id[p])
        j = self.get_root(self.id[q])

        if i < j:
            self.id[i] = j
        else:
            self.id[j] = i
