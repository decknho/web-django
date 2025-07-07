from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if host == "dereckeder.com.br":
            return HttpResponsePermanentRedirect("https://www.dereckeder.com.br" + request.get_full_path())

        return self.get_response(request)