class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year_of_creation):
        self.title = title
        self.artist = artist
        self.year_of_creation = year_of_creation


input_title = str(input())
input_artist = str(input())
input_year_of_creation = int(input())


painting = Painting("", "", 0)
painting.title = input_title
painting.artist = input_artist
painting.year_of_creation = input_year_of_creation

print('"' + str(painting.title) + '" by ' + str(painting.artist) + ' (' + str(painting.year_of_creation) + ') hangs in the Louvre.')

