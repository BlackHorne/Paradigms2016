def strip(inname, outname):
    f_in = open(inname, 'r')
    f_out = open(outname, 'w')
    for string in f_in:
        if string.count('[strip]') == 0:
            f_out.write(string)
    f_in.close()
    f_out.close()
    return
