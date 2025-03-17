# Part 1
Goal is to create a blog style website, with an authentication system.

## Creating a new project
See Mosh tutorial notes

# Part 2 Application and Routes

## Create new app
See Mosh tutorial ntoes

Inside your `view.py` import http response. 

```python
from django.http import HttpResponse
```

Create a view function that returns home page. 

```python
# blog/views.py
def home(request):
    return HttpResponse('<h1> Blog Home </h1>')
```

Map a url to your view function
* Create `url.py` file inside `blog` app. Add the following lines of code inside. 

```python
from django.urls import path
from .views import home

urlpatterns = [
    # Empty path - Home page
    path('',views.home, name='blog-home'),
]
```

Inside the project `url.py` file, import include method as well, which is from django.url

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]

```
When the user navigates to some URL, the code will look through the `urlpatterns` list inside `django_project/urls.py`. Checks if there is a pattern that matches that. Then it asks, where next should I send people if they are at this URL. For example if you land on `blog/`, it will look within the `url.py` file of that particular app. For example

```python
"""
Whenever Django sees this include function, it will chop off
whatever URL it has seen up to that point, and send the 
remaining string into the urls module for futher processing. 

In this case, the user goes to blog url, but when you chop that off
there is nothing reminaing so it's just an empty string. 
"""
include('blog.urls'),
```

Which in our case an empty string for the blog's urlpatterns returns the `home` function in our `blog/views.py` file.

```python
urlpatterns = [
    # Empty path - Home page
    path('', views.home, name='blog-home'),
]
```

Summarised: User nagivates to URL, sent to project URLpatterns, sent to app url patterns, sent to the correct view function to handle the request.

# Part 3 Templates

## Creating templates
For each app, Django will look for a templates subdirectory by default. 

Create another subfolder within `blog/templates` named after the app name `blog`. Corey (paraphrase mine): "This sounds redundant, but it's just part of the Django convention."

blog -> templates -> blog -> templates.html

Corey says to add the `BlogConfig` within `blog/apps.py` inside you `INSTALLED_APPS` list inside the `settings.py` file of your project folder. As such

```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig', # <- added new app
]
```

Now, in your view function file `views.py`, change the return of your view function to render the template html file instead of the HttpResponse.

Remarks: The first argument of render is always request. Second is the filepath to the template html file.

![](img/render_function.png)

Adding dummy data into our views function, i.e. fake posts.

1. To do so create some dummy blog posts called posts.
2. Use the context parameter, enter in a dictionary defined within your view function.
3. Change your template file, i.e. `home.html`. Write a for loop to show posts.
Remark: Use `{% %}` for for-loops, `{{}}` for variables in a HTML file.

![](img/templates_for_loops_vars.png)

4. We can also use 'if/else' statements.

```html
{% if title%}
    <title></title>
{% else %}
    <title></title>
{% endif%}
```

## Templates inheritance
Reduce repeated code for html.

We can create a base template, and replace the custom html sections with blocks. Then the child template can override the the parent base template. 

```html
{% block content %} {% end block%}
```
Then in your child templates, remove everything that isn't unique to the template. 

![](img/home_about_template_compare.png)

*New `home.html`*

```html
{% raw %}
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
    {% comment %} print post info, one at a time {% endcomment %}
        <h1>{{  post.title  }}</h1>
        <p> By {{ post.author }} on {{post.date_posted}}</p>
        <p> {{post.content}} </p>
    {% endfor %}
{% endblock content %}
{% endraw %}
```

*New `about.html`* 

```html
{% raw %}
    {% extends "blog/base.html" %}
    {% block content %}
        <h1>About Page</h1>
    {% endblock content %}
{% endraw %}
```

Summary: Template inheritance makes it easier to apply changes across multiple pages in the site. For example, if you wanna use "bootstrap"...Look into it.

## Bootstrap

![Bootstrap starter template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

^From the bootstrap boilerplate above, we extract the code with the comments "Bootstrap CSS"  and "Optional Javascript".

```html
<!DOCTYPE html>
<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        {% if title%}
        <title>Django Blog - {{ title }} </title>
        {% else %}
            <title>Django Blog</title>
        {% endif%}
    </head>
    <body>
        <div class="container">
            {% block content %} {% endblock %}
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    </body>
</html>
```

Adding the container class gives some padding to the blog post.

Stopped at importing code snippets 33:03 