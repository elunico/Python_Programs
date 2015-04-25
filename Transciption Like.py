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
from __future__ import print_function
import random

DNA = '5acgtcgactgcaaatgatttattcgacaacgttcatcatcga3'\
      '3tgcagctgacgtttactaaataagctgttggaagtagtagct5'
STOPS = ['aat', 'aag', 'aac'] # These are not the actual stop codons, they are only used as examples
COMPL = {'a':'u', 't':'a', 'c':'g', 'g':'c'}


def helicase(dna):
    split = DNA.split('33')
    split[1] = [split[1][i] for i in range(len(split[1]) -1, -1, -1)]
    split[1] = ''.join(split[1])
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
    leninuse = len(i) - 1
    indexes = find(s, i)
    code = ''
    j = -1
    while g not in code:
        j += 1
        code = i[indexes[j]:leninuse-1]
    return [indexes[j], leninuse-1]

def findStop(sec, c):
    for i in STOPS:
        if i in c:
            j = c.index(i)
            return j * 3 + 3

def polymerase(template, position, cods):
    mRNA = ''
    section = template[position[0]:position[1]]
    print (section)
    stop = findStop(section, cods)
    section = section[:stop]
    print (section)
    for i in section:
        mRNA += COMPL[i]
    mRNA = '|5-' + mRNA[:]
    mRNA += '-3|'
    return mRNA

def transcribe(dna, gene):
    strands = helicase(DNA)
    codons = []
    genecodons = []
    for i in strands:
        for j in range(0, len(i) - 1, 3):
            codons.append('{0}{1}{2}'.format(i[j], i[j+1], i[j+2]))

    for thing in range(0, len(gene) - 1, 3):
        genecodons.append('{0}{1}{2}'.format(gene[thing], gene[thing+1], gene[thing+2]))

    inuse, strandnum = findGene(strands, gene)

    start = gene[0:3]

    position = getCode(inuse, gene, start)

    if strandnum == 0:
        strands[1] = [strands[1][i] for i in range(len(strands[1]) -1, -1, -1)]
        strands[1] = ''.join(strands[1])
    elif strandnum == 1:
        strands[0] = [strands[0][i] for i in range(len(strands[0]) -1, -1, -1)]
        strands[0] = ''.join(strands[0])
    if inuse == -1:
        return -1

    mRNA = polymerase(strands[abs(strandnum-1)], position, genecodons)

    return mRNA


def main():
    gene = ['acgtcgactgcaaat', 'ttattcgacaac', 'tcgatgatgaag']
    ind = random.randrange(0, len(gene))
    mRNA = transcribe(DNA, gene[ind])
    print ('DNA:', DNA, '\n\n' + 'Gene:', gene[ind], '\nmRNA:', mRNA, end=' ')
    print ('\nEquivalent:', gene[ind].replace('t', 'u') == mRNA.strip('|').strip('3').strip('5').strip('-')) # Stripped because mRNA is structurally different than a DNA gene sequence 


if __name__ == '__main__':
    main()
