import streamlit as st
from fewshot import FewShotPosts

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish" , "Hindi"]

def main():
    st.title('Linkedin Post generator')
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1 :
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
       selected_length =  st.selectbox("Length", options=length_options)
    
    with col3:
       selected_language = st.selectbox("Language", options=language_options)
        
    if st.button('Generate Post'):
        st.write(f"Genrated Posts for {selected_tag} ,{selected_length} ,{selected_language}")

if __name__ == "__main__":
    main()