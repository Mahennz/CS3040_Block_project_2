# CS3040_Block_project_2

Simple_Encryptor by Mahennz is a very basic implementation of a password encryptor. The program runs entirely in your terminal and guides the user in generating a Key that can be used to encrypt and decrypt their passwords. It runs comepletly locally and uses basic commmands with arguments to run.

GEN randomly generates a key using pythons secrets library at a specified location or at the default.

INPUTK takes a path as its parameter and loads the .bin file to be used to either encrypt or decrypt passwords.

ENCRYPT uses the current key either generated or loaded to encrypt a password.

DECRYPT uses the current key either generated or loaded to Decrypt a password.

Finally, SAVE saves all encrypted passwords in a .enc file.

You can stop the program at anytime with QUIT.


LIMITATIONS:

This program is for educational purposes only! It is intended for learning about encryption concepts and Python programming. It is not a secure encryption for REAL passowrds.

The encryption method used(XOR with a single key) is cryptographically weak and can be easily broken. Do not use this tool for securing sensitive information, online accounts, or real passwords.

WARNING! Losing the key file will make encrypted passwords unrecoverable. Storing the key insecurely compromises all encrypted data.


ETHICAL CONSIDERATIONS:

This program could technically be used or modified to encypt or hide data by malicious users.

IF people didn't read the README people could mistakingly believe this encyption to be safe. This doesn't actually provide all that much safety.

A key based system like this is always going to be vulnerable. Unless the person safe gaurds the key file properly it is fully possible to un-encrypt everything.