import primechecker

def main():
    for i in range(0, 1):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i == 0 and j == 0 and k == 0: continue
                    if i == 1 or j == 1 or k == 1 or l == 1: continue
                    if i == 7 or j == 7 or k == 7 or l == 7: continue
                    if i + j + k + l > 10: continue
                    if k % 2 != 0: continue
                    if (i + j % 2 == 0): continue
                    if not primechecker.is_prime(int(str(i) + str(j) + str(k) + str(l))): continue
                    return int(str(i) + str(j) + str(k) + str(l))

if __name__ == '__main__':
    print main()