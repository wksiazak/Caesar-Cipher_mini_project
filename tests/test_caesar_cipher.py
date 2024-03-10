from ciphers.caesar import decrypt, encrypt


# Test for encrypt function
def test_encrypt():
    assert encrypt("Hello", 3) == "Khoor"
    assert encrypt("xyz", 3) == "abc"
    assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"


# Test for decrypt function
def test_decrypt():
    assert decrypt("Khoor", 3) == "Hello"
    assert decrypt("abc", 3) == "xyz"
    assert decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
