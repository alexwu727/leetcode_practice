from abc import ABC, abstractmethod


class ProblemAbc(ABC):
    url = ""
    test_cases = []
    y = []

    @abstractmethod
    def solution(self):
        pass

    def submit(self):
        print("problem url:", self.url)
        for i in range(len(self.test_cases)):
            output = self.solution(self.test_cases[i])
            if output != self.y[i]:
                print("===== wrong output ======")
                print("------- test case -------")
                print(self.test_cases[i], "\n")
                print("---- expected output ----")
                print(self.y[i])
                print("------ your output ------")
                print(output)
                return
        print("valid solution!")
