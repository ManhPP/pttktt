import math


class VEB:
    def __init__(self, u):
        if u < 0:
            raise Exception(f"veb init error u: {u}")
        self.u = 2
        while self.u < u:
            self.u *= self.u

        self.min = None
        self.max = None
        if u > 2:
            self.clusters = [None] * self.high(self.u)

        self.summary = None

    def high(self, x):
        return int(math.floor(x / math.sqrt(self.u)))

    def low(self, x):
        return int((x % math.ceil(math.sqrt(self.u))))

    def index(self, cluster, position):
        return int((cluster * math.floor(math.sqrt(self.u))) + position)

    def insert(self, key):
        if self.min is None:
            self.min = key
            self.max = key
        elif key < self.min:
            key, self.min = self.min, key
            if self.u > 2:
                h = self.high(self.min)
                self.clusters[h].min = self.min
        if self.u > 2:
            h = self.high(key)
            if self.clusters[h] is None:
                self.clusters[h] = VEB(self.high(self.u))
            if self.summary is None:
                self.summary = VEB(self.high(self.u))

            if self.clusters[h].min is None:
                self.summary.insert(h)
                self.clusters[h].min = self.low(key)
                self.clusters[h].max = self.low(key)

            else:
                self.clusters[h].insert(self.low(key))

        if key > self.max:
            self.max = key

    def has_member(self, key):
        if self.u < key:
            return False
        if key == self.min or key == self.max:
            return True
        else:
            if self.u == 2:
                return False
            else:
                cluster = self.clusters[self.high(key)]
                if cluster is not None:
                    return cluster.has_member(self.low(key))
                else:
                    return False

    def get_successor(self, key):
        if self.u <= 2:
            if key == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min is not None and key < self.min:
            return self.min

        else:
            h = self.high(key)
            l = self.low(key)
            max_low = None
            cluster = self.clusters[h]

            if cluster is not None:
                max_low = cluster.max
            if max_low is not None and l < max_low:
                offset = cluster.get_successor(l)
                return self.index(h, offset)
            else:
                suc_cluster = None
                if self.summary is not None:
                    suc_cluster = self.summary.get_successor(h)
                if suc_cluster is None:
                    return None
                else:
                    cluster2 = self.clusters[suc_cluster]
                    offset = 0
                    if cluster2 is not None:
                        offset = cluster2.min
                    return self.index(suc_cluster, offset)

    def get_predecessor(self, key):
        if self.u <= 2:
            if key == 1 and self.min == 0:
                return 0
            else:
                return None

        elif self.max is not None and key > self.max:
            return self.max

        else:
            h = self.high(key)
            l = self.low(key)
            min_low = None
            cluster = self.clusters[h]
            if cluster is not None:
                min_low = cluster.min

            if min_low is not None and l > min_low:
                offset = cluster.get_predecessor(l)
                if offset is None:
                    offset = 0
                return self.index(h, offset)
            else:
                pre_cluster = None
                if self.summary is not None:
                    pre_cluster = self.summary.get_predecessor(h)
                if pre_cluster is None:
                    if self.min is not None and key > self.min:
                        return self.min
                    else:
                        return None

                else:
                    cluster2 = self.clusters[pre_cluster]
                    offset = 0
                    if cluster2 is not None:
                        offset = cluster2.max
                    return self.index(pre_cluster, offset)

    def delete(self, key):
        if self.min == self.max:
            self.min = None
            self.max = None

        elif self.u == 2:
            if key == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min

        else:
            if key == self.min:
                first_cluster = self.summary.min
                key = self.index(first_cluster, self.clusters[first_cluster].min)
                self.min = key
            self.clusters[self.high(key)].delete(self.low(key))

            if self.clusters[self.high(key)].min is None:
                self.summary.delete(self.high(key))
                if key == self.max:
                    max_summary = self.summary.max
                    if max_summary is None:
                        self.max = self.min
                    else:
                        self.max = self.index(max_summary, self.clusters[max_summary].max)
            elif key == self.max:
                self.max = self.index(self.high(key), self.clusters[self.high(key)].max)


if __name__ == '__main__':
    v = VEB(-1)
    v.insert(2)
    v.insert(3)
    v.insert(6)
    v.insert(7)
    v.insert(1)

    v.has_member(4)
