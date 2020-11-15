'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Matching Same Text Again & Again
# String must be of length: 20
# 1st character: lowercase letter.
# 2nd character: word character.
# 3rd character: whitespace character.
# 4th character: non word character.
# 5th character: digit.
# 6th character: non digit.
# 7th character: uppercase letter.
# 8th character: letter (either lowercase or uppercase).
# 9th character: vowel (a, e, i , o , u, A, E, I, O or U).
# 10th character: non whitespace character.
# 11th character: should be same as 1st character.
# 12th character: should be same as 2nd character.
# 13th character: should be same as 3rd character.
# 14th character: should be same as 4th character.
# 15th character: should be same as 5th character.
# 16th character: should be same as 6th character.
# 17th character: should be same as 7th character.
# 18th character: should be same as 8th character.
# 19th character: should be same as 9th character.
# 20th character: should be same as 10th character.
Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1$'	# Do not delete 'r'.


test_string_1 = "ab #1?AZa$ab #1?AZa$"
test_string_2 = "ab-#1?AZa$ab-#1?AZa$"
test_string_3 = "ab #1?AZa ab #1?AZa "

print("\nChallenge 1--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Backrefernces To Failed Groups
# consists of 8 digits.
# may have "-" separator such that string gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
regex_pattern = r'^\d\d(-?)(\d\d\1){2}\d\d$'


test_string_1 = "12-34-56-78"
test_string_2 = "12-45-7810"
test_string_3 = "-12-45-78-10"

print("\nChallenge 2--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

