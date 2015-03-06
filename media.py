import webbrowser

#Movie is the class that entertainment_center_part2.py calls to create each movie poster.
class Movie():
    """ This py file is called to provide the movie.Media class """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

#definition to initialize each variable that will be plugged into the Movie class.    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
