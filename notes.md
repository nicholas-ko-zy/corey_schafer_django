# Part 1
Goal is to create a blog style website, with an authentication system.

## Creating a new project
See Mosh tutorial notes

# Part 2 Application and Routes

## Create new app
See Mosh tutorial notes

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

[Bootstrap starter template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

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

Key point here is about template inheritance, to make scalable code and to add some CSS to make template look nicer, not just base html.

Part 3: Templates; Timestamp 33:07

Copy code from Corey's repo, in a file called `navigation.html`. We are trying to add in some navigation features to the website. 

Right as he was explaining how to add CSS to our website, he begins to talk about creating a new directory to store CSS. Usually the folder is called `static`. 

* Create a new folder in the `blog` directory and create a new folder `static`.
* Create another folder inside your `static` folder, name it after the app.
  * ie. Your folder structure: blog -> static -> blog 
* Create a new file called `main.css` inside the lowest subfolder. Copy and paste the code from the snippets folder, there's a file with the same name `main.css`.
* Insert a code block at the top of your `base.html` file to load your custom css file.

![](img/load_static.png)

This is what you see when you refresh the server.

![](img/django_blog_with_some_css.png)

Part 3 Timestamp 39:51, replace the article html with code snippet file of the same name. The new article html has more CSS classes to make the article looks nicer.

![](img/article_html.png)

![](img/article_with_css.png)

We want to abstract the href arguments in our `base.html` file so that we don't hard code
the links in the navigation bar.

Previously:
```html
<a class="nav-item nav-link" href="/">Home</a>
```

Now (making use of a code block): 
```html
<a class="nav-item nav-link" href="{% url 'blog-home'%}">Home</a>
```

We use the url tag and the name of the route, which we chose to be 'blog-home'.

Recap on purpose of templates: Update your site in a single location (template inheritance), use URLS for link references, avoid hardcoding.

## Part 4 Admin Page

* Create new super user to login in as admin to your site.
* Create database (database migration, apply changes to database, for us, will create an auth_user table)
* Run `python manage.py makemigrations`
* Run `python manage.py migrate`
* Open terminal and enter the following command:
* `python manage.py createsuperuser`

## Part 5 Database and Migrations

* Sqlite for development
* Postgres for production

Add the stuff you need in `models.py`
```python
#models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    #  Create title attribute, a character field with a max length
    title = models.CharField(max_length=100)
    # Create content attribute as a textfield
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete removes all the posts if the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```
In your terminal

* Run `python manage.py makemigrations`
* Run `python manage.py sqlmigrate blog <migration_number>`
* Replace the migration_number with 0001.

This is the terminal output you'll see. 

![](img/sql_migrate_initial.png)

Turns class into SQL commands. Saves time for us to write the SQL ourselves. Object relational mappers makes it possible to write SQL code using on Python objects.

* Run migrate command: `python manage.py migrate`. You should get an OK status.
  
Creating a new post

* Run `python manage.py shell` to go into the Python terminal that can interact with Django objects
* Run `from blog.models import Post`
* Run `from django.contrib.auth.models import User`
* Assign user var to some user, i.e. `user = User.objects.filter(username='nkzy1517').first()`
* `user = User.objects.get(id=1)`
* Create a post instance: `post_1 = Post(title='Blog 1', content='First Post Content!', author=user)`
* Save post: `post_1.save()`
* Check that your post is saved: `Post.objects.all()`
* Creating a post through 
  * Either create another post instance, specifying the author OR
  * Run `user.post_set.create(title='Blog 3', content='Third Post Content!')` and you can leave out the author and the `.save()` method.

Instead of building out posts based on hardcoded dummy data, now we try to get the information from a SQL query to a database. 

![](img/dummy_data.png)

*Hardcoded dummy data in `views.py`*

```python
# views.py
# Old code
def home(request):
    context = {
        'posts': posts
    }
    return render(request, template_name='blog/home.html', context=context)
```

```python
# views.py
# New code
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)
```
The new code chunk uses the object relational mappers, which turn OOP Python code into SQL queries to the database. Using the `objects.all()` method gives all the posts.

Next we want to have an option to add posts via the admin page, i.e. http://127.0.0.1:8000/admin/. To do that you have to go to your `blog` folder's `admin.py` file

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

This is reflected in your admin GUI.

![](img/admin_gui_post1.png)

![](img/admin_gui_post2.png)

# Part 6 - User Registration
Goal: Create a front-end form, the kinds you typically see when you sign up for an account with a new platform.

First, we create an app called `users`. This will handle all our user features, like creating users. To create an app, recall that we run the terminal command:

```
python manage.py startapp users
```

Then we will get a new folder. Now we need to add our newly created `users` app to out settings.py file's `INSTALLED_APPS` list. Question: How do we know what name to add to the list? Well, we can think of the app you want to add as something like an import statement. You begin with the folder, followed by the subfolders, adding a period `.` as you go down the folder levels. Finally you end with the class name of your app. The class name is found in the `apps.py` file.

```python
# users/apps.py
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
```

So now we have 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig', # <- Newly added app file
]
```

Now we write the functions to create forms. Django comes with built-in classes for creating forms.

```python
from django.contrib.auth.forms import UserCreationForm
```

We create a template for this in HTML. Recall that to create a template for an app, we need to create this 'redundant' folder structure:

app_name > templates > app_name > template_name.html

Now instead of creating a `urls` module for our `users` app just as we did for blog, we are going to directly import the views function from the `users` app into the overall project's `urls.py` file.

See the difference between blog and users?

```python
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
]
```

Now we have a basic registration page when we navigate to that URL. 

![](/img/user_register_page.png)

Now we can make it look a little nicer using the form template. Simple change is to do `{{ form.as_p }}` instead of `{{ form }}`.

Key takeaway: User form gives us this user form all out of the box.

Now we want to handle the POST request that we get after the completed form. To do that, we would like to 

1. Handle the underlying POST
2. Redirect the user to home page and print a message communicating the status of the sign-up, i.e. If it was successful or not.


For (1), we can add a conditional to handle the POST request in the  `users/views.py` file. For (2), we will report a success message and add a highlighted bar at the top of the home-page, right above the posts.

(1)'s code change:

```python
# Create your views here.
def register(request):
    # Add in conditional to handle a POST request, to validate the form data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Form passes validation check, get the username and return a message.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # After a successful sign-up, use redirect function to
            # send the user back to the homepage.
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

