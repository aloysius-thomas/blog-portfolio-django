from django.db import models


class SiteData(models.Model):
    intro_background = models.ImageField(upload_to='intro_background/')
    get_in_touch_message = models.TextField()
    work_completed = models.IntegerField(default=0)
    total_clients = models.IntegerField(default=0)


class Portfolio(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='portfolio')
    category = models.CharField(max_length=64)
    date = models.DateField()

    def __str__(self):
        return f"Portfolio {self.title}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=128)
    client_image = models.ImageField(upload_to='client')
    message = models.TextField()
