class QuickFind:

    def __init__(self, size):
        self.id = [i for i in range(size)]

    def is_connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
