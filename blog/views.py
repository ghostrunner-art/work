from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator #导入分页器
from .models import Blog,BlogType
from django.conf import settings

#blogs列表页面views
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator =Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url的页码参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    # 取当前页前后各2个的页码
    page_range = list(range(max(current_page_num-2,1),current_page_num)) + list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))
    # 加上省略页码标记
    if page_range[0] -1 >=2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >=2:
        page_range.append('...')
    # 判断显示第一的页码和最后的页码
    if page_range[0] !=1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    #context['blogs'] = Blog.objects.all()  #获取全部文章列表
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = Blog.objects.dates('created_time','month',order='DESC')
    return render_to_response('blog/blog_list.html',context)
#blog内容页views
def bolg_detail(request,blog_pk):
    context = {}
    blog = get_object_or_404(Blog,id = blog_pk)
    context['previous_blog'] = Blog.objects.filter(created_time__gt = blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt = blog.created_time).first()
    context['blog'] = blog
    return render_to_response('blog/blog_detail.html',context)
#blogs分类views
def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 利用分页器每10页进行分页
    page_num = request.GET.get('page', 1)  # 获取url的页码参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    # 取当前页前后各2个的页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 判断显示第一的页码和最后的页码
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    # context['blogs'] = Blog.objects.all()  #获取全部文章列表
    context['blog_type'] = blog_type
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html',context)

def blogs_with_date(request,year,month):
    pass


