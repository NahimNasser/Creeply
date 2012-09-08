# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from django.conf import settings
from django_facebook.connect import connect_user
from django_facebook.api import get_facebook_graph
from linkedin import linkedin
from models import LinkedInProfile


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
        LinkedInProfile.objects.get_or_create(user=user)
        graph = get_facebook_graph(access_token=user.get_profile().access_token)
        graph_data = graph.get('/me')
        t = loader.get_template("profile.html")
        liApi = linkedin.LinkedIn('d4sg4uq23heb', 'CECqmTcwYr9GZod5', 'http://creeply.dev:8000/linkedin/login')
        result = liApi.request_token()
        if result:
            graph_data['liUrl'] = liApi.get_authorize_url()
            user.liProfile.request_token = liApi._request_token
            user.liProfile.request_token_secret = liApi._request_token_secret
            user.liProfile.save()
        graph_data['img'] = 'https://graph.facebook.com/%s/picture?type=large' % user.get_profile().facebook_id
        c = Context(graph_data)
        return HttpResponse(t.render(c))


def lilogin(request):
        liApi = linkedin.LinkedIn('d4sg4uq23heb', 'CECqmTcwYr9GZod5', 'http://creeply.dev:8000/linkedin/login')
        import ipdb; ipdb.set_trace()
        liApi.access_token(request_token=request.user.liProfile.request_token.encode('utf8'), request_token_secret=request.user.liProfile.request_token_secret.encode('utf8'), verifier=request.GET['oauth_verifier'])
        liProfile = liApi.get_profile()
        return HttpResponse()
