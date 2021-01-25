from preprocess_lexicon import load_rules


rules = load_rules()
sentence = 'Ben okul a git ti m'
terms = sentence.lower().split()

table = [[[] for x in range(j+1)] for j in range(len(terms))]  # generate upper triangular of the table
hor_ind = 1
ver_ind = 0

for j in range(len(terms)):
    try:
        table[j][j] = [rules[terms[j]]]
    except KeyError:
        print('Terminal not in the lexicon, can\'t parse')
        break
    for i in reversed(range(j)):
        # (i,i)x(j,i+1) tüm kombinasyonlarını ara j,i'ye yaz
        #
        combs = []
        for x in table[i][i]:
            for y in table[j][i+1]:
                temp_key = x[0] + ' ' + y[0]
                try:
                    temp_list = rules[temp_key]
                except KeyError:
                    continue
                for k in range(len(temp_list)):
                    table[j][i].append([temp_list[k], [temp_key]])

#1stSgl and 1stSglPos should be modified, one has to be removed
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
parse_list = table[len(terms)-1]
tree = ''
count = 0
for i in parse_list:
    tree += '[' + i[0][0]
    if count < len(parse_list) - 1:
        temp_level = i[0][1][0].split()
        tree +=  ' [' + temp_level[0] + ' '
        count += 1
    else:
        for j in range(count):
            tree += ']'

print(tree)