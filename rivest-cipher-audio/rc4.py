#!/usr/bin/env python
import wave

#RC4 Encryption Function
def encrypt(key, plainfile, cipherfile):
    '''
    RC4 Encryption function: 
    (str, file, fil) -> None
    Read plaintext/audio from plainfile and encrypt
    the data into cipherfile using the given key
    '''
    cipherfile = crypt(key, plainfile, cipherfile)       

#RC4 Decryption Function
def decrypt(key, cipherfile, decryptfile):
    '''
    RC4 Decryption function: 
    (str, file, fil) -> None
    Read plaintext/audio from cipherfile and decrypt
    the data into decryptfile using the given key
    '''
    decryptfile = crypt(key, cipherfile, decryptfile)
    
#Helper function
def crypt(key, inputFile, outputFile):
    '''
    Helper function that takes the key, InputFile and OutputFile
    applies the key to the InputFile and returns the resulted
    text in the OutputFile
    '''
    #Checks if input file is a wave file
    if (inputFile.endswith(".wav")):
        inWave = wave.open(inputFile, 'rb')
        
        length = inWave.getnframes()
        inputByte = ""
        
        # Writes each frame into a variable
        for i in range(length):
            inputByte += inWave.readframes(1)
    else:
        with open(inputFile, 'rb') as myfile:
            # Writes the text into a variable
            inputByte = myfile.read()
    
    # calls keySchedule function 
    # KeySchedule function initializes the permutation in key
    S = keySchedule(key)
    i = 0
    j = 0
    outputByte = ""
    
    #outputs the keystream
    for c in inputByte:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        
        t = (S[i] + S[j]) % 256
        outputByte += (chr(ord(c) ^ S[t]))
    
    # Write the produced plain/cipher text into the output files
    if(outputFile.endswith(".wav")):
        outWave = wave.open(outputFile, 'wb')
        #Set Wave file's params 
        outWave.setparams(inWave.getparams())
        outWave.writeframes(outputByte)
        outWave.close()
        inWave.close()
    else:
        with open(outputFile, "wb") as myfile:
            myfile.write(outputByte)
                
   
def keySchedule(key):
    '''
    Initialize the permutation in the array S with the size of 256-bit
    '''
    S = range(256)
    T = range(256)
    
    for i in range(256):
        S[i] = i
        T[i] = key[i % len(key)]

    j = 0
    for i in range(256):
        j = (j + S[i] + ord(T[i])) % 256
        S[i], S[j] = S[j], S[i]
   
    return S
