import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header("Breakfast")
streamlit.text('🥣 Omega3 & Blueberry Oat meal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
