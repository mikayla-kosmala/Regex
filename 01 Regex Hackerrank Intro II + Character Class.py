'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Matching Start & End
# The goal of this challenge was to follow a A0000. pattern
# where 0 denotes if a digit character and A denotes a word character

Regex_Pattern = r'^\d\w{4}\.$'	# Do not delete 'r'.


test_string_1 = "0qwer."
test_string_2 = "10aaaa."
test_string_3 = "1a2a2."

print("\nChallenge 1--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Specific Characters
# Needs to follow the following pattern
# First character: 1, 2 or 3
# Second character: 1, 2 or 0
# Third character: x, s or 0
# Fourth character: 3, 0 , A or a
# Fifth character: x, s or u
# Sixth character: . or ,

regex_pattern = r"^[123][120][xs0][30Aa][xsu][\.,]$"


test_string_1 = "21sAu,"
test_string_2 = "3000s.."
test_string_3 = "123120xs030Aaxsu.,"

print("\nChallenge 2--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Excluding Specific Characters
# Needs to follow the following pattern
# First character should not be a digit.
# Second character should not be a lowercase vowel.
# Third character should not be b, c, D or F.
# Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
# Fifth character should not be a uppercase vowel.
Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$'

test_string_1 = "athink?"
test_string_2 = "w12eE'"
test_string_3 = "w32eW'."

print("\nChallenge 3--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Character Ranges
# The first character must be a lowercase English alphabetic character.
# The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
# The third character must not be a lowercase English alphabetic character.
# The fourth character must not be an uppercase English alphabetic character.
# The fifth character must be an uppercase English alphabetic character.

Regex_Pattern = r"^[a-z][1-9][^a-z][^A-Z][A-Z].*"

test_string_1 = "h4CkR"
test_string_2 = "q9$?WWe"
test_string_3 = "a0$?ZWe"

print("\nChallenge 4--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())
