def append_bits(x, L):
    return [x + element for element in    L]

def generate_bit(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (append_bits("0", generate_bit(n - 1)) + 
                append_bits("1", generate_bit(n - 1)))
                
print(generate_bit(3))
