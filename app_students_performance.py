import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

st.markdown('# Student Performence')

df = pd.read_csv('https://raw.githubusercontent.com/camimq/student_app/main/StudentsPerformance.csv', sep=';')

# trazendo a tabela para a aplicação
st.dataframe(df)

st.markdown('## Valores nulos por coluna')
n = df.isna().sum()
# transforma o arrary numa tabela
st.table(n)

st.markdown('## Descrição Estatística')
describe = df.describe().T
st.table(describe)

st.markdown('## Contabilizando performance dos alunos')
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['avg score'] = df['total score'] / 3

math_gabaritou = df[df['math score'] == 100]['avg score'].count()
reading_gabaritou = df[df['reading score'] == 100]['avg score'].count()
writing_gabaritou = df[df['writing score'] == 100]['avg score'].count()

st.markdown(f'O número de alunos que gabaritaram em matemática foi de : {math_gabaritou}')
st.markdown(f'O número de alunos que gabaritaram em escrita foi de : {writing_gabaritou}')
st.markdown(f'O número de alunos que gabaritaram st.markdownleitura foi de : {reading_gabaritou}')

st.markdown('## Transformando os números de performance em porcentagem')
total = len(df)
p_math = (math_gabaritou / total)*100
p_writing = (writing_gabaritou / total)*100
p_reading = (reading_gabaritou / total)*100

st.markdown(f'A porcentagem de alunos que gabaritaram em matemática foi de: {p_math:.2f}%')
st.markdown(f'A porcentagem de alunos que gabaritaram em leitura foi de: {p_reading:.2f}%')
st.markdown(f'A porcentagem de alunos que gabaritaram em escrita foi de: {p_writing:.2f}%')

st.markdown('### Histograma')
fig, ax = plt.subplots(1,2, figsize=(15,7))
plt.subplot(121)
sns.histplot(data=df, x='avg score', bins = 30, kde = True, color = 'g')
plt.subplot(122)
sns.histplot(data=df, x='avg score', kde=True, hue='gender')
plt.show()

st.pyplot(fig)

st.markdown('### Pairplot')
g = sns.pairplot(df, hue='gender')
st.pyplot(g)

st.markdown('### Outros gráficos')
f,ax=plt.subplots(1,2, figsize=(20,10))
sns.countplot(x=df['race/ethnicity'], data=df, palette='bright', ax=ax[0], saturation=0.95)
for container in ax[0].containers:
  ax[0].bar_label(container, color='black', size=20)

plt.pie(x=df['race/ethnicity'].value_counts(), labels=df['race/ethnicity'].value_counts().index,  # type: ignore
        explode=[0.1,0,0,0,0], autopct='%1.1f%%', shadow=True)
plt.title('Race / Ethnicity Distribution', fontsize=20)

plt.show()
st.pyplot(f)

#st.markdown('### Mapa de Calor')

#h = sns.heatmap(df[['math score', 'writing score', 'reading score', 'avg score', 'total score']].corr(), annot=True, fmt='.2f')

#st.pyplot(h)
