import json as JSON
from django.http import HttpResponse

def json( data ):
  return HttpResponse( JSON.dumps( data ) , content_type='application/json' )