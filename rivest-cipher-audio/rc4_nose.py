'''
Test Vectors obtained from:
https://en.wikipedia.org/wiki/RC4#Test_vectors

'''
import nose
from nose import with_setup
from rc4 import encrypt, decrypt

def TestEncryptEmpty():
    """
    Test encrypt function for empty plainfile
    """
    expected = ""
    
    encrypt("asdqwqweqqa", "encryptEmptyP.txt", "encryptEmptyC.txt")
    with open('encryptEmptyC.txt', 'rb') as myfile:
        result = myfile.read()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected

def TestDecryptEmpty():
    """
    Test decrypt function for empty cipherfile
    """
    expected = ""
    
    encrypt("asdqwqweqqa", "decryptEmptyC.txt", "decryptEmptyP.txt")
    with open("decryptEmptyP.txt", 'rb') as myfile:
        result = myfile.read()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected

def TestEncryptSmall():
    """
    Test encrypt with small key and compare with
    the hexadecimal decrypted result from 
    RC4 Wiki [Links provided in at the top]
    """
    expected = "BBF316E8D940AF0AD3"
    encrypt("Key", "encryptSmallP.txt", "encryptSmallC.txt")
    with open("encryptSmallC.txt", "rb") as myfile:
        result = myfile.read().encode("hex").upper()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected
    
def TestDecryptSmall():
    """
    Test decrypt with small key
    """
    expected = "Plaintext"
    decrypt("Key", "decryptSmallC.txt", "decryptSmallP.txt")
    with open("decryptSmallP.txt", "rb") as myfile:
        result = myfile.read()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected

def TestEncryptLong():
    """
    Test encrypt with a longer key and compare with
    the hexadecimal decrypted result from 
    RC4 Wiki [Links provided in at the top]
    """
    expected = "1021BF0420"
    encrypt("Wiki", "encryptLongP.txt", "encryptLongC.txt")
    with open("encryptLongC.txt", "rb") as myfile:
        result = myfile.read().encode("hex").upper()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected
    
def TestDecryptLong():
    """
    Test decrypt with a longer key
    """
    expected = "pedia"
    decrypt("Wiki", "decryptLongC.txt", "decryptLongP.txt")
    with open("decryptLongP.txt", "rb") as myfile:
        result = myfile.read()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected

def TestEncryptMultipleWords():
    """
    Test encrypt with long key and multiple words
    then compare with the hexadecimal decrypted result from 
    RC4 Wiki [Links provided in at the top]
    """
    expected = "45A01F645FC35B383552544B9BF5"
    encrypt("Secret", "encryptMultipleP.txt", "encryptMultipleC.txt")
    with open("encryptMultipleC.txt", "rb") as myfile:
        result = myfile.read().encode("hex").upper()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected
    
def TestDecryptMultipleWords():
    """
    Test decrypt with long key and multiple words
    """
    expected = "Attack at dawn"
    decrypt("Secret", "decryptMultipleC.txt", "decryptMultipleP.txt")
    with open("decryptMultipleP.txt", "rb") as myfile:
        result = myfile.read()
    print "Expected: " + expected
    print "Result: " + result
    assert result == expected


if __name__ == '__main__':
    nose.runmodule()
    