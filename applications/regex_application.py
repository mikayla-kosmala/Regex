"""Hacker Rank: Regex"""

# Libraries -------------------------
import re
import sys

# Challenges ------------------------

""" Detect HTML Tags:
Using Regex detect the various tags found in an HTML document. 
Things to note: 
 Most tags come in pairs. <t> blah blah </t>
 An exception to this is the self-closing tags <p/>

Assign the tags found in a single line containing all of the unique tag names found in the input semi-colon separated and ordered lexicographically.
"""

def detect_html_tags(html):
    regex_pattern = r'<(\s*?\w+\s*?)'
    results = ';'.join(sorted(set(re.findall(regex_pattern, html))))
    return results


""" Find a Sub-Word:
Using Regex count the number of sub-words in a sentence. 

Things to note: 
 Word characters contain any of the following:
    English alphabetic letter
    Decimal digit
    or an underscore
 A sub-word which is a word character preceded and succeeded by word characters only.
"""

def find_a_sub_word(string,sub_word):
    regex_pattern = r"\w({})\w".format(sub_word)
    results = len(re.findall(regex_pattern, string))
    return results

""" Alien Username:
Using Regex determine if a username is Valid or Invalid 

Things to note about a valid username: 
 Must begin with an underscore or a period
 Must immediately followed by one or more digits
 After the digits there must be zero or english letters
 Username can be terminated with an underscore then there
  should be no characters after the sequence of 0 or more English letters
"""

def alien_username(username):
    regex_pattern = r'^[_.]\d+[a-zA-Z]*[_]?$'
    results = re.search(regex_pattern,username)
    return 'VALID' if results else 'INVALID'

""" IP Address Validation:
Using Regex determine if the text fed through is an IPv4 address IPv6 address or None of these.

Things to Note about IPv4 and IPv6 addresses:
 IPv4 - The typical format is A.B.C.D where A, B, C and D are integers between 0 and 255.
 IPv6 - Is 8 groups of 4 hexadecimal digits separated by colons. Leading zeros may be omitted in writing the address
"""

def ip_address_validation(ip_address):
    s4 =('^'+'{v4}\.'*3+'{v4}$').format(v4 = "(25[0-5]|2[0-4]\d|[01]?\d?\d)")
    s6 = ('^'+'{v6}:'*7+'{v6}$').format(v6 = '[\da-f]{1,4}')
    regex_pattern_ipv4 = re.compile(s4)
    regex_pattern_ipv6 = re.compile(s6)
    if regex_pattern_ipv4.match(ip_address):
        return 'IPv4'
    elif regex_pattern_ipv6.match(ip_address):
        return 'IPv6'
    else: 
        return 'Neither'


""" Find a Word: 
Using Regex count the number of occurences of a specific word in a sentence

Things to note word definition:
 A word is a non-empty maximum sequence of characters that can contain only lowercase letters, uppercase letters, digits, and underscores. 
"""
def find_a_word(string,word):
    regex_pattern = r'\b{}\b'.format(word)
    results = len(re.findall(regex_pattern,string))
    return results

""" Detect the Email Address: 
Using Regex find all the unique email addresses present in the text.

Things to note email definition:
 Multiple strings separated by dots before and after the '@' symbol. 
 Strings will be made up of characters in the ranges a-z,A-Z,0-9,_
"""

def detect_the_email_address(string):
    regex_pattern = "[\w|\.]+@(?:\w+\.)+\w"
    results_list = re.findall(regex_pattern,string)
    return ';'.join(sorted(list(set(results_list))))


""" Detect the Domain Name: 
Using Regex find all the unique domain names from the links or urls in the markup.

Things to note domain name:
 Prefixes like "www." and "ww2." should be scrubbed from the domain name.
"""

def detect_the_domain_name(string):
    regex_pattern = r"http[s]?://[\w-]+\.[\.\w-]+[\?/\"]"
    