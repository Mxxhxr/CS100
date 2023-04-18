def file_copy(in_file, out_file):
    iFile = open(in_file, 'r')
    oFile = open(out_file, 'a')
    for line in iFile:
        oFile.write(line.strip() + '\n')

    iFile.close()
    oFile.close()
