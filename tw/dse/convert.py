import re

def process_file(filename):
    label_rx = re.compile(r'^label\s+(\w+)\s*:\s*');

    labels = [];

    with open(filename, 'r') as f:
        curr_label = None

        for lin in f:
            match = label_rx.match(lin)
            if match:
                curr_label = {
                    'label': match.group(1),
                    'body' : ''
                }
                labels.append(curr_label)

    return labels


sections = process_file('game/main.rpy')
print(sections)
