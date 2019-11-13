import pandas as pd

x = pd.read_csv("../prog/output_data/clones.dat", sep='\t')
print(x)
## print(x[['Generation', 'NumCells', 'S1(MeanNum)', 'S2(MeanNum)', 'S3(MeanNum)']])
