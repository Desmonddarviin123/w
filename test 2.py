Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requets
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import requets
ModuleNotFoundError: No module named 'requets'
>>> import requests
>>> url requests.get('https://bolajiolajide.github.io')
SyntaxError: invalid syntax
>>> url = requests.get('https://bolajiolajide.github.io')
>>> source = BeautifulSoup(url.text, 'html.parser')
>>> post_feed = spurce.find('div', class_="post-feed")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    post_feed = spurce.find('div', class_="post-feed")
NameError: name 'spurce' is not defined
>>> post_feed = source.find('div', class_="post-feed")
>>> posts = post_feed.find_all('article', class_="post-card")
>>> single_post = posts [0]
>>> title = single_post.find('h2', class_='post-card-title')
>>> title.text
'Recursion For Beginners'
>>> excerpt = single_post.find('section', class_="post-card-excerpt")
>>> excerpt.p.text
'What is recursion? Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem (as opposed to iteration). The approach can be applied to'
>>> author = single_post.find('span', class_="post-card-author")
>>> author.a.text
'Bolaji Olajide'
>>> def get_post_details(article)
SyntaxError: invalid syntax
>>> get_post_details(article):
	
SyntaxError: invalid syntax
>>> def get_post_details(article):
	title = article.find('h2', class_='post-card-title').text
	excerpt = article.find('section', class_='post-csrd-excerpt').p.
	
SyntaxError: invalid syntax
>>> def get_post_details(article):
	title = article.find('h2', class_='post-card-title').text
	excerpt = article.find('section', class_='post-csrd-excerpt').p.text
	author = article.find('span', class_='post-card-author').a.text
	return

>>> def get_post_details(article):
	title = article.find('h2', class_='post-card-title').text
	excerpt = article.find('section', class_='post-csrd-excerpt').p.text
	author = article.find('span', class_='post-card-author').a.text
	return {
		"title": title,
		"excerpt": excerpt,
		"author": author
		}

>>> blog_posts = [get_post-details(post) for post in posts];
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    blog_posts = [get_post-details(post) for post in posts];
  File "<pyshell#31>", line 1, in <listcomp>
    blog_posts = [get_post-details(post) for post in posts];
NameError: name 'get_post' is not defined
>>> blog_posts = [get_post_details(post) for post in posts];
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    blog_posts = [get_post_details(post) for post in posts];
  File "<pyshell#32>", line 1, in <listcomp>
    blog_posts = [get_post_details(post) for post in posts];
  File "<pyshell#30>", line 3, in get_post_details
    excerpt = article.find('section', class_='post-csrd-excerpt').p.text
AttributeError: 'NoneType' object has no attribute 'p'
>>> def get_post_details(article):
	title = article.find('h2', class_='post-card-title').text
	excerpt = article.find('section', class_='post-card-excerpt').p.text
	author = article.find('span', class_='post-card-author').a.text
	return {
		"title": title,
		"excerpt": excerpt,
		"author": author
		}

>>> blog_posts = [get_post_details(post) for post in posts ];
>>> blog_posts
[{'title': 'Recursion For Beginners', 'excerpt': 'What is recursion? Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem (as opposed to iteration). The approach can be applied to', 'author': 'Bolaji Olajide'}, {'title': 'Creating a Simple Python Decorator', 'excerpt': 'One of the amazing things about the Python language is the use of decorators to alter functionality. Decorators are used to extend functions without actually modifying them directly.', 'author': 'Bolaji Olajide'}, {'title': 'The Art of Learning\u200a—\u200aMy Learning Process', 'excerpt': 'Learning is the process of acquiring new or modifying existing knowledge, behaviors, skills, values, or preferences.', 'author': 'Bolaji Olajide'}]
>>> blog_posts = []
>>> for post in posts:
	blog_posts.append(get_post_details(post))

	
>>> blog_posts
[{'title': 'Recursion For Beginners', 'excerpt': 'What is recursion? Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem (as opposed to iteration). The approach can be applied to', 'author': 'Bolaji Olajide'}, {'title': 'Creating a Simple Python Decorator', 'excerpt': 'One of the amazing things about the Python language is the use of decorators to alter functionality. Decorators are used to extend functions without actually modifying them directly.', 'author': 'Bolaji Olajide'}, {'title': 'The Art of Learning\u200a—\u200aMy Learning Process', 'excerpt': 'Learning is the process of acquiring new or modifying existing knowledge, behaviors, skills, values, or preferences.', 'author': 'Bolaji Olajide'}]
>>> 
