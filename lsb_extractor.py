
# I'm aware that this is not the best solution and I also know that it could be written in more "Python" way. 
# Its purpose is to teach fundamentals of extracting LSB from a file. 

binary_data = open("blank.bmp","rb") # "rb" opening data in binary mode
binary_data.seek(60)  # this will change current file stream position
data = binary_data.read() # read() method returns the number of bytes from a file where default is -1 e.i. the whole file
list_for_LSB = [] #creating empty list

for byte in data:
    list_for_LSB.append(bin(byte)[-1])  #make a list of LS bits

for i in range(0,170,8):
    arr_of_8_bits = list_for_LSB[i:i+8]
    joint_of_arr_values= ''.join(arr_of_8_bits)
    integer_value = int(joint_of_arr_values,2)
    print(chr(integer_value), end='')




