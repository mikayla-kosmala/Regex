'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Matching {x} Repetitions
# Must be of length equal to 45.
# The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
# The last 5 characters should consist of odd digits or whitespace characters.
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.


test_string_1 = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
test_string_2 = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo139	7"
test_string_3 = "x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957"

print("\nChallenge 1--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching {x,y} Repetitions
# Needs to follow the following pattern
# Should begin with 1 or 2 digits.
# After that, S should have 3 or more letters (both lowercase and uppercase).
# Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.

regex_pattern = r"^\d{1,2}[a-zA-Z]{3,}\.{0,3}$"


test_string_1 = "00d."
test_string_2 = "3threeormorealphabetsACNSDNPINQCPIQNCPNQPCINQPICNPIQNCPQINCQPC"
test_string_3 = "a91nckalnlkn."

print("\nChallenge 2--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Zero Or More Repetitions
# Needs to follow the following pattern
# Should begin with 2 or more digits.
# After that, it should have 0 or more lowercase letters.
# Should end with 0 or more uppercase letters

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'

test_string_1 = "14"
test_string_2 = "1akldflkvnlDFVDFVDFVD"
test_string_3 = "123321dasdASDASDASD1132"

print("\nChallenge 3--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching One Or More Repetitions
# Should begin with 1 or more digits.
# After that, it should have 1 or more uppercase letters.
# Should end with 1 or more lowercase letters.
Regex_Pattern = r"^\d+[A-Z]+[a-z]+$"

test_string_1 = "1Qa"
test_string_2 = "ASDA123ASDwer"
test_string_3 = "Ao"

print("\nChallenge 4--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Ending Items
# Should consist of only lowercase and uppercase letters (no numbers or symbols).
# Should end in s.
Regex_Pattern = r"^[a-zA-Z]*s$"

test_string_1 = "Kites"
test_string_2 = "1ess"
test_string_3 = "seses"

print("\nChallenge 5--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())
