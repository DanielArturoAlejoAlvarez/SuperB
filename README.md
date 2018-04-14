# SuperB
## Description

This repository is a Application software with Python, Django and MYSQL, this application contains a simple Blog.

## Installation
Using Python2.7 and Django 1.11.12 preferably.

## Usage
```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/SuperB.git [NAME APP] 
```
Follow the following steps and you're good to go! Important:


![alt text](https://ugc.kn3.net/i/origin/https://i1.wp.com/blog.desdelinux.net/wp-content/uploads/2017/05/terminal-para-mysql.gif?resize=640%2C463&ssl=1)


## Coding

### Urls

```
...
url(r'^details/(?P<slug>[-\w]+)/$', views.details),     
url(r'^category/(?P<id>\w+)/$', views.category, name='category'),    
url(r'^tag/(?P<id>\w{0,50})/(?P<slug>[-\w]+)/$', views.tag, name='tag'),
...

```

### Views

```python
...
def tag(request,slug,id):     
    tags2 = Tag.objects.all()
    category = Category.objects.all()  
    tags = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags=id)
    
    context = {
        'tags': tags,
        'posts': posts,
        'tags2': tags2,
        'category': category, 
    }
    return render(request, 'tag.html', context)
...
```

### Model

```python
...
class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    state = models.BooleanField(default=True)
    picture = models.FileField(blank=True)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)
...
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/SuperB. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
