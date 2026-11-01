class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.orderd={}
        for i in range(len(order)):
            self.orderd[order[i]]=i
        def word_to_order(word):
            return [self.orderd[i] for i in word]
        for i in range(len(words)-1):
            if word_to_order(words[i]) > word_to_order(words[i+1]):
                return False
        return True