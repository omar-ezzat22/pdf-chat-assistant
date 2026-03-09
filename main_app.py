import streamlit as st
import pdf_helper as helper

st.set_page_config(page_title="PDF ChatBot", layout="wide")
st.title(" مساعدك الذكي لملفات PDF")

with st.sidebar:
    st.header("إعدادات الملف")
    uploaded_file = st.file_uploader("ارفع ملف PDF هنا", type="pdf")
    process_button = st.button("تحليل المستند")

if uploaded_file and process_button:
    with st.spinner("جاري قراءة الملف وتقطيعه وبناء قاعدة البيانات..."):
        with open("temp_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.session_state.vector_db = helper.create_vector_db_from_pdf("temp_file.pdf")
        st.success("تم تجهيز الملف للدردشة!")

query = st.text_input("اسأل أي سؤال عن محتوى الملف:")

if query:
    if "vector_db" not in st.session_state:
        st.error("عفواً، يجب رفع ملف وتحليله أولاً قبل السؤال.")
    else:
        with st.spinner("جاري استخراج الإجابة..."):
            response = helper.get_response_from_pdf(st.session_state.vector_db, query)
            st.markdown("الإجابة:")
            st.info(response)