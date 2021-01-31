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
            # i,k x k,j
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
    return table, table[len(terms)-1]


#Decoding the parse, only parses the first possibility for now
# Bu şekilde basmaya çalışıcam tree'yi
def bracket_form_parse(parse_list):
    bracket_form = ''
    # count = 0
    # TODO loop over second indices to include more than one parse
    if len(parse_list) > 1:
        parent = parse_list[0][0][0]  # parent node
        terminal = parse_list[0][0][1][0].split()[0]  # terminal child
        bracket_form = '[' + parent + ' [' + terminal + '] ' + bracket_form_parse(parse_list[1:]) + ']'
    else:
        parent = parse_list[0][0][0]
        bracket_form = ' [' + parent + ']'

    return bracket_form


#from bracket to tree
def tree_form_parse(bracket_form, depth):
    left_ind = bracket_form[1:].find('[')
    # returns -1 if no left bracket found which means we have reached to the end of the tree
    curr_depth = depth - bracket_form.count('[')//2
    if left_ind != -1:
        right_ind = bracket_form[1:].find(']')
        parent = bracket_form[1:left_ind]
        terminal = bracket_form[left_ind+2:right_ind+1]
        next_branch_start = bracket_form[left_ind+2:].find('[')
        tree = parent + '\n' + '\t'*curr_depth + '|--' + terminal + '\n' + '\t'*curr_depth + '|--' + tree_form_parse(bracket_form[next_branch_start+left_ind+2:], depth)
    else:
        right_ind = bracket_form.find(']')
        terminal = bracket_form[1:right_ind]
        tree = terminal

    return tree



if __name__ == '__main__':
    rules = load_rules()
    sentence = 'Ben okul a git ti m'
    sentence2 = 'Dün arkadaş ım a bir hediye al dı m'
    sentence3 = 'Tarihi roman lar ı keyifle oku yor um'
    sentence4 = 'Ben dün akşam yemek i için anne m e yardım et ti m'
    sentence5 = 'Destan lar milli kültür ümüz ü ve tarih imiz i anlat ır'
    sentence6 = 'Yaz meyve ler in den karpuz bence en güzel meyve dir'
    sentence7 = 'Bu akşam ki toplantı ya katıl acak mı s ınız'
    sentence8 = 'Bu ağaç ın alt ı n da her gece mehtap ı izle r di k' #TO BE REVISITED
    sentence9 = 'Siz bura y a en son nezaman gel di niz'
    sentence10 = 'anadolu n un dört yan ı medeniyet in beşik i dir'
    sentence11 = 'Orhun Abide ler i Türkçe n in ilk yazılı örnek ler i dir'
    sentence12 = 'Okul biz im köy e epeyce uzak ta y dı'
    sentence13 = 'Yüksek sesle müzik dinle me'
    sentence14 = 'Ben arkadaş ım a hediye al dı n'
    sentence15 = 'Tarihi bir roman lar oku du m'
    sentence16 = 'Dün babam a yardım et ecek im'
    sentence17 = 'Ben okul git ti m'
    sentence18 = 'Ben kitap oku n du'
    sentence19 = 'Ben okul da git ti m'


    parse_table, parse_list = parse_sentence(rules, sentence4)
    bracket_form = bracket_form_parse(parse_list)
    print(bracket_form)
    tree = tree_form_parse(bracket_form, bracket_form.count('[')//2)
    print(tree)

