# L-AES-128-Light-AES-128-Encrytion:

The L-AES-128 is similar to AES except that each round of processing involves the following three steps:
- byte-by-byte substitution using S-box 
- shifting of the rows of the state array
- The addition of the round key.
Output:
- A txt file named out_a1.txt with the results ciphertext in Base64 format.
- A txt file named out_a2.txt with the results of avalanche effect test.

For part 2, I wrote a Python code to encrypt the same message using the same key, twice, once in CFB-64bit (s=64) mode, then in OFB mode. 
