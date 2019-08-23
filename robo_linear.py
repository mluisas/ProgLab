sequence = input('Commands: Ex: TFTFFT \n').upper()
# The loop will continue until only one of the letters is in sequence
while 'F' in sequence and 'T' in sequence:
    sequence = sequence.replace('TF', '')
    sequence = sequence.replace('FT', '')
# As there is only one of the letters, the string length is equal to the number of steps
size = len(sequence)
if size == 0:
    print('No steps')
elif sequence[0] == 'F':
    print('{} steps forward'.format(size))
elif sequence[0] == 'T':
    print('{} steps back'.format(size))
else:
    print('Your input is incorrect. Please, try again')
