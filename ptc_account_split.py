import getopt, sys
from datetime import datetime

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:o:v", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    filename = None
    outputfile = "accounts_"
    verbose = False
    num_to_split = 50
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--filename"):
            filename = str(a)
        elif o in ("-o","--output"):
            outputfile = str(a)
        elif o in ("-n","--number"):
            num_to_split = int(a)
        else:
            assert False, "unhandled option"
    #print filename
    y = file_len(filename)
    #print y
    fd = open(filename,"r")
    d = datetime.now().strftime('%Y-%m-%d')
    write_fn = outputfile + str(d) + "_"
    write_count = 0
    read_count = 0
    num_to_index = num_to_split + 1
    while read_count < y:
        wr_fn = write_fn + str(write_count) + ".txt"
        fw = open(wr_fn,"w")
        for i in xrange(1,num_to_index):
            a = fd.readline()
            fw.write(a)
        write_count += 1
        read_count += num_to_split

     


if __name__ == "__main__":
    main()
