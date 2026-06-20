class Solution:
    def findAnagrams(self, s, p):

        # Answer list
        result = []

        # Pattern frequency map
        p_count = {}

        # Window frequency map
        window_count = {}

        # Build pattern hashmap
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1

        k = len(p)

        # Expand window using right pointer
        for right in range(len(s)):

            # Add incoming character
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # Window too large?
            if right >= k:

                # Character leaving window
                left_char = s[right - k]

                window_count[left_char] -= 1

                # Remove key if count becomes 0
                if window_count[left_char] == 0:
                    del window_count[left_char]

            # Compare both hashmaps
            if window_count == p_count:

                # Starting index of current window
                result.append(right - k + 1)

        return result