from django.http import HttpResponse
from api.utils import response
# from var_dump import var_dump


def index(request):
  # var_dump(request)
  return response.json({'haha':'oke deh'})