#entertainment_center_part2.py file feeds fresh_tomatoes.py
#with needed class and title info to
#create a web page.

#fresh_tomatoes is a py file that sets up the web site html template,
#and extracts movie content
#from entertainment_center.py file.
import fresh_tomatoes

#media is a class that entertainment_center_part2 re-uses for each
#movie trailer instance.
import media

#code that calls media.Movie class to create each movie trailer.
#used google url shortener to reduce trailer jpeg link size.
Gods_not_dead = media.Movie("Gods not dead",
                            "College student stands up for his faith",
                            "http://goo.gl/vM8hOn",
                            "https://www.youtube.com/watch?v=Mqf5gAYcFWs")

Bruce_Lee = media.Movie("Enter The Dragon",
                        "Bruce Lee's last completed movie",
                        "http://goo.gl/6T7mrh",
                        "https://www.youtube.com/watch?v=tB-QGOChuQc")

StarWars_vs_StarTrek = media.Movie("Star Wars vs Star Trek",
                                   "A well done trailer that got my geek going",
                                   "http://goo.gl/1jH4ZD",
                                   "http://www.youtube.com/watch?v=o5S5tBuNJdM",)

Grownups = media.Movie("Grownups",
                       "Adam Sandler makes another movie with his friends",
                       "http://goo.gl/ilwfVo",
                       "https://www.youtube.com/watch?v=e01NVCveGkg")

Facing_the_giants = media.Movie("Facing The Giants",
                                "A low budget movie with a good message",
                                "http://goo.gl/6o3RxT",
                                "http://www.youtube.com/watch?v=jtVJqyhk97U",)

Book_of_eli = media.Movie("Book Of Eli",
                          "2010 Denzel movie about perserving a copy of the Bible",
                          "http://goo.gl/Dg52vF",
                          "http://www.youtube.com/watch?v=kAMUv22y1og")

# movies list populates fresh_tomatoes()
movies = Grownups, Bruce_Lee, Book_of_eli, StarWars_vs_StarTrek, Gods_not_dead, Facing_the_giants

# fresh_tomatoes.open_movies_page(movies) launches fresh_tomatoes py file operation.
fresh_tomatoes.open_movies_page(movies)

# prints scrip info from media.py using __doc__ class
print (media.Movie.__doc__)
