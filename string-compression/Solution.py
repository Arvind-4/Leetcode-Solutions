// https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1
        while i < len(chars) - 1:
            if chars[i + 1] == chars[i]:
                chars.pop(i + 1)
                count += 1
            elif count > 1:
                cc = [*str(count)]
                for j in range(len(cc)):
                    chars.insert(i + j+ 1, cc[j])
                count = 1
                i += len(cc) + 1
            else:
                i += 1
        if count > 1:
            chars += [*str(count)]
        return len(chars)