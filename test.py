data = "00110000011110000011000101100011001100100011000001111000011001000011001000110000011110000011001101100100011001010011000001111000001100100110001000110010"

def split_data(l, data):
    for i in range(0, len(data), l):
        yield data[i:i+l]

def bin2ascii(s):
    count = 0
    for i in s:
        count *= 2
        count += 1 if (i=='1') else 0
    return chr(count)
        
data_splited = [a for a in split_data(8, data)]
message = map(bin2ascii, data_splited)

message = [450,210,990,690]
