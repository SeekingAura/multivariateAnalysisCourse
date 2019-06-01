import pyreadstat

if(len(sys.argv)!=3):
    sys.stderr.write('Usage: "{0}" $csvFileName $IndexOfX1 (csv headers should be must otherThink0, otherThink1, ... , otherThinnkn, "x1", "x2", ..., "xn", "Y")\n'.format(sys.argv[0]))
    os._exit(1)

if(".csv" in sys.argv[1]):
    data = pd.read_csv(sys.argv[1])
else:
    data, meta = pyreadstat.read_sav(sys.argv[1])

    