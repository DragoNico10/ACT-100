moviereviews=[]
class MovieReview:
    def _init_(self, movie, story, actors, music):
        self.movie_name=movie
        self.story_rating=story
        self.actor_rating=actors
        self.music_rating=music
        self.avg=int((story+actors+music) / 3)
        self.rating={
            "Movie name": {movie},
            "Story rating": {story},
            "Actor rating": {actors},
            "Music rating": {music},
            "Average rating": {self.avg}
        }
    def add_movie_ratings(self, movie_list:list):
        movie_list.append(self.rating)
    def avg_star_ratings(self, movie_list:list):
        for movie in movie_list:
            print('Thanks for your opinion, you rated the movie with:')
            for i in range(movie['Average rating']):
                print('*',end=' ',sep='')
            print()
rev=MovieReview('TestMovie', 5, 5, 5)
rev.add_movie_ratings(moviereviews)
rev.avg_star_ratings(moviereviews)