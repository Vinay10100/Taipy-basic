import taipy as tp
from taipy.gui import Gui
import pandas as pd

# sample
movies = pd.DataFrame({
    'Title': ['Inception', 'The Dark Knight', 'Pulp Fiction', 'The Godfather', 'The Matrix', 
              'Fight Club', 'Forrest Gump', 'The Shawshank Redemption', 'The Avengers', 'Avatar'],
    'Genre': ['Action', 'Action', 'Crime', 'Crime', 'Action', 
              'Drama', 'Drama', 'Drama', 'Action', 'Sci-Fi'],
    'Rating': [8.8, 9.0, 8.9, 9.2, 8.7, 8.8, 8.8, 9.3, 8.0, 7.8]
})

# Initial empty data
filtered_movies = pd.DataFrame()
selected_genre = ""
genres = ['Action', 'Drama', 'Crime', 'Sci-Fi']

# Define the layout of the dashboard
layout = """
# Movie Recommendation Dashboard

## Select Genre:
<|{selected_genre}|selector|lov={genres}|dropdown|>

<|Get Recommendations|button|on_action=get_recommendations|>

### Movie Recommendations for <|selected_genre|text|>

<|{filtered_movies}|table|width=500px|>

<|{filtered_movies}|chart|type=bar|x=Title|y=Rating|color=Title|title="Average Rating of Movies"|>
"""

# Function to filter movies by genre
def get_recommendations(state):
    if state.selected_genre:
        state.filtered_movies = movies[movies['Genre'] == state.selected_genre]
    else:
        state.filtered_movies = pd.DataFrame()  # Clear the table if no genre is selected

# Create the GUI object
gui = Gui(page=layout)

if __name__ == "__main__":
    gui.run()
