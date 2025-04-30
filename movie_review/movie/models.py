from django.db import models

# Create your models here.


class Actor(models.Model):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)
    
    def __str__(self):
        return self.name 
class ActorImage(models.Model):
    image = models.ImageField(upload_to='actors/')
    actor = models.ForeignKey(Actor, related_name='actor_image', on_delete=models.CASCADE) 


class Movie(models.Model):
    GENRE = [
        ('ACT', 'Action'),
        ('COM', 'Comedy'),
        ('DRM', 'Drama'),
        ('HOR', 'Horror'),
        ('SCI', 'Sci-Fi'),
        ('ROM', 'Romance'),
        ('DOC', 'Documentary')
    ]
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=3, choices=GENRE)
    description = models.TextField(null=True, blank=True)
    cast = models.ManyToManyField(Actor, related_name='movie_actor')

    def __str__(self):
        return self.title
    

class MovieImage(models.Model):
    img = models.ImageField(upload_to='movies/')
    default = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, related_name='movie_image', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.movie.title}"

