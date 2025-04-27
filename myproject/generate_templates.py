import os

# Define your app name and paths
app_name = 'myapp'
base_dir = os.path.join('templates', app_name)
partials_dir = os.path.join(base_dir, 'partials')

# Files to create
pages = [
    'base.html',
    'home.html',
    'about.html',
    'projects.html',
    'pricing.html',
    'team.html',
    'faq.html',
    'services.html',
    'services_detail.html',
    'blog.html',
    'blog_detail.html',
    'contact.html',
]
partials = ['header.html', 'footer.html']

# Boilerplate content
base_content = """{% load static %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% include 'myapp/partials/header.html' %}
    {% block content %}{% endblock %}
    {% include 'myapp/partials/footer.html' %}
</body>
</html>
"""

page_template = """{% extends 'myapp/base.html' %}
{% load static %}
{% block title %}{{ title }}{% endblock %}
{% block content %}
<h1>{{ title }}</h1>
<p>This is the {{ title|lower }} page.</p>
{% endblock %}
"""

header_content = """<header>
    <nav>
        <ul>
            <li><a href="{% url 'home' %}">Home</a></li>
            <li><a href="{% url 'about' %}">About</a></li>
            <li><a href="{% url 'services' %}">Services</a></li>
            <li><a href="{% url 'blog' %}">Blog</a></li>
            <li><a href="{% url 'contact' %}">Contact</a></li>
        </ul>
    </nav>
</header>
"""

# Create directories
os.makedirs(base_dir, exist_ok=True)
os.makedirs(partials_dir, exist_ok=True)

# Create base.html
with open(os.path.join(base_dir, 'base.html'), 'w') as f:
    f.write(base_content)

# Create page templates
for page in pages:
    if page != 'base.html':
        file_path = os.path.join(base_dir, page)
        with open(file_path, 'w') as f:
            title = page.replace('.html', '').replace('_', ' ').title()
            f.write(page_template.replace('{{ title }}', title))

# Create partials
for partial in partials:
    with open(os.path.join(partials_dir, partial), 'w') as f:
        f.write(header_content)

print("✅ Templates generated successfully!")
