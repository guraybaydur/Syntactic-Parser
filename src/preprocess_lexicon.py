

def read_terminals(directory='../', file='terminal_lexicon.txt'):
    terminals = {}
    with open(directory + file, 'r', encoding='utf8') as f:
        for line in f:
            line_list = line.split() # 0 --> terminal 1 --> POS
            if line_list[1] not in terminals.keys():
                key = line_list[1]
                terminals[key] = []
            terminals[key].append(line_list[0])
    return terminals


def read_grammar