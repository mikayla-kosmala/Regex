'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Postive Lookahead
# Count the number of occurrences of o followed immediately by oo
Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.


test_string_1 = "gooooo!"
test_string_2 = "goooglooo!"
test_string_3 = "googoogoogooo"

print("\nChallenge 1--------------\n"+test_string_1+": Found",str(bool(re.findall(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+": Found",str(bool(re.findall(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+": Found",str(bool(re.findall(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Negative Lookahead
# Find the number of occurences of characters which are not
# immediately followed by that same character

regex_pattern = r'(.)(?!\1)'


test_string_1 = "gooooo!"
test_string_2 = "###$$$$"
test_string_3 = "goluo"

print("\nChallenge 2--------------\n"+test_string_1+": Found",str(bool(re.findall(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+": Found",str(bool(re.findall(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+": Found",str(bool(re.findall(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Postive Lookbehind
# Find the number of occurences of digit which are
# immediately followed by an odd digit

Regex_Pattern = r'(?<=[13579])\d'

test_string_1 = "123Go!"
test_string_2 = "11111"
test_string_3 = "1349876562bsdbcjksdc bsjdc11231231sc nsdj cs,c n"

print("\nChallenge 3--------------\n"+test_string_1+": Found",str(bool(re.findall(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+": Found",str(bool(re.findall(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+": Found",str(bool(re.findall(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Negative Lookbehind
# Find the number of occurences of characters which aren't
# immediately followed by a vowel
Regex_Pattern = r'(?<![aeiouAEIOU])(.)'

test_string_1 = "1o1s"
test_string_2 = "hireme"
test_string_3 = "pls"

print("\nChallenge 4--------------\n"+test_string_1+": Found",str(bool(re.findall(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+": Found",str(bool(re.findall(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+": Found",str(bool(re.findall(Regex_Pattern, test_string_3))).lower())
