class Solution:
    def maxVowels(self, s, k):

        vowels = {'a', 'e', 'i', 'o', 'u'}

        # count vowels in first window
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # slide window
        for right in range(k, len(s)):

            outgoing = s[right - k]
            incoming = s[right]

            if outgoing in vowels:
                count -= 1

            if incoming in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count