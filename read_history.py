import pandas as pd
from pandas import DataFrame

#importar arquivo no formato CSV 
data = pd.read_csv (r'LOGS/history_a.csv')

# df.info() ver linhas e colunas do arquivo

# quero que mostre apenas essas colunas
df = pd.DataFrame(data, columns= ['effective_T', 'log_Teff', 'log_g', 'luminosity', 'radius'])
#df = pd.DataFrame(data, columns= ['effective_T', 'log_Teff', 'log_g', 'log_L', 'log_R'])

#imprimir colunas que eu desejar
print(df.loc[(df['log_Teff'] < 3.9444) & (df['log_Teff'] >= 3.9242) & (df['log_g'] > 3.5) & (df['log_g'] < 3.7), ['effective_T', 'log_Teff', 'log_g', 'luminosity', 'radius']].to_csv(r'LOGS/history_b.csv'))
#df.loc[(df['log_Teff'] < 3.9) & (df['log_Teff'] >= 3.8) & (df['log_g'] > 3.7) & (df['log_g'] < 3.8), ['log_Teff', 'log_g', 'log_L', 'log_R']].to_csv(r'teste2.txt')

#escrever novo arquivo
#export_csv = df.to_csv(r'teste.csv')

#df = pd.read_csv("history_out.csv")

