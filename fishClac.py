fish = 6
bigWz = fish/4
smlWz = 2
join = smlWz + smlWz

def small_pieces(n):
    pieces = ((fish % bigWz) * n) / smlWz
    print(pieces)


def all_pieces(n):
    small_bits = (fish % bigWz) *n
    big_bits = (fish *n) / bigWz
    fill_bits = (fish*n) / smlWz

    print(small_bits, big_bits, fill_bits)

small_pieces(6)
all_pieces(120)

