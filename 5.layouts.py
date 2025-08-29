import streamlit as st

st.title('Layouts')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/layout')

# sidebar 📧  📱  ☎
with st.sidebar:
    st.header('1.Sidebar')
add_selectbox = st.sidebar.selectbox('어떻게 연락드릴까요?', ('Email','Mobile', 'Office phone'))

if add_selectbox == 'Email':
    st.sidebar.title('📧')
elif add_selectbox == 'Mobile':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎')


st.header('2.Columns')
col1, col2, col3 = st.columns(3)
with col1:
    st.text('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.text('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with col3:
    st.text('A owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')


st.header('3.Tabs')
tab1, tab2, tab3 = st.tabs(['고양이', '개', '부엉이'])
with tab1:
    st.caption('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tab2:
    st.caption('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with tab3:
    st.caption('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')