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
        #prefw contains men who prefer that women over current, and listw is just added tp that
        prefw = {}
        prefm = {}
        for i in pairs:
            for x in i:
                man = self.men[x[0]]
                woman = self.women[x[1]]
                listm = []
                listw = []
                if man[0] != x[1]:
                    if man[0] not in prefw:
                        listw.append(x[0])
                        prefw[man[0]] = listw
                    else:
                        prefw[man[0]].append(x[0])
                    if man[1] != x[1]:
                        if man[1] not in prefw:
                            listw = []
                            listw.append(x[0])
                            prefw[man[1]] = listw
                        else:
                            prefw[man[1]].append(x[0])
                if woman[0] != x[0]:
                    if woman[0] not in prefm:
                        listm.append(x[1])
                        prefm[woman[0]] = listm
                    else:
                        prefm[woman[0]].append(x[1])
                    if woman[1] != x[0]:
                        if woman[1] not in prefm:
                            listm = []
                            listm.append(x[1])
                            prefm[woman[1]] = listm
                        else:
                            prefm[woman[1]].append(x[1])












        return self.stable_matchings

