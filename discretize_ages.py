# dicretize_ages.py
# Author: Sharon Mizrahi
# Email: smizrahi@bu.edu
#
# takes an existing comma-delimited data 
# file containing an age attribute and creates 
# a new comma-delimited data file in which each 
# age value is replaced with the letter code for its bin.
#
#

infile_name = input('name of input file: ')
outfile_name = infile_name.split(".")

infile = open(infile_name, 'r')
outfile = open(outfile_name[0] + '_disc.' + outfile_name[-1], 'w')

for line in infile:
    line = line[:-1]
    fields = line.split(',')
    # age is the last field
    age = int(fields[-1])

    if age in range(0,13):
        fields[-1] = 'C'
    elif age in range(13, 20):
        fields[-1] = 'T'
    elif age in range(20, 36):
        fields[-1] = 'E'
    elif age in range(36, 61):
        fields[-1] = 'A'
    else: 
        fields[-1] = 'S'

    transformed = ','.join(fields)
    print(transformed, file=outfile)

infile.close()
outfile.close()


