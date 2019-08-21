from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from apps.login_app.models import User
from apps.optima_app.admin import google_maps_api_key

def routes(request):
    if 'new_user_id' not in request.session:
        return redirect('/login')
    else:
        print(f"----- {request.session['new_user_id']} -----")
        user = User.objects.get(id=request.session['new_user_id'])
        context = {
            'user': user,
            'logged_in': request.session['logged_in'],
            'google_maps_api_key': google_maps_api_key
        }
        return render(request, "optima_app/routes.html", context)


