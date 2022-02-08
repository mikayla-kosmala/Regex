"""Hacker Rank: Regex Introduction"""

# Libraries -------------------------
import re

# Challenges ------------------------

""" Matching Specific String:
Using Regex count how many times hackerrank shows up in the string.
"""

def match_specific_string(string):
    regex_pattern = r'hackerrank'
    results = len(re.findall(regex_pattern, string))
    return results


""" Matching Anything But NewLine:
Using Regex detect if the string follows the pattern where there is a set of 4 groups of 3 characters with a period seperating them.
example abc.def.ghi.jkx.
"""

def matching_anything_but_newline(string):
    regex_pattern = r"^...\....\....\....$"
    results = re.match(regex_pattern, string)
    return results

""" Matching Digits & Non-Digit Characters:
Using Regex detect if the string matching the following pattern: 00A00A0000

0 denotes if a digit character and A denotes a non-digit character.
"""

def matching_digits_and_non_digit_characters(string):
    regex_pattern = r'(\d{2}\D){2}\d{4}'
    results = re.match(regex_pattern,string)
    return results

""" Matching Whitespace and Non-Whitespace Character:
Using Regex detect if the string matching the following pattern: 00A00A00

0 denotes if a whitespace character and A denotes a non-whitespace character.
"""

def matching_whitespace_and_non_whitespace_characters(string):
    regex_pattern = r'(\S{2}\s){2}\S{2}'
    results = re.match(regex_pattern,string)
    return results


""" Matching Word and Non-Word Character
Using Regex detect if the string matches the following pattern: 000A0000000000A000

0 denotes if a word character and A denotes a non-word character.
"""

def matching_word_and_non_word_character(string):
    regex_pattern = r'\w{3}\W\w{10}\W\w{3}'
    results = re.match(regex_pattern,string)
    return results

""" Matching Start & End
Using Regex detect if the string matches the following pattern: A0000.

0 denotes if a word character and A denotes a digit character.
"""

def matching_start_and_end(string):
    regex_pattern = r'^\d\w{4}\.$'
    results = re.match(regex_pattern,string)
    return results
