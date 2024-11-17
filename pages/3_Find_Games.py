import streamlit as st
import os
import requests as req

#User enters genre, output game options


def findGames():
    st.title("Want To Play A New Free Game? Find One Today!")
   # image_filename = os.path.join("FreeGamesImages/"+name.lower() + ".jpg")
    #st.image(image_filename, use_column_width=True)
    st.header("Select Video Game Genre")
    pref = st.radio("How would you like to find a game?", ["One Genre", "Multiple Genres"])
    if pref=="Multiple Genres":
        options = st.multiselect("What are your favorite colors",["Mmorpg", "Shooter", "Strategy", "Moba", "Racing", "Sports", "Social", "Sandbox", "Open-world", "Survival", "Pvp", "Pve", "Pixel", "Voxel", "Zombie", "Turn-based", "First-person", "Third-Person", "Top-down", "Tank", "Space", "Sailing", "Side-scroller", "Superhero", "Permadeath", "Card", "Battle-royale", "Mmo", "Mmofps", "Mmotps", "3d", "2d", "Anime", "Fantasy", "Sci-fi", "Fighting", "Action-rpg", "Action", "Military", "Martial-arts", "Flight", "Low-spec", "Tower-defense", "Horror", "Mmorts"],)    
        optionStr = ""
        for i in options:
            optionStr += f".{i.lower()}"
        api = req.get(f"https://www.freetogame.com/api/filter?tag={optionStr[1:]}=pc").json()    
        gameList = []
        for i in api:
            gameList.append(i["title"])

        choice = st.selectbox("Which Game Do you like best",gameList,  index=None, placeholder="Select game of choice...", )
        for i in api:
            if i["title"]==choice:
                st.image(i["thumbnail"])
                st.write(f"Your game of choice is {i[ 'title']} ")
                st.write(f"Game Description: {i['short_description']}") 
    if pref=="One Genre":
        option = st.selectbox('What Genre Are You Looking For?',("Mmorpg", "Shooter", "Strategy", "Moba", "Racing", "Sports", "Social", "Sandbox", "Open-world", "Survival", "Pvp", "Pve", "Pixel", "Voxel", "Zombie", "Turn-based", "First-person", "Third-Person", "Top-down", "Tank", "Space", "Sailing", "Side-scroller", "Superhero", "Permadeath", "Card", "Battle-royale", "Mmo", "Mmofps", "Mmotps", "3d", "2d", "Anime", "Fantasy", "Sci-fi", "Fighting", "Action-rpg", "Action", "Military", "Martial-arts", "Flight", "Low-spec", "Tower-defense", "Horror", "Mmorts"),index=None,placeholder="Select videogame category...",)
        api = req.get(f"https://www.freetogame.com/api/games?category={option}").json()
        gameList = []
        for i in api:
            gameList.append(i["title"])

        choice = st.selectbox("Which Game Do you like best",gameList,  index=None, placeholder="Select game of choice...", )
        if choice != "":
            st.write(f"You chose {choice}!")
        else:
            st.write(f"") 
        for i in api:
            if i["title"]==choice:
                st.image(i["thumbnail"])
                st.write(f"Your game of choice is {i[ 'title']} ")
                st.write(f"Game Description: {i['short_description']}")
try:
    findGames()
except (TypeError, ValueError, IndexError) as e:
    st.write("")
    