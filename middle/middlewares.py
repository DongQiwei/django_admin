'''
如何自定义中间件
1.10以前
1.10以后
'''

# 请求首先经过中间件
# 如果在process函数中有返回值,直接就将内容响应给客户端,就不走视图函数

# 1.11
from django.utils.deprecation import MiddlewareMixin


# class Middle01:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#     # 提供了三个方法
#     # 请求到达视图函数之前
#     def process_view(self, request, callback, *args, **kwargs):
#         print('process_view')
#
#     # 视图函数抛出异常且没有处理异常的时候执行的方法
#     def process_exception(self, request, response):
#         print('process_exception')
#
#     # 在视图函数中使用render方法
#     def process_template_response(self, request, response):
#         print('process_template_response')

class Middle02(MiddlewareMixin):
    def process_request(self, request):
        print('Middle02---process_request--->执行了')
    def process_view(self, request, callback, *args, **kwargs):
        print('Middle02---process_view--->执行了')
    def process_response(self, request, response):
        print('Middle02---process_response--->执行了')
        return response