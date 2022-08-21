
PLACE_HOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for i, name in enumerate(names):
    names[i] = name.strip('\n')

with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.readlines()


def replace_name(new_name, old_letter):
    new_letter = []
    for line in old_letter:
        new_line = line.replace(PLACE_HOLDER, new_name)
        new_letter.append(new_line)
    return new_letter


for name in names:
    with open(f'./Output/ReadyToSend/ready_letter_{name}.txt', 'w') as file:
        updated_letter = replace_name(name, letter)
        file.write(''.join(updated_letter))