(2)'s code change, focus being on the if messages block.

```html
-snip-

<div class="row">
    <div class="col-md-8">
    {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{ message.tags}}"> 
            {{ message }}
        </div>
        {% endfor %}  
    {% endif %}
    {% block content %}{% endblock %}
    </div>
    <div class="col-md-4">
    <div class="content-section">
        <h3>Our Sidebar</h3>

-snip-
```

![](/img/account_creation_message.png)

Finally, to update your database after a successful signup, just add `form.save()` to your views function.

![](/img/new_user_added.png)

## Adding a new field to the user creation form
Notice that we are missing the email address field for our alicebob. Now we need to create a new field to add to our register template.

To resolve this, we create a custom registration form using Django's default form template. Essentially, this we make a child class from Django's `UserCreationForm` class. After that we need to replace the default form we used in the views function to our custom form class, which we call `UserRegisterForm`, which now includes an email field.

```python
# django_project/users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create a form that inherits from UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # The model that is affected is the User model
        model = User
        # These are fields we want in the form, in this order
        fields = ['username', 'email', 'password1', 'password2']
```
Voila

![](img/registration_form_w_email_field.png)

So let's try again, to add a new user, this time with an email address...

![](img/new_user_w_email.png)

## Add bootstrap style to registration page to match our homepage style

Plus we want to add a highlight message to tell the user that they entered something wrong in one of the fields.

Let's try to do all our styling in our templates. C.S introduces a third-party Django framework called CrispyForms.

So we install it with `pip install django-crispy-forms`.

Add it to your settings file's `INSTALLED_APPS`:

```python
-snip-
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms', # <- added crispy forms
]
-snip-

.
.
.
# Specify which CSS framework you wanna use, in our case, bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

Then go back to your `register.html` template and load the Crispy Form in a code block and add a filter (denoted by `|`) on the `forms` variable.

```html
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">

