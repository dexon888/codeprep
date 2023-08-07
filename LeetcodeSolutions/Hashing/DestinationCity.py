def destCity(paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        departure = set()
        for path in paths:
            departure.add(path[0])

        for path in paths:
            if path[1] not in departure:
                return path[1]
            
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))