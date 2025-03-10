from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)


def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, 'errors/400.html', status=400)


def handler403(request, exception):
    """Error Handler 403 - Permission Denied """
    return render(request, 'errors/403.html', status=403)


def handler500(request):
    """Error Handler 500 - Permission Denied """
    return render(request, 'errors/500.html', status=500)
