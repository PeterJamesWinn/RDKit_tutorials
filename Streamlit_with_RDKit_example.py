import streamlit as st
st.write('Hello World')
x = st.slider('x')
st.write(x,'squared is', x*x)
st.write("and another thing")
st.write("and another")

from PIL import Image
import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
m = Chem.MolFromSmiles('Cc1ccccc1')
#im = Draw.MolToFile(m,'mol.png')
im = Draw.MolToImage(m)

st.image(im)