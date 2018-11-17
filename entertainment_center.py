# to import file media
import media
# to import file fresh tomatoes
import fresh_tomatoes

# Movie Toy Story
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Toy_Story_2.jpg/220px-Toy_Story_2.jpg",
						"https://www.youtube.com/watch?v=v-PjgYDrg70")

# Movie Avatar
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=uZNHIU3uHT4")

# Movie Black Banther
black_banther = media.Movie("Black Panther",
					 "Black Panther is a 2018 American superhero film based on the Marvel Comics character of the same name",
					 "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
					 "https://www.youtube.com/watch?v=dxWvtMOGAhw")

movies = [toy_story, avatar, black_banther]
fresh_tomatoes.open_movies_page(movies)