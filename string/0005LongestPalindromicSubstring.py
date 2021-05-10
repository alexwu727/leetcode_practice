from problem_abc import ProblemAbc


class Problem5(ProblemAbc):
    def __init__(self):
        self.url = "https://leetcode.com/problems/longest-palindromic-substring/"
        self.test_cases = ["babad", "cbbd", "a", "abbabde", "ccd"]
        self.y = ["aba", "bb", "a", "abba", "cc"]

    @staticmethod
    def solution(test_case):
        s = test_case

        if len(s) == 1:
            return s
        mx = 1
        ans = s[0]
        i = (len(s) - 1) // 2
        n = 1
        direction = 1
        # start from the middle
        # the edge character is restricted
        # e.g. abcde : c -> d -> b -> a -> e
        while (i >= 0) and (i <= len(s) - 1):
            # if ith length of maximum substring is less than mx
            if (i + 1) * 2 <= mx:
                break
            if (len(s) - i) * 2 - 1 < mx:
                break
            # center of string
            for j in [1, 2]:
                left = i
                right = i + j
                while left >= 0 and right <= len(s):
                    sub_string = s[left:right]
                    if sub_string == sub_string[::-1]:
                        if len(sub_string) > mx:
                            mx = len(sub_string)
                            ans = sub_string
                        left -= 1
                        right += 1
                    else:
                        break

            # change the direction for the next iteration
            i += n * direction
            direction = -direction
            n += 1
        return ans


if __name__ == '__main__':
    p = Problem5()
    p.submit()
