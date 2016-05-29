from django.shortcuts import render_to_response, RequestContext


def welcome(request):
    return render_to_response('welcome.html', context_instance=RequestContext(request))
