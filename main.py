import streamlit as st

st.set_page_config(
    layout="centered", page_title="生日快乐", page_icon="🎆"
)

c1, c2 = st.columns([0.3, 2])
# The snowflake logo will be displayed in the first column, on the left.
with c1:
    st.title(":fireworks:")
# The heading will be on the right.
with c2:
    st.title("丽霞，生日快乐")
st.caption('点击播放按钮播放音乐')
st.audio('./audio/birthday.m4a', loop=True, autoplay=True, end_time=218)
st.image('./img/fireworks_1.gif')

st.markdown(
    '''> **这是我第一次用这种方式祝贺生日快乐** :grin: \n > 祝你生日快乐:birthday:，又大了一岁:kissing_smiling_eyes::kissing_smiling_eyes:''')
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    st.image('./img/cake_1.gif')


st.markdown('### **我知道**：')
# st.markdown(
#     '* 我不是太会说话，说话太直接，哪里让你不高兴，别往心里去，如果觉得我哪里不好，都可以和我说，我一定会改的:innocent: 我希望可以成为你生活中的一部分')
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    st.write('我不是太会说话，说话太直接，')
    st.write('哪里让你不高兴，别往心里去，')
    st.write('如果觉得我哪里不好，都可以和我说，我一定会改的:innocent: ')
    st.write('我希望可以成为你生活中的一部分:man_and_woman_holding_hands:')

st.markdown('### **我觉得**：')
# st.markdown('* 你很温柔，很让我心动，有你晚安的夜让我睡得安稳:sleeping:')
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    st.write('你很温柔，很让我心动，')
    st.write('有你晚安的夜让我睡得安稳:sleeping:')

st.markdown('### **我最想做**: ')
# Three columns with different widths
col1, col2, col3 = st.columns([2, 3, 2])
# Using 'with' notation:
with col2:
    st.write(':sunny:想和你无忧无虑在一起，')
    st.write('想去哪里去哪里，')
    st.write('想做什么做什么，')
    st.write('去逛街、去购物......')

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.markdown('# 希望可以和你走很久:gem:')
    st.image('./img/HandonHand.gif')
