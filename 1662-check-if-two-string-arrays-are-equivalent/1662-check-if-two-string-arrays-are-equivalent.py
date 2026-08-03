class Solution:
    def arrayStringsAreEqual(self, word1, word2):

        i = j = 0
        x = y = 0

        while i < len(word1) and x < len(word2):

            # Characters must match
            if word1[i][j] != word2[x][y]:
                return False

            # Move to next character
            j += 1
            y += 1

            # Finished current word in word1?
            if j == len(word1[i]):
                i += 1
                j = 0

            # Finished current word in word2?
            if y == len(word2[x]):
                x += 1
                y = 0

        # Both arrays should finish together
        return i == len(word1) and x == len(word2)