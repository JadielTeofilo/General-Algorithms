"""
A valid number can be split up into these components (in order):

    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.


start
    digit -> decimal_state
    sign -> decimal_state
    dot -> integer_state

decimal_state
        dot -> integer_state
        digit -> decimal_state

integer_state
        digit -> integer_state
        expo -> exponent_state

exponent_state 
        digit -> expo_digit_state
        sign -> ex_sign_state

ex_sign_state
        digit -> expo_digit_state

expo_digit_state
        digit -> expo_digit_state


O(n) time where n is the size of the string

"""
class Solution:
    def isNumber(self, word: str) -> bool:
        states: Dict[str, Dict[str, str]] = {
            'start': {'digit': 'decimal_state', 'sign': 'decimal_state', 'dot': 'integer_state'},
        }
        end_states: Set[str] = {'decimal_state', 'integer_state', 
                                'expo_digit_state'}
        curr: str = 'start'
        for char in word:
            char_type: str = self.find_type(char)  # TODO
            curr = states[curr].get(char_type, '')
            if not curr:
                return False
        return curr in end_states:
            
            
        
