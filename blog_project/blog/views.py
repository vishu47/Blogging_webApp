from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
# dummydata
#
# posts = [
#     {
#       'author':'Vishnu',
#       'topic':'About ME',
#       'posted_date':'4th june,2020',
#       'content':'Your project may not work properly until you apply the migrations for app'
#      },
#      {
#        'author':'Maurya',
#        'topic':'About us',
#        'posted_date':'7th may,2020',
#        'content':'Your project may not work properly until you apply the migrations for app'
#       },
#       {
#         'author':'Mahesh',
#         'topic':'Lucknow',
#         'posted_date':'10th june,2020',
#         'content':'Your project may not work properly until you apply the migrations for app'
#        },
# ]

# def home(request):
#     context = {'posts':Post.objects.all()}
#     return render(request,'blog/home.html',context)

class PostListView(ListView):
    # which model want to in ListView
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-posted_date']  #ordering is default
    paginate_by = 4  #go to home.html

# user return the post related that user
class UserPostListView(ListView):
    # which model want to in ListView
    model = Post
    template_name = 'blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-posted_date']  #ordering is default
    paginate_by = 4  #go to home.html

    # get all query post of that user
    def get_queryset(self):
        # username=self.kwargs,get('username') comes from url
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_date')


class PostDetailView(DetailView):
    # which model want to in ListView and Create post_detail.html for detail view
    # context to be called as object chabge in post_detail.html
    model = Post

# mixins always left to the styleview
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    # add the author before the submit the form
    def form_valid(self,form):
        # take th form ad instance and then add author set it equels to user
        form.instance.author = self.request.user
        # save the form
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    # add the author before the submit the form
    def form_valid(self,form):
        # take th form ad instance and then add author set it equels to user
        form.instance.author = self.request.user
        # save the form
        return super().form_valid(form)
        # till now enyone can update the post user mixins to aboid that (UserPassesTestMixin)
    def test_func(self):
        # get the exact post by method (self.get_object())
        post = self.get_object()
        # check for author logged in user == post of the author
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView( DeleteView):
        model = Post

        success_url = '/'

        def test_func(self):
            # get the exact post by method (self.get_object())
            post = self.get_object()
            # check for author logged in user == post of the author
            if self.request.user == post.author:
                return True
            return False

def about(request):
    return render(request,'blog/about.html')
