
terminals = {}
with open('../terminal_lexicon.txt', 'r', encoding='utf8') as f:
    for line in f:
        line_list = line.split() # 0 --> terminal 1 --> POS
        if line_list[1] not in terminals.keys():
            key = line_list[1]
            terminals[key] = []
        terminals[key].append(line_list[0])