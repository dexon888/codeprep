from collections import defaultdict
def countPoints(rings):
        """
        :type rings: str
        :rtype: int
        """
        map = defaultdict(str)
        result = 0
        for i in range(0, len(rings), 2):
            map[rings[i + 1]] += rings[i]
        for ring in map:
            if "B" in map[ring] and "G" in map[ring] and "R" in map[ring]:
                result += 1
        return result

rings = "B0B6G0R6R0R6G9"
print(countPoints(rings))