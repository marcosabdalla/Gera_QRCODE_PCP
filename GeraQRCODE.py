import qrcode
import streamlit as st
import io

# Text input area
txt = st.empty()
code = txt.text_input(label="Texto para o QR-Code")
if code:
    meu_qrcode = qrcode.make(code)

    # Save the QR code image to an in-memory buffer
    img_buffer = io.BytesIO()
    meu_qrcode.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Create a download button for the QR code
    btn = st.download_button(
        label="Baixar QR-Code",
        data=img_buffer,
        file_name="qrcode.png",
        mime="image/png"
    )
    txt.text_input("",value="")
