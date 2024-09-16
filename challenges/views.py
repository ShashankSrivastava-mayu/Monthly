from django.http import Http404, HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def January(request):
#     return HttpResponse("NO NEED TO EAT NONVEG")

# def February(request):
#     return HttpResponse("EAT ONLY VEG")

# def March(request):
#     return HttpResponse("EAT WHATEVER YOU WANT")
# modifying in more dynamic way 

# def month_challenge(request, month):
#     mera_challenge = None
#     if month == "January":
#         mera_challenge = "NO need to eat"
#     elif month == "February":
#         mera_challenge = "eat every needed things"
#     elif month == "March":
#         mera_challenge ="eat mutton"
#     else:
#         return HttpResponseNotFound("not in menu")
#     return HttpResponse(mera_challenge)

#in more dynamic way by dictionary

'''monthly_challenge = {
    "January":"Eat only salad",
    "February":"Eat only green vegies",
    "March":"Eat only seeds",
    "April":"Drink only water",
    "May":"Eat only vegan",
    "June":"Eat only mutton",
    "July":"Eat only chicken",
    "August":"Eat only non-veg",
    "September":"Eat only veg",
    "October":"Eat only eggs",
    "November":"Eat only gutka",
    "December":"Eat only fruits",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirected_month = months[month-1]
#We are using reverse function here because we don't want to change the url name everywhere 
# for example we are using here this code (return HttpResponseRedirect("/challenge/" + redirected_month))
# so if we change our urls name in project URLS.py then by using name(in app urls.py) and reverse function
# we have to change only in main project Urls.py not everywhere 
    redirected_URL = reverse("Month_ka_Challenge", args =[redirected_month])
#    return HttpResponseRedirect("/challenge/" + redirected_month) # we have to give the new path because now we are using by numeric values
#    now instead of using "/challenge/" + redirected_month we can below code
    return HttpResponseRedirect(redirected_URL)

def monthly_challenge_by_String(request, month):
    try:
        mera_challenging = monthly_challenge[month]
        returning_html = f"<h1>{mera_challenging}</h1>"# using some html here to design the code
        return HttpResponse(returning_html)
    except:  
        return HttpResponseNotFound("<h1>NOT in MENU</h1>")'''
    
#-------------------------------------------------------------------------------------------------

# in this portion we have created new list and of month and by clicking it jan,feb march and so on 
# it will show the description(values) of dictionary 


monthly_challenge = {
    "January":"Eat only salad",
    "February":"Eat only green vegies",
    "March":"Eat only seeds",
    "April":"Drink only water",
    "May":"Eat only vegan",
    "June":"Eat only mutton",
    "July":"Eat only chicken",
    "August":"Eat only non-veg",
    "September":"Eat only veg",
    "October":"Eat only eggs",
    "November":"Eat only gutka",
    "December":None,
}


# def index(request):
#     list_items = ""
#     months =  list(monthly_challenge.keys())
    
#     for month in months:# this will hold and iterate every keys of monthly_challenge dict and after completion create 12 links
#         monthly = reverse("Month_ka_Challenge",args=[month])
#      #   capital_month = month.capitalize()
#         list_items += f"<li><a href=\"{monthly}\">{month}</a></li>"
        
#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)
#    # instead of above code we can use this by creating another index.html and write
#    # that code by using the help of html for tag and forloops and please check below code for this.

def index(request):
    month_s= list(monthly_challenge.keys())
    return render(request, "challenges/index.html",{
        "month": month_s
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirected_month = months[month-1]

    redirected_URL = reverse("Month_ka_Challenge", args =[redirected_month])
    return HttpResponseRedirect(redirected_URL)

def monthly_challenge_by_String(request, month):
    try:
        mera_challenging = monthly_challenge[month]
        # returning_html = render_to_string("challenges/challenge.html")
        # returning_html = f"<h1>{mera_challenging}</h1>"# using some html here to design the code
        # return HttpResponse(returning_html)
        # We can also use adynamic way behalf of this both upper lines by using render function
        # render function only use in successfull response not in error response 
        # by using httpresponsenotfound not in httpresponse
        return render(request, "challenges/challenge.html", {
            "Text" : mera_challenging,
            "Month_text": month.capitalize()
            })
        # now if we want to get dict values instead of "Welcome in lala's Kingdom" 
        # we have to add one more parameter in return render of dict type which we will call in challenge.html file
    except: 
         
        #return HttpResponseNotFound("<h1>NOT in MENU</h1>")
    # now we will create 404.html page instead of above code for getting other message
    # by using render_to_string function just because we can use render function only in 
    # case of successfull response

        # returning_404 = render_to_string("404.html")
        # return HttpResponseNotFound(returning_404)
    
    # we can also use a class which we can import hera and use instead of above code  
    
    
            raise Http404()# it will dynamically give exact 404 error not found
 