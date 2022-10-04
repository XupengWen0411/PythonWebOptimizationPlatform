# from django.shortcuts import render
#
# # Create your views here.
# # from jinja2 import Environment, FileSystemLoader
# # from pyecharts.globals import CurrentConfig
# # from django.http import HttpResponse
# #
# # CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates/pycharms_TM"))
# #
# # from pyecharts import options as opts
# # from pyecharts.charts import Bar
# #
# #
# # def index(request):
# #     c = (
# #         Bar()
# #         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# #         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# #         .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
# #         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
# #     )
# #     return HttpResponse(c.render_embed())
#
#
# '''
# 前后台分离View
# '''
# import json
# from random import randrange
# from django.http import HttpResponse
# from rest_framework.views import APIView
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
#
# # Create your views here.
# def response_as_json(data):
#     json_str = json.dumps(data)
#     response = HttpResponse(
#         json_str,
#         content_type="application/json",
#     )
#     response["Access-Control-Allow-Origin"] = "*"
#     return response
#
#
# def json_response(data, code=200):
#     data = {
#         "code": code,
#         "msg": "success",
#         "data": data,
#     }
#     return response_as_json(data)
#
#
# def json_error(error_string="error", code=500, **kwargs):
#     data = {
#         "code": code,
#         "msg": error_string,
#         "data": {}
#     }
#     data.update(kwargs)
#     return response_as_json(data)
#
#
# JsonResponse = json_response
# JsonError = json_error
#
#
# def index() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
#         .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
#         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
#         .dump_options_with_quotes()
#     )
#     return c
#
#
# class ChartView(APIView):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(json.loads(index()))
#
#
# class IndexView(APIView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse(content=open("./templates/One_APP_TM/index.html").read())
import json
from random import randrange
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base():
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
        .dump_options_with_quotes()
    )
    return c



class Chart_View(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))


# class Index_View(APIView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse(content=open("templates/One_APP_TM/index.html").read())

def Index_View(request):
    return HttpResponse(content=open("templates/One_APP_TM/index.html").read())
