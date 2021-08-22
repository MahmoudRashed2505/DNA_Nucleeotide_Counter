################################################
# Import Libraries
####################################################

from altair.vegalite.v4.api import sequence
import pandas as pd
import streamlit as st
import altair as alt

#################################
# Page Title
#################################


st.write("""

    # DNA Nucleeotide Count Web App

    This app counts Nucleeotide composition of query DNA !

""")

#################################
# Input Text Box
#################################

# Header Before Text Box
st.header("Enter DNA sequence")

# Placeholder for the text box
sequence_input = ">DNA Query\ngttgatggctttttcgtgggacactacaccgcactcacagaaaaggggtatcaataaaac\nttcctgggtaatttgaagcgctcaattggggcaataatcacttcacgtattcagtactcg\ncgttcacggcccggcgcccggctcatgaacaggaactctggtagggcgtttgtagcccgc\n"

# Creating the Text area
sequence = st.text_area("Sequence input",sequence_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skip the sequence name (first line)
sequence = "".join(sequence) # Concatenate the list of strings


# Separator
st.write("""
*******
""")

# Prints the input DNA sequence
st.header('Input (DNA Query)')
sequence


# Separator
st.write("""
*******
""")

# Prints the input DNA sequence
st.header('Output')

# 1. Print Dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleeotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),

    ])
    return d

X = DNA_nucleeotide_count(sequence)
X_label = list(X)
X_values = list(X.values())

X

# 2. Print Humanly Readable Text
st.subheader('2. Print text')
st.write('These are ' + str(X['A']) + ' Adenine (A)')
st.write('These are ' + str(X['T']) + ' Thymine (T)')
st.write('These are ' + str(X['G']) + ' Guanine (G)')
st.write('These are ' + str(X['C']) + ' Cytosine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X,orient='index')
df = df.rename({0: 'Count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'Nucleeotide'})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'Nucleeotide',
    y = 'Count'
)
p = p.properties(
    width=alt.Step(80) # Controls the Width of the Bar
)

st.write(p)