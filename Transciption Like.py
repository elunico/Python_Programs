#!/usr/bin/python
# -*- Coding: utf-8 -*-

# Thomas Povinelli
# Transciption Like.py

# I know this could be a much simpler program
# obviously this is totally out of the way
# but I was trying to more accurately simulate
# biological processes such as the use of helicase
# and the template strands to replicate essentially
# the same sequence.

# Please don't think I made this with efficiency in
# mind


DNA = "5acgtcgactgcaaatgatttattcgacaacgcgcatcatcga33tgcagctgacgtttactaaataagctgttgcgcgtagtagct5"
STOPS = ["aat", 'aag', 'aac']
COMPL = {'a':'u', 't':'a', 'c':'g', "g":'c'}


def helicase(dna):
    split = DNA.split('33')
    #split[1] = [split[1][i] for i in range(len(split[1]) -1, -1, -1)]
    #split[1] = "".join(split[1])
    split[0] = split[0].strip('5')
    split[1] = split[1].strip('5')
    return split

def findGene(strand, gene):
    if gene in strand[0]:
        k = 0
        inuse = strand[0]
    elif gene in strand[1]:
        k = 1
        inuse = strand[1]
    else:
        return -1
    return inuse, k

def find(ch,string1):
    pos = []
    for i in range(0, len(string1)-3, 3):
        if ch == string1[i:i+3]:
            pos.append(i)
    return pos

def getCode(i, g, s):
    leninuse = len(g)
    indexes = find(s, i)
    code = ""
    j = -1
    while g not in code:
        j += 1
        code = g[indexes[j]:leninuse]
    return [indexes[j], leninuse]

def findStop(sec, c):
    for i in STOPS:
        if i in c:
            j = c.index(i)
            return (j * 3)

def polymerase(template, position, cods):
    mRNA = ''
    section = template[position[0]:position[1]]
    stop = findStop(section, cods)
    section = section[:stop]
    for i in section:
        mRNA += COMPL[i]
    return mRNA

def transcribe(dna, gene):
    strands = helicase(DNA)
    codons = []
    for i in strands:
        for j in range(0, len(i) - 1, 3):
            codons.append("{0}{1}{2}".format(i[j], i[j+1], i[j+2]))

    inuse, strandnum = findGene(strands, gene)
    if inuse == -1:
        return -1

    start = gene[0:3]

    position = getCode(inuse, gene, start)

    mRNA = polymerase(strands[abs(strandnum-1)], position, codons)

    return mRNA


def main():
    gene = 'acgtcgactgcaaat'
    mRNA = transcribe(DNA, gene)
    print gene, mRNA
    print gene[:-3].replace('t', 'u') == mRNA


if __name__ == '__main__':
    main()
