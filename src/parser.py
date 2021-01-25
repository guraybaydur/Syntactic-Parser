from preprocess_lexicon import load_rules



def parse_sentence(rules, sentence):
    terms = sentence.lower().split()
    table = [[[] for x in range(j + 1)] for j in range(len(terms))]  # generate upper triangular of the table
    for j in range(len(terms)):
        try:
            table[j][j] = [rules[terms[j]]]
        except KeyError:
            print('Terminal not in the lexicon, can\'t parse')
            break
        for i in reversed(range(j)):
            # (i,i)x(j,i+1) tüm kombinasyonlarını ara j,i'ye yaz
            for x in table[i][i][0]:
                for y in table[j][i+1][0]:
                    if type(y) != list and y != None:
                        temp_key = x + ' ' + y  # in order not to take subclauses i.e. [NP [NOUN DS]] here only take NP
                        try:
                            temp_list = rules[temp_key]
                        except KeyError:
                            continue
                        for k in range(len(temp_list)):
                            table[j][i].append([temp_list[k], [temp_key]])

            if len(table[j][i]) == 0:  # if no combination of two elements found, insert None
                table[j][i].append([None])
    return table, table[len(terms)]


#Decoding the parse, only parses the first possibility for now
# z
# # ├── c
# # │   ├── a
# # │   └── b
# # ├── d
# # ├── e
# # │   └── asdf
# # └── f
# Bu şekilde basmaya çalışıcam tree'yi
def bracket_form_parse(parse_list):
    bracket_form = ''
    count = 0
    for i in parse_list:
        bracket_form += '[' + i[0][0]
        if count < len(parse_list) - 1:
            temp_level = i[0][1][0].split()
            bracket_form += ' [' + temp_level[0] + ' '
            count += 1
        else:
            for j in range(count):
                bracket_form += ']'
    return bracket_form


#from bracket to tree
def tree_form_parse(bracket_form):
    tree = ''
    take = False
    temp_str = ''
    for i in bracket_form:
        if i == '[':
            take = True
        # if take


if __name__ == '__main__':
    rules = load_rules()
    sentence = 'Ben okul a git ti m'
    sentence2 = 'Dün arkadaş ım a bir hediye al dı m'
    parse_table, parse_list = parse_sentence(rules, sentence2)
    bracket_form = bracket_form_parse(parse_list)
    print(bracket_form)
