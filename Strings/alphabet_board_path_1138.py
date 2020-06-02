class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # always either go left->down/up or up->right/left
        lookUp = {chr(97+i):[int(i/5), i % 5] for i in range(26)}
        row = col = 0
        ret = ""
        currentPos = (0,0)  # row, col
        for letter in target:
            row, col = lookUp[letter]
            vert = row - currentPos[0]
            horiz = col - currentPos[1]
            if horiz < 0: ret += "L" * abs(horiz)
            if vert < 0: ret += "U" * abs(vert)
            if horiz > 0: ret += "R" * abs(horiz)
            if vert > 0: ret += "D" * abs(vert)
            ret += "!"
            currentPos = (row, col)
        return ret
