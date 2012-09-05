# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django_facebook.connect import connect_user
from django_facebook.api import get_facebook_graph
from django.core.urlresolvers import reverse


def home(request):
    t = loader.get_template("home.html")
    url = 'https://www.facebook.com/dialog/oauth?client_id=' + settings.FACEBOOK_APP_ID + '&redirect_uri=' + settings.FACEBOOOK_REDIRECT_URI + '&scope=' + settings.FACEBOOK_DEFAULT_SCOPE + '&state=' + settings.FACEBOOK_STATE_VAR
    c = Context({'fbconnect_url': url})
    return HttpResponse(t.render(c))


def fblogin(request):
        # we store the place to redirct to in state

        graph = get_facebook_graph(request, redirect_uri=settings.FACEBOOOK_REDIRECT_URI)
        action, user = connect_user(request, facebook_graph=graph)
        user.save()
        graph = get_facebook_graph(access_token=user.get_profile().access_token)
        t = loader.get_template("profile.html")
        c = Context({'fbconnect_url': user.get_profile().image.url})
        return HttpResponse(t.render(c))
