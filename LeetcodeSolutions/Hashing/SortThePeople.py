def sortPeople(names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        map = {}
        for i in range(len(names)):
            map[heights[i]] = names[i]
        heights = sorted(heights, reverse=True)
        names = [map[height] for height in heights]
        return names

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))