import streamlit as st
import requests as req
import os
import google.generativeai as genai


st.title("Online-Game Analyzer")
st.write("Welcome to our Online-Game Analyzer. Enter the name of the game you're interested in along with its corresponding genre, and get a brief background of the game and its developers. If you're still curious, ask questions related to the game and developer company using the text box below the description!")

def generateWithAI():
    nameInputted = st.text_input("Game Title", "",placeholder="Enter Game Title Here")
    genreInputted = st.text_input("Genre", "", placeholder="Enter Corresponding Genre Here")
    random = st.button("Randomize")

    st.subheader("Game Description")

    gameId = ""
    api = req.get("https://www.freetogame.com/api/games").json()
    for gameDict in api:
        if gameDict["title"] == nameInputted and gameDict["genre"] == genreInputted:
            gameId = gameDict["id"]

    gameInfo = req.get(f"https://www.freetogame.com/api/game?id={gameId}").json()
    genre = gameInfo["genre"]
    title = gameInfo["title"]
    description = gameInfo["description"]
    releaseDate = gameInfo["release_date"]
    publisher = gameInfo["publisher"]
    developer = gameInfo["developer"]

    

    key = st.secrets["key"]
    genai.configure(api_key=key)

    model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
    response = model.generate_content(f'Give a brief intro paragraph explaining this game genre: {genre}. In the next paragraph give a brief description of the game {title}, starting with the release date ({releaseDate}) utlizing parts from this description: ({description}), and other info you find. In the next paragraph give a brief description about the publisher company: {publisher} and developer company: {developer}. In the final paragraph give a small list of beginner tips for beginners when playing {title}.') #enter your prompt here!
    st.write(response.text)

    
    
    st.subheader(f"Additional Questions About {title}")
    st.write(f"If you're still curious about {title}, ask your questions below!")

    def aiChatBot(role):
        if role == "model":
            return "assistant"
        else:
            return role
        
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history = [])
    
    for message in st.session_state.chat.history:
        with st.chat_message(aiChatBot(message.role)):
            st.markdown(message.parts[0].text)

    if prompt := st.chat_input("What would you like to know?"):
        st.chat_message("user").markdown(prompt)
        with st.spinner("Thinking tirelessly..."):

            response = st.session_state.chat.send_message(f"Using information related to the game {title}, and its developer and publisher companies ({developer} and {publisher}), pretend to be an expert on the game and answer questions the users asks in a brief paragraph. If the user's prompt is rude or offensive, politely ask them to ask questions related to the game analyzed. If you do not understand the user's query, simply give them a few basic info about the game and prompt them for further questions. Only provide information about the game in the 'Game Description' section above; if the user wants to know more about a different game, prompt them to input it into the Game Analyzer. User's prompt:" + prompt)

            with st.chat_message("assistant"):
                st.markdown(response.text)


    
        
try:
    generateWithAI()
except (KeyError, RuntimeError) as e:
    st.write("")