import pandas as pd
import streamlit as st
import pickle
import requests


# def fetch_poster(movie_id):
#     response = requests.get("".format(movie_id))
#     data = response.json()
#     print(data)
#     return "" + data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        # recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity =pickle.load(open('similarity.pkl','rb'))



st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
movies['title'].values)

st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    names = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        # st.image(posters[0])

    with col2:
        st.text(names[1])
        # st.image(posters[1])

    with col3:
        st.text(names[2])
        # st.image(posters[2])

    with col4:
        st.text(names[3])
        # st.image(posters[3])

    with col5:
        st.text(names[4])
        # st.image(posters[4])