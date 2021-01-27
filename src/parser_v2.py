from preprocess_lexicon import load_rules


def parse_sentence(rules, sentence, parse='sentence'):
    if parse == 'sentence':
        terms = sentence.lower().split()
        phrasal_index = []
    else:
        terms = sentence.split('-')
    table = [[[] for x in range(j + 1)] for j in range(len(terms))]  # generate upper triangular of the table
    for j in range(len(terms)):
        try:
            table[j][j] = [rules[terms[j]]]
        except KeyError:
            if '-' in terms[j]:
                #keep track of phrasal terminals
                phrasal_index.append(j)
                _, word_parse = parse_sentence(rules, terms[j], parse='word')
                temp_list = [i[0] for i in word_parse]
                table[j][j] = temp_list
            else:
                print('Terminal not in the lexicon, can\'t parse')
                break
        for i in reversed(range(j)):
            # (i,i)x(j,i+1) tüm kombinasyonlarını ara j,i'ye yaz
            # i,k x k,j
            for x in table[i][i][0]:
                for y in table[j][i+1][0]:
                    if type(y) != list and y != None and type(x) != list and x != None:
                        temp_key = x + ' ' + y  # in order not to take subclauses i.e. [NP [NOUN DS]] here only take NP
                        try:
                            temp_list = rules[temp_key]
                        except KeyError:
                            continue
                        for k in range(len(temp_list)):
                            table[j][i].append([temp_list[k], [temp_key]])

            if len(table[j][i]) == 0:  # if no combination of two elements found, insert None
                table[j][i].append([None])

    #postprocess missing
    parse_column = table[len(terms)-1]

    return table, parse_column


if __name__ == '__main__':
    sentence2 = 'Dün arkadaş-ım-a bir hediye al-dı-m'
    rules = load_rules()
    parse, parse_list = parse_sentence(rules, sentence2)