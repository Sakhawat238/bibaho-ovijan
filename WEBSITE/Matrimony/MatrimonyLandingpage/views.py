from django.shortcuts import render
from django.contrib import messages
from CORE.Matrimony.MatrimonyConfig.services import landing_page_data
from CORE.Common.Auth.services import registerUser
from django.shortcuts import redirect
import json



def LandingPage(request):
    if request.method =='POST':
        response = registerUser(request)
        response = json.loads(response.content)
        print('response-----------------', response)

        if response['success']:
            messages.success(request, response['msg'])
            return redirect('LandingPage')
        else:
            messages.warning(request, response['msg'])
            return redirect('MatrimonyLandingPage')


    else:
        context = landing_page_data()
        print('context-------------------', context)
        return render(request, 'WEBSITE/Matrimony/LandingPage.html', context)


