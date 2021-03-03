def base10_valueGenerator(input_string, data):
    if len(input_string) % 2 == 0:
        split1 = input_string[:len(input_string)//2]
        split2 = input_string[len(input_string)//2:]
        print(split1)

        x = 2
        res1 = [split1[y-x:y] for y in range(x, len(split1) + x, x)]
        res2 = [split2[y-x:y] for y in range(x, len(split1) + x, x)]

        val1 =[]
        val2 =[]

        for i in res1:
            if i in data:
                val1.append(data[i])
            else:
                val1.append(alaphabets_dict[i])

        for i in res2:
            if i in data:
                val2.append(data[i])
            else:
                val2.append(alaphabets_dict[i])

        the_base10_split1 = 0
        the_base10_split2 = 0
        for i in range(len(val1)):
            the_base10_split1 += val1[i]*26**(len(val1)-i-1)

        for i in range(0, len(val2)):
            the_base10_split2 += val2[i]*26**(len(val2)-i-1)

        total_base10 = the_base10_split1 + the_base10_split2
        print(f'{split1}({the_base10_split1})')
        print(f'{split2}({the_base10_split2})\n')
        return total_base10

    else:
        return 0


def base26_valueGenrator(d1, d2, ls):
    run1, run2 = True, True
    d1_quo = d1
    d2_quo = d2

    val1_alph =''
    val2_alph =''

    while run1 or run2:
        if run1:
            d1_rem = d1_quo%26
            d1_quo = int(d1_quo/26)
            for key,value in ls.items():

                if value == d1_rem:
                    val1_alph = key + val1_alph
                if value == d1_quo:
                    val1_alph = key +val1_alph
                    run1 = False

        if run2:
            d2_rem = d2_quo%26
            d2_quo = int(d2_quo/26)
            for key,value in ls.items():
                if value == d2_rem:
                    val2_alph = key + val2_alph

                if value == d2_quo:
                    val2_alph = key + val2_alph
                    run2 = False
    print(f'{d1}({val1_alph})')
    print(f'{d2}({val2_alph})\n')

    return val1_alph+val2_alph




def create_base26_table():
    alaphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    val = 0
    data = {}

    for n in range(len(alaphabets)):
        data[f'{alaphabets[n]}'] = val
        val += 1

    for n in range(len(alaphabets)):
        for m in range(len(alaphabets)):
            data[f'{alaphabets[n]}{alaphabets[m]}'] = val
            val += 1
    return data

def start_prog():
    data = create_base26_table()
    user_input = input('Type 1 for base26 to base10 conversion or Type 2 for base10 to base26 conversion:\n')
    if user_input == '1':
        alaphabet = input('Enter the alphabet\n')
        alaphabet = alaphabet.upper()
        base10_val = base10_valueGenerator(alaphabet, data)
        print(base10_val)

    elif user_input == '2':
        d1 = int(input('Enter first base10 value\t'))
        d2 = int(input('Enter secodn base10 value\t'))

        base26_val = base26_valueGenrator(d1, d2, data)
        print(base26_val)

    else:
        print('Wrong Input')
        start_prog()



start_prog()
