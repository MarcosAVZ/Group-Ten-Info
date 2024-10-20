from django.shortcuts import redirect

class BloqueoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.bloqueado:
            return redirect('pagina_bloqueada')  # Redirige a una página que indiques

        response = self.get_response(request)
        return response