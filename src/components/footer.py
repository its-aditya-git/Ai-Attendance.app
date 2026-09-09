import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/0pGwM1pG/logg.png"

    st.markdown(
        f"""
        <div style="margin-top:3rem; display:flex; gap:0.6rem; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;">Created with ❤️ by</p>
        <img src="{logo_url}" style="max-height:25px" />
        </div>

    """, unsafe_allow_html=True )



def footer_dashboard():
    logo_url = "https://i.ibb.co/9m0n4nBv/logg.png"

    st.markdown(
        f"""
        <div style="margin-top:2.4rem; display:flex; gap:0.6rem; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;">Created with ❤️ by</p>
        <img src='{logo_url}' style='max-height:25px' />
        </div>
        
                """, unsafe_allow_html=True )
        