

def read_terminals(directory='../', file='terminal_lexicon.txt'):
    terminals = {}
    with open(directory + file, 'r', encoding='utf8') as f:
        for line in f:
            line_list = line.split() # 0 --> terminal 1 --> POS
            if line_list[0] not in terminals.keys():
                terminals[line_list[0]] = []
            terminals[line_list[0]].append(line_list[1])

    return terminals


def read_grammar(directory='../', file='grammar_rules.txt'):
    grammar = {}
    with open(directory+file, 'r', encoding='utf8') as f:
        for line in f:
            line_list = line.split('-->')
            key = line_list[1].strip()
            if key not in grammar.keys():
                grammar[key] = []
            grammar[key].append(line_list[0].strip())

    return grammar


def read_suffixes(directory='../', file='suffix_list.txt'):
    suffixes = {}
    with open(directory+file, 'r', encoding='utf8') as f:
        for line in f:
            line_list = line.split('-->')
            key = line_list[1].strip()
            if key not in suffixes.keys():
                suffixes[key] = []
            suffixes[key].append(line_list[0].strip())

    return suffixes

def combine_dicts(x, y, z):
    t = x.copy()
    for i in y.keys():
        if i in t.keys():
            t[i].append(y[i])
        else:
            t[i] = y[i]
    for i in z.keys():
        if i in t.keys():
            t[i].extend(z[i])
        else:
            t[i] = z[i]
    return t

def load_rules():
    terminals = read_terminals()
    grammar = read_grammar()
    suffixes = read_suffixes()
    rules = combine_dicts(terminals, grammar, suffixes)
    return rules

if __name__ == '__main__':
    terminals = read_terminals()
    grammar = read_grammar()
    suffixes = read_suffixes()
    rules = combine_dicts(terminals, grammar, suffixes)


