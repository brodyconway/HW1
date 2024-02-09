import itertools

from Marriage import Marriage


class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []
        self.output_stable_matchings()

    def output_stable_matchings(self):
        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """
        """"
        Just create pairs by keeping women same order itll be different each time
        """
        perm = itertools.permutations(range(1, self.num + 1))
        pairs = []
        for i in perm:
            pair = []
            t = 1
            while t <= self.num:
                marriage = Marriage(i[t - 1], t)
                t += 1
                pair.append(marriage)
            pairs.append(pair)
        self.stable_matchings = pairs
        #for prefw the key is the women and vice versa
        prefw = {}
        prefm = {}
        for i in self.stable_matchings:
            stable = True
            for t in i:
                man = self.men[t.man()]
                woman = self.women[t.woman()]
                if man[0] != t.woman():
                    if self.women[man[0]][0] == t.man():
                        stable = False
                    elif len(prefw[man[0]]) != 0:
                        prefw[man[0]].append(t.man())
                    else:
                        lists = [t.man()]
                        prefw[man[0]] = lists
                    if man[1] != t.woman():
                        if self.women[man[1]][0] == t.man():
                            stable = False
                        else:
                            list.append(t.m)






        return self.stable_matchings


Solution(3, women={1: [2,1,3], 2: [3,2,1], 3: [3,2,1]}, men={1: [1,2,3], 2: [2,1,3], 3: [3,2,1]})
