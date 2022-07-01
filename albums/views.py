from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def show_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/show_albums.html", {"albums": albums})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='show_albums')
    else:
        form = AlbumForm()
        return render(request, "albums/add_album.html", {"form": form})
    # return render(request, "albums/show_albums.html", {
    #     "form": form, "albums": albums
    # })