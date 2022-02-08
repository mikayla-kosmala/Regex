import pytest
import regex_intro as ri
import regex_intro_test_variables as tv

# Testing functions for match_specific_string------------------------------
def test_match_specific_string_1():
    """testing match_specific_string with string_1"""
    results = ri.match_specific_string(tv.string_1)
    assert results == 2

def test_match_specific_string_2():
    """testing match_specific_string with string_2"""
    results = ri.match_specific_string(tv.string_2)
    assert results == 3

# Testing functions for matching_anything_but_newline ---------------------
def test_matching_anything_but_newline_1():
    """testing matching_anything_but_newline with string_3"""
    results = ri.matching_anything_but_newline(tv.string_3)
    assert results == True

def test_matching_anything_but_newline_2():
    """testing matching_anything_but_newline with string_4"""
    results = ri.matching_anything_but_newline(tv.string_4)
    assert results == None

#Testing functions for matching_digits_and_non_digit_characters -----------
def test_matching_digits_and_non_digit_characters_1():
    """testing matching_digits_and_non_digit_characters with string_5"""
    results = ri.matching_digits_and_non_digit_characters(tv.string_5)
    assert results == True

def test_matching_digits_and_non_digit_characters_2():
    """testing matching_digits_and_non_digit_characters with string_6"""
    results = ri.matching_digits_and_non_digit_characters(tv.string_6)
    assert results == False

def test_matching_digits_and_non_digit_characters_3():
    """testing matching_digits_and_non_digit_characters with string_7"""
    results = ri.matching_digits_and_non_digit_characters(tv.string_7)
    assert results == False

#Testing functions for matching_whitespace_and_non_whitespace_character ---
def test_matching_whitespace_and_non_whitespace_characters_1():
    """testing matching_whitespace_and_non_whitespace_characters with string_8"""
    results = ri.matching_whitespace_and_non_whitespace_characters(tv.string_8)
    assert results == True

def test_matching_whitespace_and_non_whitespace_characters_2():
    """testing matching_whitespace_and_non_whitespace_characters with string_9"""
    results = ri.matching_whitespace_and_non_whitespace_characters(tv.string_9)
    assert results == False

def test_matching_whitespace_and_non_whitespace_characters_3():
    """testing matching_whitespace_and_non_whitespace_characters with string_10"""
    results = ri.matching_whitespace_and_non_whitespace_characters(tv.string_10)
    assert results == False

#Testing functions for matching_word_and_non_word_character ---------------
def test_matching_word_and_non_word_character_1():
    """testing matching_word_and_non_word_character with string_11"""
    results = ri.matching_word_and_non_word_character(tv.string_11)
    assert results == True

def test_matching_word_and_non_word_character_2():
    """testing matching_word_and_non_word_character with string_12"""
    results = ri.matching_word_and_non_word_character(tv.string_12)
    assert results == True

def test_matching_word_and_non_word_character_3():
    """testing matching_word_and_non_word_character with string_13"""
    results = ri.matching_word_and_non_word_character(tv.string_13)
    assert results == False

#Testing functions for matching_start_and_end -----------------------------
def test_matching_start_and_end_1():
    """testing matching_start_and_end with string_14"""
    results = ri.matching_start_and_end(tv.string_14)
    assert results == True

def test_matching_start_and_end_2():
    """testing matching_start_and_end with string_15"""
    results = ri.matching_start_and_end(tv.string_15)
    assert results == False

def test_matching_start_and_end_3():
    """testing matching_start_and_end with string_16"""
    results = ri.matching_start_and_end(tv.string_16)
    assert results == False