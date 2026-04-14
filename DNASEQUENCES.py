def validate_dna(sequence):

    if sequence == "":
        return False


    sequence = sequence.upper()
    allowed = "ATCG"

    for char in sequence:
        if char not in allowed:
            return False  # Found a bad character, stop immediately

    return True


def count_bases(sequence):

    seq = sequence.upper()
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for char in seq:
        if char == 'A':
            counts['A'] += 1
        elif char == 'T':
            counts['T'] += 1
        elif char == 'C':
            counts['C'] += 1
        elif char == 'G':
            counts['G'] += 1

    return counts


def find_codon(sequence, codon):
    seq = sequence.upper()
    target = codon.upper()
    foundat = []


    for i in range(len(seq) - 2):
        if seq[i: i + 3] == target:
            foundat.append(i)

    return foundat

def calculate_gc_content(sequence):
    if len(sequence) == 0:
        return 0.0

    seq = sequence.upper()
    gc_count = 0

    for char in seq:
        if char == 'G' or char == 'C':
            gc_count += 1

    percent = (gc_count / len(seq)) * 100
    return round(percent, 2)

userseq = input("Enter DNA sequence: ")

if validate_dna(userseq) == False:
    print("Error: This is not a valid DNA sequence.")
else:

    my_counts = count_bases(userseq)
    my_gc = calculate_gc_content(userseq)

    starts = find_codon(userseq, "ATG")

    taa_list = find_codon(userseq, "TAA")
    tag_list = find_codon(userseq, "TAG")
    tga_list = find_codon(userseq, "TGA")
    all_stops = taa_list + tag_list + tga_list
    all_stops.sort()

    mulof3 = (len(userseq) % 3 == 0)

    print("REPORT")
    print("Sequence Length:", len(userseq))
    print("Multiple of 3:", mulof3)
    print("GC Content:", my_gc, "%")
    print("Base Counts:", my_counts)
    print("ATG Start Positions:", starts)
    print("Stop Codon Positions:", all_stops)

