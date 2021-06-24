from abc import ABC, abstractmethod


class ProblemAbc(ABC):
    url = ""
    test_cases = []
    y = []
    adjust_output = False
    wrong = False

    @abstractmethod
    def solution(self):
        pass

    def submit(self):
        print("problem url:", self.url)
        for i in range(len(self.test_cases)):
            output = self.solution(self.test_cases[i])
            if self.adjust_output == "any_order":
                for j in output:
                    if j not in self.y[i]:
                        self.wrong = True
                        break
                for j in self.y[i]:
                    if j not in output:
                        self.wrong = True
                        break

            else:
                if self.adjust_output:
                    output = self.adjust_output(output)
                if output != self.y[i]:
                    self.wrong = True
        if self.wrong:
            print("===== wrong output ======")
            print("------- test case -------")
            print(self.test_cases[i], "\n")
            print("---- expected output ----")
            print(self.y[i])
            print("------ your output ------")
            print(output)
            return
        print("valid solution!")
