def replace_accents(x):
    chars = list(x.encode('utf-8').replace(b'\xcc\x81', b'+').decode('utf-8'))

    final_chars = []
    for i, c in enumerate(chars):
        if c == '+':
            try:
                tmp = final_chars[i - 1]

                final_chars.pop()
                final_chars.append('+')
                final_chars.append(tmp)
            except IndexError:
                final_chars.append(c)
        else:
            final_chars.append(c)

    return ''.join(final_chars)


with open('filelists/original_lada_ukrainian_train_filelist.txt') as x:
    for l in x:
        l = l.strip()
        s = l.split('|')
        fixed = s[1].replace('—','').replace('  ', ' ').lower().strip()
        fixed = replace_accents(fixed)
        print(f'{s[0]}|{fixed}|{s[2]}')
