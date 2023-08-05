def decodeMessage(key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ptr = 0
        map = {" ": " "}
        for c in key:
            if c != " " and c not in map:
                map[c] = alphabet[ptr]
                ptr += 1
                if ptr == len(alphabet):
                    break
        result = ""
        for c in message:
            result += map[c]
        return result

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decodeMessage(key, message))