def checkIfPangram(sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        hashset = set()
        for c in sentence:
            hashset.add(c)
        return len(hashset) == 26
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))