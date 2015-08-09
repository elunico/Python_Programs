from __future__ import print_function
import random
import sys
import tcolors # not a built-in module

BASES = ['a', 'g', 'c', 't']
AMINOS = {'ttt': 'phe', 'ttc': 'phe', 'ctt': 'leu', 'ctc': 'leu', 'cta': 'leu',
          'ctg': 'leu', 'att': 'ile', 'atc': 'ile', 'ata': 'ile', 'atg': 'met',
          'gtt': 'val', 'gtg': 'val', 'gta': 'val', 'tct': 'ser', 'tcc': 'ser',
          'tca': 'ser', 'tcg': 'ser', 'cct': 'pro', 'ccc': 'pro', 'cca': 'pro',
          'ccg': 'pro', 'act': 'thr', 'acc': 'thr', 'aca': 'thr', 'acg': 'thr',
          'gct': 'ala', 'gcc': 'ala', 'gca': 'ala', 'gcg': 'ala', 'tat': 'tyr',
          'tac': 'tyr', 'taa': 'stp', 'tag': 'stp', 'cat': 'his', 'cac': 'his',
          'caa': 'gln', 'cag': 'gln', 'aat': 'asn', 'aac': 'asn', 'aaa': 'lys',
          'aag': 'lys', 'gat': 'asp', 'gac': 'asp', 'gaa': 'glu', 'gag': 'glu',
          'tgt': 'cys', 'tga': 'stp', 'tgg': 'trp', 'cgt': 'arg', 'cgc': 'arg',
          'cga': 'arg', 'cgg': 'arg', 'agt': 'ser', 'agc': 'ser', 'aga': 'arg',
          'agg': 'arg', 'ggt': 'gly', 'ggc': 'gly', 'gga': 'gly', 'ggg': 'gly',
          'tta': 'leu', 'ttg': 'leu', 'gtc': 'val', 'tgc': 'cys'}

def warn(msg):
    print(tcolors.warn + msg + tcolors.end)


def makeDNA(length):
    a = ""
    for i in range(length):
        a += random.choice(BASES)
    return a


def breakUp(dna):
    bases = []
    for i in range(0, len(dna), 3):
        new_code = ""
        new_code = new_code + dna[i] + dna[i + 1] + dna[i + 2]
        bases.append(new_code)
    return bases


def translateBases(bases):
    # protein = ""
    polypep = []
    for i in bases:
        amino = AMINOS[i]
        polypep.append(amino)
        if amino == 'stp':
            break
    return "-".join(polypep)


def mutateDNA(count, prob, dna=""):
    if not dna:
        dna = makeDNA(900)
    new_dna = ob = op = nb = np = ""
    op = np = translateBases(breakUp(dna))
    for i in range(count):
        if random.randint(0, 1000) < prob:
            pos = random.randint(0, (len(dna) - 1))
            new_dna = dna[:pos] + random.choice(BASES) + dna[pos + 1:]
            ob = breakUp(dna)
            nb = breakUp(new_dna)
            op = translateBases(ob)
            np = translateBases(nb)
            if op != np:
                print("Protein Mutation!")
                print(op)
                print("-" * 79)
                for j in range(len(np)):
                    try:
                        if np[j] != op[j]:
                            print(tcolors.red, end='')
                        else:
                            print(tcolors.black, end='')
                    except IndexError:
                        pass
                    print(np[j], end='')
                print(tcolors.black)
                print()
                print("After %i of the possible %i turns" % (i+1, count))
                return (new_dna, ob, nb, op, np, i, count)
    print(op)
    print("-" * 79)
    print(np)
    print()
    print("No protein change after %i turns" % count)
    return (new_dna, ob, nb, op, np, i, count)


def main(argc, argv):
    w = 0
    if argc < 4:
        raise SystemExit("Usage: "
                         "./tto DNA_Length Num_Of_Turns prob_in_1000")
    try:
        argv[1] = int(argv[1])
        argv[2] = int(argv[2])
        argv[3] = int(argv[3])
    except:
        raise SystemExit("Usage: "
                         "./tto DNA_Length Num_Of_Turns "
                         "prob_in_1000 **must be integers**")
    print()
    if argv[1] % 3 != 0:
        argv[1] = argv[1] // 3 * 3
        warn("WARNING: Length of DNA must be divisible"
             " by 3, rounding down to %i"
             % argv[1])
    if argv[3] <= 0:
        warn("WARNING: 0 probability (3rd arg) means "
             "no mutations can EVER occur in the DNA.")
    print()
    d = makeDNA(argv[1])
    mutateDNA(argv[2], argv[3], d)
    print("Note each 'turn' is a %i in 1000 chance that the DNA will mutate" %
          argv[3])
    print(tcolors.black)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
