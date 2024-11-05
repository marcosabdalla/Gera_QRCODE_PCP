import qrcode
import streamlit as st

# Text input area
txt = st.empty()
code = txt.text_input(label="Texto para o QR-Code")

bt = st.button('Gerar QR-Code')

if bt:
    meu_qrcode = qrcode.make(code)
    meu_qrcode.save("CodigoQR.png")
    txt.text_input("",value="")
