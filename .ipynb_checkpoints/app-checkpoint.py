import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Data/world_bank_cleaned.csv')
st.set_page_config(page_title="ADIS")
st.set_page_config(layout="wide")


st.sidebar.markdown(f"""<div 
style="font-size:18px;
text-align:left;
font-weight:bold;
color:white">
Asian </div>
<div 
style="font-size:14px;
text-align:bottom-left;
font-weight:semibold;
margin-bottom:0;
color:#B6B4AA">
Intelligence System</div>""", unsafe_allow_html=True)

st.sidebar.markdown("""
<hr style="
    margin-left: -1rem;
    margin-right: -1rem;
    border: :6px solid #333;
    height: 1px;
    background-color: #9C9A92;
">
""", unsafe_allow_html=True)


st.sidebar.markdown("<br>", unsafe_allow_html=True)

single_country = st.sidebar.selectbox(
   'COUNTRY FOCUS',
    df['country'].unique()
)

selected_countries= st.sidebar.multiselect(
    'COMPARE WITH',
    df['country'].unique(),
    default=['India']
    
)


selected_year = st.sidebar.slider(
    "YEAR RANGE - 2000-2023",
    int(df['year'].min()),
    int(df['year'].max()),
    (2000,2014)
    
)


filtered_df = df[(df['country'].isin(selected_countries))
    & (df['year'] >= selected_year[0]) &
    (df['year'] <=selected_year[1])]


heading1,heading2=st.columns(2)
with heading1:
   st.markdown(f"""
   <div style="display:flex">
   <div style="
    font-size:20px;
    font-weight:bold;">
    {single_country}—Overview</div>
    <div style="color:#75A1CC;
    font-weight:bold;
    font-size:20px;
    margin-left:25px;
    ">{selected_year[0]}-{selected_year[1]}</div>
    </div>
""", unsafe_allow_html=True)

with heading2:
    st.markdown("""<div 
style="font-size:18px;
text-align:right;
font-weight:semibold;
color:#B6B4AA">
Asian Development Intelligence System - World Bank Data</div>""", unsafe_allow_html=True)
    
    


st.markdown("""
<hr style="
    margin-left: -10rem;
    margin-right: -10rem;
    border: :6px solid #333;
    height: 1px;
    background-color: #9C9A92;
">
""", unsafe_allow_html=True)

st.markdown("""
<div style="
   color:#204C76;
   font-weight:bold;
   font-size:24px
">ASIAN DEVELOPMENT INTELLIGENCE SCORE
</div>
""", unsafe_allow_html=True)




def kpi_card(title,column,is_inverse=False):
    current_year = selected_year[1]
    previous_year = current_year -1

    current = filtered_df[filtered_df['year'] == current_year][column].mean()
    previous = filtered_df[filtered_df['year'] == previous_year][column].mean()
    delta = current - previous
    arrow = "▲" if delta > 0 else "▼"
    if is_inverse:
        color = "green" if delta < 0 else "red"
    else:
        color = "green" if delta > 0 else "red"
    
    st.markdown(f"""
    <div style="
       background: #FAEEDA;
        padding:25px;
        border-radius:15px;
        text-align:center;
         box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        border-left: 4px solid #633806;
    ">
        <h5 style=
        "color:#633806;
        font-weight:bold;
        text-align:center;" >
        {title}</h5>
        <div style="display:flex;
        justify-content:center";
        align-item:center
        >
         <p style="
        color:black;
        font-size:30px;
        text-align:center;;
        font-weight:bold" >
       {round(current, 2)}
        </p>
       <p style="color:{color};
       font-size:15px;
       margin-top:14px;
       margin-left:10px";
       >
            {arrow} {round(delta, 2)}
        </p></div>
       
    </div>
""", unsafe_allow_html=True)


col1,col2,col3 = st.columns(3)
st.markdown("<br>", unsafe_allow_html=True)

with col1:
    kpi_card(
    "GDP Per Capita",'gdp_per_capita')
    
    st.markdown("<br>", unsafe_allow_html=True)

with col2:
    kpi_card(
        "GDP Growth", 'gdp_growth')
    
    st.markdown("<br>", unsafe_allow_html=True)
with col3:
    kpi_card(
        "Life Expectency",
         'life_expectancy')
    
    st.markdown("<br>", unsafe_allow_html=True)

col4,col5,col6=st.columns(3)

with col4:
    kpi_card(
    "Unemployment",'unemployment')
st.markdown("<br>", unsafe_allow_html=True)
    


with col5:
    kpi_card(
        "Literacy Rate", 'education_index')
st.markdown("<br>", unsafe_allow_html=True)    
with col6:
    kpi_card(
        "Foreign ",
         'fdi_per_capita')
st.markdown("<br>", unsafe_allow_html=True)    

filtered_df
col7,col8=st.columns(2)

with col7:
    fig = px.line(
    filtered_df,
    x = 'year',
    y = 'gdp_per_capita',
    color="country"
     )
    st.plotly_chart(fig,use_container_width=True)

with col8:
    fig = px.histogram(
    filtered_df,
    x = 'year',
    y = 'gdp_growth',
    color="country"
     )
    st.plotly_chart(fig,use_container_width=True)
    
col9,col10=st.columns(2)

with col9:
    fig = px.pie(filtered_df, names="country", values="gdp_per_capita")
    st.plotly_chart(fig)
with col10:
    fig = px.scatter(
    filtered_df,
    x="gdp_per_capita",
    y="life_expectancy",
    size="population",
    color="country"
    )
    st.plotly_chart(fig)

fig = px.bar(filtered_df, x="country", y="gdp_per_capita", color="year")
st.plotly_chart(fig)
    








