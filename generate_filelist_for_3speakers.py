import json

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


lada_path = '/home/yehor/RADTTS-Multiple-Voices/datasets/lada/accept'
with open('/home/yehor/RADTTS-Multiple-Voices/datasets/lada/metadata.jsonl') as x:
    for jsonline in x:
        row = json.loads(jsonline.strip())
        
        raw_text = row['orig_text']
        fixed_text = raw_text.replace('—','').replace('  ', ' ').lower().strip()
        fixed_text = replace_accents(fixed_text)

        filepath = lada_path + '/' + row['file']

        print(f'{filepath}|{fixed_text}|lada')


mykyta_path = '/home/yehor/RADTTS-Multiple-Voices/datasets/mykyta/accept'
with open('/home/yehor/RADTTS-Multiple-Voices/datasets/mykyta/metadata.jsonl') as x:
    for jsonline in x:
        row = json.loads(jsonline.strip())
        
        raw_text = row['orig_text']
        fixed_text = raw_text.replace('—','').replace('  ', ' ').lower().strip()
        fixed_text = replace_accents(fixed_text)

        filepath = mykyta_path + '/' + row['file']

        print(f'{filepath}|{fixed_text}|mykyta')


tetiana_path = '/home/yehor/RADTTS-Multiple-Voices/datasets/tetiana/accept'
with open('/home/yehor/RADTTS-Multiple-Voices/datasets/tetiana/metadata.jsonl') as x:
    for jsonline in x:
        row = json.loads(jsonline.strip())
        
        raw_text = row['orig_text']
        fixed_text = raw_text.replace('—','').replace('  ', ' ').lower().strip()
        fixed_text = replace_accents(fixed_text)

        filepath = tetiana_path + '/' + row['file']

        print(f'{filepath}|{fixed_text}|tetiana')
