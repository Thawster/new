from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import PageForm
from django.http import HttpResponseRedirect
from wiki.models import Page

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class PageCreateView(CreateView):
    model = Page

    def get(self, request):
        form = PageForm()
        context = {'form': form,}
        return render(request, "new-wiki.html", context)

    def post(self, request):
        if request.method == "POST":
            form = PageForm(request.POST)
            if form.is_valid():
                wiki = form.save()

                txt_message = wiki.title+" has been successfully created"

                return render(request, 'page.html', {'page': wiki})
            else:

                errors = "Wiki was not created" 
                error_page('page-error', errors)
        else:
            form = PageForm()

        context = {'form': form}

        return render(request, 'wiki/page.html', context)