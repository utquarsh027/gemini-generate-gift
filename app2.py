import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm

API_KEY="AIzaSyAo9yfpvJACfzgxPyX3cj3FkSoV4wUy3nY"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Generate Gift", 
                   page_icon="🎁",
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Generate Gift")

occasion=st.text_input(label="occasion",label_visibility="collapsed",placeholder="What's the occasion?")
relation=st.text_input(label="realtion",label_visibility="collapsed",placeholder="Your relation with the receiver")
interests=st.text_input(label="Interest",label_visibility="collapsed",placeholder="Enter some of the receiver's interests")
food_they_love=st.text_input(label="Food",label_visibility="collapsed",placeholder="There favorite food")
items_they_love=st.text_input(label="Items",label_visibility="collapsed",placeholder="Somethings they uses a lot")
age=st.slider(label="Age",min_value=1,max_value=100)
budget=st.text_input(label="budget",label_visibility="collapsed",placeholder="Enter your budget")

generate=st.button("Generate Gift")

if generate:
    try:
        model=genai.GenerativeModel("gemini-pro")
        prompt = f"I'm having a hard time finding a {occasion} gift for my {relation}\n\n"
        prompt += f"Their main interests are {interests} and they love to eat {food_they_love}\n\n"
        prompt += f"Items they use a lot are {items_they_love}\n\n"
        prompt += f"They are {age} years old and my budget for them is {budget} rupees\n\n"
        prompt += f"Could you suggest some good {occasion} gift ideas that I could buy them?"
        prompt += f"Try to be as thoughtful and delightful as possible and always suggest a specific product if available with price and don't suggest something over {budget}."

        response = model.generate_content(
                glm.Content(
                    parts = [
                        glm.Part(text=prompt),
                    ],
                ))
        st.write(response.text)
    except:
        st.write("Check Prompt")    


ft = """
<style>
a:link, a:visited {
  color: #BFBFBF;
  background-color: transparent;
  text-decoration: none;
}

a:hover, a:active {
  color: #0283C3;
  background-color: transparent;
  text-decoration: underline;
}

body {
  margin: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.content {
  flex: 1;
}

.footer {
  background-color: transparent;
  color: #808080;
  text-align: center;
  padding: 20px 0;
}
</style>

<div class="content">
  <!-- Your content here -->
</div>

<div class="footer">
  <p style='font-size: 0.875em;'>
    Made with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height="10"/>
    <a href="https://github.com/utquarsh027" target="_blank">by Utkarsh</a>
  </p>
</div>
"""

st.write(ft, unsafe_allow_html=True)
