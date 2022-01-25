import pytest
import regex_application as ra
import regex_application_test_variables as tv

# Testing functions for detect_html_tags ----------
def test_detect_html_tags_1():
    """testing detect_html_tags with html_1"""
    results = ra.detect_html_tags(tv.html_1)
    assert results == "a;div;p"

def test_detect_html_tags_2():
    """testing detect_html_tags with html_2"""
    results = ra.detect_html_tags(tv.html_2)
    assert results == "a;b;br;div;i;li"

def test_detect_html_tags_3():
    """testing detect_html_tags with html_2"""
    results = ra.detect_html_tags(tv.html_3)
    assert results == "a;b;i;li;span;ul"

# Testing function for find_a_sub_word

def test_find_a_sub_word_1():
    """testing find_a_sub_word with string_1 and sub_word_1"""
    results = ra.find_a_sub_word(tv.string_1, tv.sub_word_1)
    assert results == 2

def test_find_a_sub_word_2():
    """testing find_a_sub_word with string_1 and sub_words_2"""
    results = ra.find_a_sub_word(tv.string_1, tv.sub_word_2)
    assert results == 2

def test_find_a_sub_word_3():
    """testing find_a_sub_word with string_1 and sub_words_3"""
    results = ra.find_a_sub_word(tv.string_1, tv.sub_word_3)
    assert results == 1

def test_find_a_sub_word_4():
    """testing find_a_sub_word with string_1 and sub_words_4"""
    results = ra.find_a_sub_word(tv.string_1, tv.sub_word_4)
    assert results == 1

# Testing function for alien_username
def test_alien_username_1():
    """testing alien_username with username_1"""
    results = ra.alien_username(tv.username_1)
    assert results == "VALID"

def test_alien_username_2():
    """testing alien_username with username_2"""
    results = ra.alien_username(tv.username_2)
    assert results == "INVALID"

def test_alien_username_3():
    """testing alien_username with username_3"""
    results = ra.alien_username(tv.username_3)
    assert results == "INVALID"

def test_alien_username_4():
    """testing alien_username with username_4"""
    results = ra.alien_username(tv.username_4)
    assert results == "VALID"

def test_alien_username_5():
    """testing alien_username with username_5"""
    results = ra.alien_username(tv.username_5)
    assert results == "INVALID"

# Testing ip_address_validation
def test_ip_address_validation_1():
    """testing ip_address_username with ip_address_1"""
    results = ra.ip_address_validation(tv.ip_address_1)
    assert results == "IPv6"

def test_ip_address_validation_2():
    """testing ip_address_username with ip_address_2"""
    results = ra.ip_address_validation(tv.ip_address_2)
    assert results == "IPv4"

def test_ip_address_validation_3():
    """testing ip_address_username with ip_address_3"""
    results = ra.ip_address_validation(tv.ip_address_3)
    assert results == "Neither"

def test_ip_address_validation_4():
    """testing ip_address_username with ip_address_2"""
    results = ra.ip_address_validation(tv.ip_address_4)
    assert results == "IPv6"

# Testing function find_a_word
def test_find_a_word_1():
    """testing find_a_word with string_2 with word_1"""
    results = ra.find_a_word(tv.string_2,tv.word_1)
    assert results == 75

def test_find_a_word_2():
    """testing find_a_word with string_2 with word_2"""
    results = ra.find_a_word(tv.string_2,tv.word_2)
    assert results == 48

def test_find_a_word_3():
    """testing find_a_word with string_2 with word_3"""
    results = ra.find_a_word(tv.string_2,tv.word_3)
    assert results == 83

def test_find_a_word_4():
    """testing find_a_word with string_2 with word_3"""
    results = ra.find_a_word(tv.string_2,tv.word_4)
    assert results == 93

# Testing function detect_the_email_address
def test_detect_the_email_address_1():
    """testing detect_the_email_address with string_3"""
    results = ra.detect_the_email_address(tv.string_3)
    assert results == "Traveler@ngs.org;apps@ngs.org;askngs@nationalgeographic.com;feedback@natgeotv.com;genographic@ngs.org;genographicespanol@ngs.org;givinginfo@ngs.org;jbmccorm@ngs.org;maps@ngs.org;mpotts@ngs.org;newsdesk@nationalgeographic.com;ngassignment@ngs.org;ngsdigital@customersvc.com;ngsforum@nationalgeographic.com;ngsline@customersvc.com;pressroom@ngs.org;speakers@ngs.org;stock@ngs.org;topo@ngs.org"

def test_detect_the_email_address_2():
    """testing detect_the_email_address with string_4"""
    results = ra.detect_the_email_address(tv.string_4)
    assert results == "drm@agc.railnet.gov.in;drm@ald.railnet.gov.in;drm@bb.railnet.gov.in;drm@bsl.railnet.gov.in;drm@dli.railnet.gov.in;drm@fzr.railnet.gov.in;drm@jhs.railnet.gov.in;drm@lko.railnet.gov.in;drm@mb.railnet.gov.in;drm@ngp.railnet.gov.in;drm@pa.railnet.gov.in;drm@sur.railnet.gov.in;drm@umb.railnet.gov.in;drmaii@nwr.railnet.gov.in;drmapdj@nfr.railnet.gov.in;drmasn@er.railnet.gov.in;drmbkn@nwr.railnet.gov.in;drmbsb@ner.railnet.gov.in;drmbza@scr.railnet.gov.in;drmdhn@ecr.railnet.gov.in;drmdnr@ecr.railnet.gov.in;drmgnt@scr.railnet.gov.in;drmgtl@scr.railnet.gov.in;drmhwh@er.railnet.gov.in;drmizn@ner.railnet.gov.in;drmjp@nwr.railnet.gov.in;drmju@nwr.railnet.gov.in;drmkir@nfr.railnet.gov.in;drmkur@eastcoastrailway.gov.in;drmljn@ner.railnet.gov.in;drmlmg@nfr.railnet.gov.in;drmmas@sr.railnet.gov.in;drmmdu@sr.railnet.gov.in;drmmgs@ecr.railnet.gov.in;drmmldt@er.railnet.gov.in;drmned@scr.railnet.gov.in;drmpgt@sr.railnet.gov.in;drmrny@nfr.railnet.gov.in;drmsa@sr.railnet.gov.in;drmsbp@eastcoastrailway.gov.in;drmsc@scr.railnet.gov.in;drmsdah@er.railnet.gov.in;drmsee@ecr.railnet.gov.in;drmshyb@scr.railnet.gov.in;drmspj@ecr.railnet.gov.in;drmtpj@sr.railnet.gov.in;drmtsk@nfr.railnet.gov.in;drmtvc@sr.railnet.gov.in;drmwat@eastcoastrailway.gov.in;gm@cr.railnet.gov.in;gm@eastcoastrailway.gov.in;gm@ecr.railnet.gov.in;gm@er.railnet.gov.in;gm@ncr.railnet.gov.in;gm@ner.railnet.gov.in;gm@nfr.railnet.gov.in;gm@nr.railnet.gov.in;gm@nwr.railnet.gov.in;gm@scr.railnet.gov.in;gm@sr.railnet.gov.in"