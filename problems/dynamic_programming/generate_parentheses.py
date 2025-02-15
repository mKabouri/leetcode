# Link: https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def simulate_expression(exp: str, nb_open: int, counter: int):
            if len(exp) == 2*n:
                res.append(exp)
                return
            if nb_open == n:
                valid_parenthesis = {")"}
            elif counter == 0:
                valid_parenthesis = {"("}
            else:
                valid_parenthesis = {"(", ")"}

            for valid_par in valid_parenthesis:
                if valid_par == "(":
                    simulate_expression(exp + valid_par, nb_open+1, counter+1)
                else:
                    simulate_expression(exp + valid_par, nb_open, counter-1)

        simulate_expression("(", 1, 1)
        return res
