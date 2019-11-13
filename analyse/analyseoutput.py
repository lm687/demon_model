import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("../prog/output_data/output.dat", sep='\t')
print(x[['Generation', 'NumCells', 'S1(MeanNum)', 'S2(MeanNum)', 'S3(MeanNum)']])

plt.plot(x['Generation'], x['NumCells'])
plt.title('Generation vs number of cells')
plt.show()

for i in ['S1(MeanNum)', 'S2(MeanNum)', 'S3(MeanNum)'] :
    plt.plot(x['Generation'], x[i])
plt.title('Generation vs mean number of S3')
plt.show()
