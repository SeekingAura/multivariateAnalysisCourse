
import sys
import pyreadstat

df, meta = pyreadstat.read_sav(sys.argv[1])

print(df["PRODUCTO"])