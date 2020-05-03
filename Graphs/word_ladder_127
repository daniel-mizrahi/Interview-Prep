class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        dictionary = set(wordList)
        queue = [(beginWord, 1)]  # word, jumps
        while len(queue) > 0:
            word, distance = queue.pop(0)
            for i, c in enumerate(word):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in dictionary and new_word not in visited:
                        if new_word == endWord:
                            return distance + 1
                        queue.append((new_word, distance + 1))
                        visited.add(new_word)
        return 0
