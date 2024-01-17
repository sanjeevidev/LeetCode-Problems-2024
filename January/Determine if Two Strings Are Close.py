class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        sw1 = sorted(w1.values())
        sw2 = sorted(w2.values())
      
        keys_match = set(w1.keys()) == set(w2.keys())

        return sw1 == sw2 and keys_match
