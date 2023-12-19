import streamlit as st

import json

st.title("Mostafa Samir Yehia Saad - Group A - ID: 4211247")
st.title("example of Array ")

with open("data/array.json", "r") as file:
    data = json.load(file)

add_input_container, add_btn_container = st.columns([0.7, 0.3])

with add_input_container:
    add_input = st.number_input("Enter a number:", value=0, key="add")

with add_btn_container:
    add_btn = st.button("add")

if add_btn and add_input != "":
    data.append(add_input)

remove_input_container, remove_btn_container = st.columns([0.7, 0.3])

with remove_input_container:
    remove_input = st.number_input("Enter a number:", value=0, key="remove")

with remove_btn_container:
    remove_btn = st.button("remove")

if remove_btn and remove_input != "":
    if remove_input in data:
        data.remove(remove_input)
    else:
        st.warning(f"Element {remove_input} not array")

st.write(" <-> ".join(map(str, data)))

with open("data/array.json", "w") as file:
    json.dump(data, file)