-snip-
.
.
.
            <fieldset class="form-group">
                <legend class="border-bottom mb-4"> Join Today </legend>
                {{ form|crispy }}
            </fieldset>
-snip-
```

![](img/registration_form_bootstrap5.png)

We can see that the both the spacing of the fields and the error messages look so much better.

# Part 7 Admin and User Authentication

First, we have to import Django's standard out-of-the-box views for user authentication.

```python
# django_project/django_project/urls.py
from django.contrib.auth import views as auth_views
```

Remember that you always want to import `views` as something else, since there will be all kinds of views, you'll mess them up if you don't rename them.  i.e. importing from users, rename as `user_views`, importing from auth, rename `auth_views`.

After that, we add the login/logout paths to our url patterns list in the same file. We also need a template for the user login page. First we specify where our template path is. There's a default path for the template, but we can specify it in the as_views method's `template_name=` parameter.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'), # <- Newly added login path
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'), # <- Newly added logout path
]
```

![](/img/login_failed.png)

Now suppose we have a successful login, then we need a redirect otherwise we will get an error. To avoid the error, we need to add this to the settings file.

```python
# django_project/settings.py
.
.
.
-snip-

LOGIN_REDIRECT_URL = 'blog-home'
```

Now, we add a message that after someone creates new account, we redirect them back to the login page so they can test out their login credentials instead of sending them back to the home page.


*Before*
```python
# users/views.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') #<- Old message
            return redirect('blog-home') # <-Old redirect
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

*After*
```python
# users/views.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!') # <- New message
            return redirect('login') # <- New redirect
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

Now we add a logout view. Ok, so CS's method of just typing `/logout/` in the url doesn't work. This because going to a URL invokes a GET request, but Django's logout requires a POST request instead.

Now we want to change navigation link to change what people depending on their they're logged in or not. If they are, then no need to see login, vice versa.

```html
{%raw%}

<!-- Navbar Right Side -->
<div class="navbar-nav">
{% if user.is_authenticated %}
    <form method="post" action="{% url 'logout' %}" style="display: inline;">
    {% csrf_token %}
    <button type="submit" class="nav-item nav-link" style="background: none; border: none; padding: 0; cursor: pointer; color: #cbd5db; text-decoration: none;">
        Logout
    </button>
    </form>
{% else %}
    <a class="nav-item nav-link" href= {% url 'login' %}>Login</a>
    <a class="nav-item nav-link" href= {% url 'register' %}>Register</a>
{% endif %}
</div>
{%endraw%}
```


![](img/logout_link_after_user_auth.png)

Now we create a route to the user's profile. First, we create a users's profile method.

```python
# users/views.py
def profile(request):
    return render(request, 'users/profile.html')
```

Second, create a profile template, that goes into our users/templates/users folder.

```html
{% raw %}
<!-- users/templates/users/profile -->
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <h1> {{ user.username }} </h1>
{% endblock content %}

{% endraw %}
```

Next, add in the urlpattern for profile

```python
# django_project/django_project/urls.py
-snip-
path('profile', user_views.profile, user_views.profile, name='profile'),
-snip-
```

Now we also want to add a condition for the user to be logged in in order to see the profile. It doesn't make sense to be able to navigate to the profile page if you are logged out.

To do this we can do a simple check on the user authentication state. In the `users/views.py` file, first import

```python
from django.contrib.auth.decorators import login_required
```

Then add this line of code to the profile function and redirect user to the login page if they wanna see the profile page.

In settings, specify your login url. 
```python
# django_project/django_project/settings.py
-snip-
LOGIN_URL = 'login'
```
Viola you're done. You'll notice that in the URL, it keeps track of the page you were trying to access and once your login is successful, it will direct you to the page you wanted to go.

![](/img/login_to_see_profile.png)

# Part 8: User Profile and Picture

Create a new model in our users app. 

We need to install `pillow` with `pip install Pillow` so that our database migration works with images. 

Then after that we makemigrations -> migrate

1. `python manage.py makemigrations`
2. `python manage.py migrate`


We also want to register our profile module in `users/admin.py`.

