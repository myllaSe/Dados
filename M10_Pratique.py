import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())
print(df.tail().to_string())

# Dicionário para padronização dos valores do df['Gênero']
print(df['Gênero'].value_counts())
generos = {
    'Feminino' : 'Feminino',
    'Mulher' : 'Feminino',
    'short menina verao look mulher' : 'Feminino',
    'roupa para gordinha pluss P ao 52' : 'Feminino',
    'bermuda feminina brilho Blogueira' : 'Feminino',
    'Masculino' : 'Masculino',
    'Sem gênero' : 'Sem gênero',
    'Unissex' : 'Sem gênero',
    'Bebês' : 'Bebês',
    'Meninas' : 'Meninas',
    'Meninos' : 'Meninos',
    'menino' : 'Meninos'
}
df['Gênero'] = df['Gênero'].replace(generos)

# Histograma
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

plt.figure(figsize=(18, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Gênero')
plt.xlabel('Gênero')
plt.ylabel('Frequência')
plt.show()

# Gráfico de Dispersão
plt.scatter(df['Nota_MinMax'], df['N_Avaliações_MinMax'])
plt.title('Dispersão - Nota x Número de Avaliações')
plt.xlabel('Nota')
plt.ylabel('N_Avaliações')
plt.show()

# Mapa de Calor
corr = df[['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax']].corr()
sns.heatmap(corr, annot = True, cmap = 'coolwarm')
plt.title('Correlação Preço e Marca')
plt.show()

#Normalizar os dados do df['Material']
df['Material_limpo'] = (df['Material'].str.lower().str.strip())
df['Material_limpo'] = df['Material_limpo'].str.normalize('NFKD') \
    .str.encode('ascii', errors='ignore') \
    .str.decode('utf-8')

# Categoriza os dados do df['Material']
def categorizar_material(texto):
    if pd.isna(texto):
        return 'Outros'
    texto = texto.lower()
    if 'algod' in texto:
        return 'Algodão'
    elif 'poliest' in texto or 'pet' in texto:
        return 'Poliéster'
    elif 'jean' in texto:
        return 'Jeans'
    elif 'microfibra' in texto:
        return 'Microfibra'
    elif 'elastan' in texto:
        return 'Elastano'
    elif 'viscos' in texto:
        return 'Viscose'
    elif 'linho' in texto:
        return 'Linho'
    else:
        return 'Outros'
df['Material_categoria'] = df['Material_limpo'].apply(categorizar_material)
contagem = df['Material_categoria'].value_counts()

# Gráfico de barras
plt.figure(figsize=(8, 5))
contagem.plot(kind='bar', color='#4C72B0')
plt.title('Distribuição de Materiais')
plt.xlabel('Material')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

# Gráfico de Pizza
df['Nota_agrupada'] = df['Nota'].apply(
lambda x:
'5.0' if x == 5 else
'4.9 a 4.5' if x >= 4.5 else
'4.4 a 4.0' if x >= 4.0 else
'Outros')
contagem = df['Nota_agrupada'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Avaliações')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Qtd_Vendidos_Cod'], fill=True, color='#863e9c')
plt.title('Densidade de Quantidade de Vendas')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Preço_MinMax', y='Marca_Cod', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Preço por Marca')
plt.show()


