from django.db import models
from django.contrib import auth
# Create your models here.

class Publisher(models.Model):
    """Publishers of books."""
    name = models.CharField(max_length=50, help_text="Name of the publisher")
    website = models.URLField(help_text="Website of the publisher")
    email = models.EmailField(help_text="Address email of the publisher")

    def __str__(self):
        """Return name of the publisher."""
        return self.name

class Book(models.Model):
    """Published book."""
    title = models.CharField(max_length=70, help_text="Book title")
    publication_date = models.DateField(verbose_name="Publication date")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField("Contributor", through="BookContributor")

    def __str__(self):
        """Return title of the book."""
        return self.title

class Contributor(models.Model):
    """Contrbutors."""
    first_names = models.CharField(max_length=50, help_text="Name/s of contributors")
    last_names = models.CharField(max_length=50, help_text="Surname/s of contributors")
    email = models.EmailField(help_text="Email.")

    def initialled_name( obj):
        """ obj.first_names='Jerome David', obj.last_names='Salinger'
            => 'Salinger, JD' """
        initials = ''.join([name[0] for name in obj.first_names.split(' ')])
        return "{}, {}".format(obj.last_names, initials)

    def __str__(self):
        """Return first names of contributors."""
        return self.initialled_name
    

class BookContributor(models.Model):
    """Bookd contributors"""

    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Role which contributors fulffiled",\
                            choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    """Reviews."""
    content = models.TextField(help_text="Text review")
    rating = models.IntegerField(help_text="Users' rating")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date and time of creating review")
    date_edited = models.DateTimeField(null=True, help_text="Date and time of the last edition")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,help_text="Reviewed book")