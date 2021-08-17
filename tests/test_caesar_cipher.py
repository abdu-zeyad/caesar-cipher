from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import crack,encrypt,decrypt

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    word = 'nope10'
    key = 5
    actual = encrypt(word,5)
    expected = 'stuj65'
    assert actual == expected

def test_decrypt():
    word = 'stuj65'
    key = 5
    actual = decrypt(word,5)
    expected = 'nope10'
    assert actual == expected


def test_crack():
    word = 'stuj65'
    actual = crack(word)
    expected = 'nope10'
    assert actual == expected