def run_length_encoding(seq):
    compressed = []
    count = 1
    char = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == char:
            count = count + 1
        else:
            compressed.append([char, count])
            char = seq[i]
            count = 1
    compressed.append([char, count])

    compressed_seq = ''
    for i in range(0, len(compressed)):
      for j in compressed[i]:
        compressed_seq += str(j)

    return compressed_seq

seq = input("Intorduce a sequence : e.g. AACCCBBBBBAAAAFFFFFFFF \n")
list1 = run_length_encoding(seq)
print("Sequence after encoding: ", list1)