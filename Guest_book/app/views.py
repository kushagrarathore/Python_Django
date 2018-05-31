from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm
# Create your views here.
def index(request):
	comment = Comment.objects.all().order_by('id')
	context = {'comment':comment}

	return render(request, 'index.html',context)

def signin(request):
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
			new_comment.save()
			return redirect('index')
			

	else:
		form = CommentForm()
	context = {'form':form}
	return render(request, 'signin.html', context)

def login(request):
	return render(request,'login.html')