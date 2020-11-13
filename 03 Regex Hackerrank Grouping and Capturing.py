'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Matching Word Boundaries
# Word starting with vowel (a,e,i,o, u, A, E, I , O or U).
# The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
# The matched word must start and end with a word boundary.

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z\s]*\b'	# Do not delete 'r'.


test_string_1 = "Found any match?"
test_string_2 = "okyouwin? yes"
test_string_3 = "Iamdead-4u"

print("\nChallenge 1--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Capturing & Non-Capturing Groups
#  should have 3 or more consecutive repetitions of ok.

regex_pattern = r"(ok){3}"


test_string_1 = "okokok! cya"
test_string_2 = "oookokokokokoko"
test_string_3 = "ok ok ok ok"

print("\nChallenge 2--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Alternative Matching
# must start with Mr., Mrs., Ms., Dr. or Er..
# The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'

test_string_1 = "Mr.DOSHI"
test_string_2 = "MR.MR"
test_string_3 = "Ms._underscore"

print("\nChallenge 3--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

