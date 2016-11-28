from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(requet) :
	htmlCode = '<html>Fly Panda</html>'
	return HttpResponse(htmlCode)

# def index(request) :
# 	t = loader.get_template('index.html')
# 	blogs = Blog.objects.all()
# 	context = ('blogs':blogs)
# 	html = t.render(context)
# 	return HttpResponse(html)
# 
# 
# def blogDetail(request,blogId) :
# 	t = loader.get_template('blog.html')
# 	blogs = Blog.objects.get(id=blogId)
# 	context = ('blogs':blogs)
# 	html = t.render(context)
# 	return HttpResponse(html)

