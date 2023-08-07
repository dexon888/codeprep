def uniqueMorseRepresentations(words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        seen = {"".join(morse[ord(c) - ord("a")] for c in word) for word in words}
        return len(seen)

words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))