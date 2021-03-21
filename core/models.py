from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save




class HomePage(models.Model):
    
    title = models.CharField(max_length=60)
    subtitle = models.TextField()
    icon = models.FileField()
    page_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    
    def __str__(self):
        return f'{self.name} - {self.phone}'


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    gradient = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=60, blank=True)
    # meta_description = RichTextUploadingField(blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    service = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='portfolio')
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    name_gradient = models.CharField(max_length=100, blank=True)
    brand_name = models.CharField(max_length=80)
    date = models.CharField(blank=True, max_length=20)
    category_portfolio = models.CharField(max_length=80)
    challenge = RichTextUploadingField(blank=True)
    # solution = RichTextUploadingField(blank=True)
    main_image = models.FileField(upload_to='portfolio_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)

    def __str__(self):
        return self.name


class PortfolioVideoUploads(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images_portfolio')
    images = models.FileField(upload_to='portfolio_images/')

    def __str__(self):
        return self.portfolio.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    image = models.FileField(blank=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    roadmap_content = RichTextUploadingField(blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, related_name='service')
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='service_item', null=True)
    name = models.CharField(max_length=80, help_text='Ex. Planning')
    image = models.FileField(blank=True)
    text = RichTextUploadingField(blank=True)
    gradient = models.CharField(max_length=150,blank=True)




class Teachers(models.Model):
    name_surname = models.CharField(max_length=120)
    sphere = models.CharField(max_length=120)
    image = models.FileField()
    gradient = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_surname

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'


class AboutUs(models.Model):
    content = RichTextUploadingField(blank=True)
    content_own = RichTextUploadingField(blank=True)
    content_two = RichTextUploadingField(blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    def __str__(self):
        return 'Abouts Us'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True)

    def __str__(self):
        return self.user.username


def create_profile_post_save(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user)


post_save.connect(create_profile_post_save, sender=User)


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    gradient = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)


    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    gradient = models.CharField(max_length=120)
    tag = models.ManyToManyField(Tag, related_name='blog_posts')
    content = RichTextUploadingField()
    short_content = RichTextUploadingField(blank=True)
    main_image = models.FileField()
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)


    def __str__(self):
        return self.title


class Partners(models.Model):
    image = models.FileField()

    def __str__(self):
        return f'{self.id}'


class Vacancies(models.Model):

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=50,help_text='Yereven RA')
    location_icon = models.FileField(upload_to='job_icons/')
    job_type = models.CharField(max_length=50,help_text='Remote OK')
    job_type_icon = models.FileField(upload_to='job_icons/')
    job_time = models.CharField(max_length=50,help_text='Full time')
    job_time_icon = models.FileField(upload_to='job_icons/')
    vacancy_description = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    google_map = models.TextField(blank=True)
    is_custom_list_style = models.BooleanField(blank=True,default=False)
    graddient = models.CharField(max_length=50,blank=True)
    head_title = models.CharField(max_length=120,blank=True)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    
    
    def __str__(self):
        return self.name

class VacancyTeamImages(models.Model):

    vacancy = models.ForeignKey(Vacancies,on_delete=models.CASCADE,related_name='images')
    image = models.FileField(upload_to='job_images/')

    def __str__(self):
        return self.vacancy.name


class VacancySubscribe(models.Model):

    vacancy = models.ForeignKey(Vacancies,on_delete=models.CASCADE,null=True,blank=True,related_name='subscribe')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    linkedin = models.URLField(blank=True)
    file_cv = models.FileField(blank=True,null=True)
    cover_letter = models.TextField(blank=True)
    about_text = models.TextField(blank=True)
    why_want = models.TextField(blank=True)
    work_style = models.TextField(blank=True)
    five_years = models.TextField(blank=True)
    salary_range = models.CharField(max_length=20,blank=True)
    portfolio_link = models.TextField(blank=True)
    question_for_us = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'


class ProgrammingLanguages(models.Model):
    
    icon = models.FileField()
    alt_icon = models.CharField(blank=True,max_length=40)
    
    def __str__(self):
        return str(self.pk)
        
class FooterData(models.Model):
    
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    
    
class FooterIcon(models.Model):
    footer = models.ForeignKey(FooterData,on_delete=models.SET_NULL,null=True,blank=True,related_name="footericon")
    icon = models.FileField()
    url = models.URLField(blank=True,null=True)
    
    
class TextContext(models.Model):
    
    head_title = models.CharField(max_length=150)
    head_content = models.TextField(blank=True)
    head_image = models.FileField(blank=True)
    
    def __str__(self):
        return self.head_title