```python
# users/admin.py`
admin.site.register(Profile)
```

Now we'll try to add in a profile picture for one of our users. 

Let's also reorganise where the profile pictures are saved to. Currently, they are saved to `django_project/profile_pics` which in the future might be very cluttered if there are many pictures.

First, add this line in the settings file.

```python
# django_project/django_project/settings.py
-snip-
# Set media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

After this, Corey does two things which I won't go deep into: 
1. Copy/paste code snippets for the profile HTML.
2. Follow Django documentation for serving user-uploaded files

```python
# django_project/django_project/urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

![](/img/profile_page_w_pic.png)

We want to make sure that every new user created, they automatically get a profile, which includes the default profile picture. Now we have to go to the admin page to create the profiles for our users. To resolve this, we'll a Django signal. 

1. Create a `signals.py` file in your users app.
```python
# Fire this signal after a post is saved.
from django.db.models.signals import post_save
# User is the sender, user sends a signal
from django.contrib.auth.models import User
# Create a receiver, receives signal
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

```

* When a post is saved, the it will trigger a signal. Sender is user, and receiver is this `create_profile` function, which...as you guessed it, creates a profile.
* Save profile after it's created.

2. Import signals inside users app.

```python
# users/apps.py
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
```

So now each time we create a new user, we also create a new profile automatically with the default picture loaded.

i.e. 

![](/img/TU1_create.png)

![](/img/TU1_profile_created.png)


# Part 9: Update User Profile

We need to create a form that will update our user model. To do so, we just need to add more forms to update the user and profile. 

```python
# django_project/users/forms.py
-snip-
class UserUpdateForm(forms.ModelForm):
    # A user update form to update the username and email
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # A profile update form to update our profile picture
    class Meta: 
        model = Profile
        field = ['image']
```

After that, we need to update our view function so that we also see the UserUpdateForm, ProfileUpdateForm, on top of the existing UserRegisterForm.

```python
# django_project/users/views.py
-snip-
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # Add requirement for user to be logged in to see profile
    return render(request, 'users/profile.html', context=context)
```

Recap on what is context in a Django view function and how it is used in templates:

Taken from: https://clouddevs.com/django/use-context-in-templates/

> "
    How is it Used in Templates? Once the context dictionary is populated in a view, it’s passed to the template as a parameter when rendering the template. This makes the data within the context accessible within the template, allowing you to dynamically generate HTML content based on that data.
"
So the changes we made to our view function now will dynamically update the profile based on the context, which is based on the user and profile update forms.

Next we want to copy the form from the `register.html` template and paste it into the `profile.html` template. 

```
<!-- Form snippet from register.html, the register template -->
{% raw %}
<form method="POST">
    {% comment %} Add csrf token {% endcomment %}
    {% csrf_token %}
    <fieldset class="form-group">
        <legend class="border-bottom mb-4"> Join Today </legend>
        {{ form|crispy }}
    </fieldset>
    <div class="form-group">
        <button class="btn btn-outline-info" type="submit">Sign Up</button>
    </div>
</form>
{% endraw %}
```

We need to change the code snipper a bit so that we see both the user and profile update forms as a single form. We need to edit it out as such:

```
<!-- profile.html -->
{% raw %}
-snip-
<form method="POST" enctype="multipart/form-data">
    {% comment %} Add csrf token {% endcomment %}
    {% csrf_token %}
    <fieldset class="form-group">
        <legend class="border-bottom mb-4"> Profile Info </legend>
        {{ u_form|crispy }}
        {{ p_form|crispy }}
    </fieldset>
    <div class="form-group">
        <button class="btn btn-outline-info" type="submit"> Update </button>
    </div>
</form>
-snip-
{% endraw %}
```

We changed the variable name for the form and stacked them on top of each other. `u_form` and `p_form`.

![](/img/profile_form_v1.png)

It would make sense for the username, email address and image to be filled in with the current ones. 

```python
# django_project/users/views.py
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # POST GET REDIRECT
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # Add requirement for user to be logged in to see profile
    return render(request, 'users/profile.html', context=context)
```

![](/img/profile_form_v2.png)

Then if we try to update the profile form

![](/img/update_profile_form.png)

![](/img/updated_profile_page.png)

Now we try to resize image so that the large image doesn't eat up memory. 

Stopped at Part 9 17:10