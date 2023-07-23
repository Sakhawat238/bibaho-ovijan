from django.shortcuts import redirect
from AUTH.UserAuthentication.models import USER_TYPE


def seller_required():
    def _method_wrapper(function):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_anonymous:
                return redirect("LandingPage")
            if request.user.type != USER_TYPE.SELLER:
                return redirect("LandingPage")
            return function(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


def seller_self_required():
    def _method_wrapper(function):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_anonymous:
                return redirect("LandingPage")
            slug = kwargs['slug']
            if request.user.slug != slug:
                return redirect("LandingPage")
            return function(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


def visitor_required():
    def _method_wrapper(function):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_anonymous:
                return redirect("LandingPage")
            if request.user.type != USER_TYPE.VISITOR:
                return redirect("LandingPage")
            return function(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper