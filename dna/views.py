from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
    return render(request, 'dna/main.html', context)


def result(request):
    sequence = request.GET['sequence']
    comp_pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complementing_strand = ""
    for i in range(len(sequence)-1, -1, -1):
        complementing_strand += comp_pairs[sequence[i]]

    mRNA=""
    sequence = request.GET['sequence']
    for i in sequence:
        if i not in 'ATGC':
            mRNA = "Invalid Input"
            break
        if i == 'A':
            mRNA += 'U'
        elif i == 'C':
            mRNA += 'G'
        elif i == 'T':
            mRNA += 'A'
        else:
            mRNA += 'C'

    tRNA = ""
    for i in mRNA:
        # if i not in 'ATGC':
        #     tRNA = "Invalid Input"
        #     break
        if i == 'G':
            tRNA += 'C'
        if i == 'C':
            tRNA += 'G'
        if i == 'A':
            tRNA += 'U'
        if i == 'U':
            tRNA += 'A'
    return render(request, 'dna/result.html', {'comp_strand':complementing_strand, 'mRNA': mRNA, 'tRNA':tRNA})


