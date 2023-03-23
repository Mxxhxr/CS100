outfile = open('example.txt', 'w')

outfile.write('T')

outfile.write('his is the first line.')

outfile.write(' Still the first line...\n')

outfile.write('Now we are in the second line.\n')

outfile.write('Non string value like ' + str(5) + ' must be converted first.\n')

outfile.write('Non string value like {} must be converted first.\n'.format(5))

outfile.close()