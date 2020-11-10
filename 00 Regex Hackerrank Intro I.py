'''Hacker Rank: Regex'''
import re
import sys
#-----------------------------------------------------------------------------------------
#Matching Specific String 
# The goal was to see how many times hackerrank shows up in the string

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.


Test_String_1 = "The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers."
Test_String_2 = "hackerrank is hackerrank not HackerRank. so please use hackerrank always and not hackerrrank"

print("Challenge 1--------------\n"+"Number of matches :", len(re.findall(Regex_Pattern, Test_String_1)),
    "\nNumber of matches :", len(re.findall(Regex_Pattern, Test_String_2)))

#-----------------------------------------------------------------------------------------
#Matching Anything But NewLine
# The goal of this challenge was to follow a abc.def.ghi.jkx. pattern
# where there is a set of 4 groups of 3 characters with a period seperating them

regex_pattern = r"^...\....\....\....$"


test_string_1 = "123.456.abc.def"
test_string_2 = "1123.456.abc.def"

match = re.match(regex_pattern, test_string_1) is not None

print("\nChallenge 2--------------\n"+test_string_1+":",str(re.match(regex_pattern, test_string_1) is not None).lower(),
    "\n"+test_string_2+":",str(re.match(regex_pattern, test_string_2) is not None).lower())

#-----------------------------------------------------------------------------------------
#Matching Digits & Non-Digit Characters
# The goal of this challenge was to follow a 00A00A0000 pattern
# where 0 denotes if a digit character and A denotes a non-digit character

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"
Regex_Pattern = r"(\d{2}\D){2}\d{4}"

test_string_1 = "06-11-2015"
test_string_2 = "10a10.2015452254"
test_string_3 = "11..11.2015"

print("\nChallenge 3--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Whitespace & Non-Whitespace Character
# The goal of this challenge was to follow a 00A00A00 pattern
# where 0 denotes a whitespace character and A denotes a non-whitespace character

Regex_Pattern = r"\S\S\s\S\S\s\S\S"
Regex_Pattern = r"(\S\s){2}\S{2}"

test_string_1 = "12 11 15"
test_string_2 = "123 123 123"
test_string_3 = "12 12	1ee"

print("\nChallenge 4--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())

#-----------------------------------------------------------------------------------------
#Matching Word & Non-Word Character
# The goal of this challenge was to follow a 000A0000000000A000 pattern
# where 0 denotes a word character and A denotes a non-word character

# A word character is anything (a-z,A-Z,and 0-9) and underscores (_)

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"

test_string_1 = "www.hackerrank.com"
test_string_2 = "132.__________.co_"
test_string_3 = "www.hackerrank.co"

print("\nChallenge 5--------------\n"+test_string_1+":",str(bool(re.search(Regex_Pattern, test_string_1))).lower(),
    "\n"+test_string_2+":",str(bool(re.search(Regex_Pattern, test_string_2))).lower(),
    "\n"+test_string_3+":",str(bool(re.search(Regex_Pattern, test_string_3))).lower())
