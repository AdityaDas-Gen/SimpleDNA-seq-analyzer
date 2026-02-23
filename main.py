# DNA Sequence Analyzer
# Author: Aditya Das
# Description: Reads a DNA sequence from a file and calculates nucleotide composition.



from collections import Counter

file_path = " #your file path goes here "

def read_seq():
    parts = []
    with open(file_path,"r") as file:
        for line in file:
            parts.append(line.strip())
    dna = "".join(parts)

    return dna

def analyse_seq():
    seq = read_seq()

    counts = Counter(seq)

    total_length = sum(counts.values())

    A, T, G, C = counts["A"], counts["T"], counts["G"], counts["C"]


      # Percentages
    analyzed_data = { "A_percentage" : round(A/total_length * 100,2),
                      "T_percentage" : round(T/total_length * 100,2),
                      "G_percentage" : round(G/total_length * 100,2),
                      "C_percentage" : round(C/total_length * 100,2),
                      "GC_percentage" : round(G/total_length * 100 + C/total_length * 100,2),
                      "AT_percentage" : round(A/total_length * 100 + T/total_length * 100,2),
                      "Purine" : round(G/total_length * 100 + A/total_length * 100,2),
                      "Pyrimidine" : round(T/total_length * 100 + C/total_length * 100,2)
    }

    return total_length,analyzed_data,counts

def display (total_length,analyzed_data,counts):
    print("---------------------------------------")
    print(f"{total_length} total numbers of nt")
    print("---------------------------------------")
    for key,value in counts.items():
        print(f"{key} = {value}")
    print("---------------------------------------")
    for key,value in analyzed_data.items():
        print(f"{key} = {value}%")

total_length, analyzed_data, counts = analyse_seq()
display(total_length, analyzed_data, counts)

