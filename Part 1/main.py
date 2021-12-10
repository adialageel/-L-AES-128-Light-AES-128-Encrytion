from Laes import LAES, convertTextToMatrix, convertMatrixToText

if __name__ == '__main__':

    #this is the first part
    with open('AES-pair','r') as f:
        data = f.read()
        half = data.split()
        print(half[3])

    i = 0
    while i < 200:
        p = LAES(int(half[i], base=16))
        plaintext = half[i+1]
        encrypted = p.encrypt(int(plaintext, base=16))
        f = open("out_a1.txt", "a")
        f.writelines(str(hex(encrypted)))
        f.write("\n")
        i = i + 2
     #p = LAES(0x8670deb3fd4c2a6fffd96560b9d66647)
     #p = LAES(int(0x8670deb3fd4c2a6fffd96560b9d66647, base=16))
     #1afb3917e49ebe53246a7fe6220e43a3
     #0e63d33238cf5aa8fb0e6273f7026ef9
     #plaintext = hex(1afb3917e49ebe53246a7fe6220e43a3)
     
     #encrypted = p.encrypt(plaintext)
     #f = open("out_a1.txt", "a")
     #decrypted = p.decrypt(encrypted)
     #f.writelines(str(hex(encrypted)))
    #
     #plaintext1 = 0x48656c6c6f206576657279626f647921
     #plaintext2 = 0x68656c6c6f206576657279626f647921

    #this is second part of first question
     #key = 0xFDE8F7A9B86C3BFF07C0D39D04605EDD
     #obj1 = LAES(key)
     #res = obj1.bitDifferenceCheck(plaintext1, plaintext2)
     #f = open("out_a2.txt","w")
     #f.write(res)

