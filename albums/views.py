from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
from django_music import settings
from django.http import JsonResponse
import requests

# Create your views here.
def show_albums(request):
    albums = Album.objects.all()
    response = requests.get(f"https://itunes.apple.com/search?media=music&attribute=albumTerm&term=selling england by the pound&limit=200&page=2")
    response_json = response.json()
    return render(
        request, "albums/show_albums.html", {"albums": albums}
    )

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            response = requests.get(
                f"https://itunes.apple.com/search?media=music&attribute=albumTerm&term={album.title}&limit=200"
            )
            response_json = response.json()
            result_objects = response_json["results"]
            for result in result_objects:
                artist_lower = album.artist.lower()
                if artist_lower in result["artistName"].lower()or artist_lower in result["collectionName"].lower():
                    filtered_result = result["artworkUrl100"]
                    album.album_art_url = filtered_result
                    break
            album.save()
        return redirect(to='show_albums')
    else:
        form = AlbumForm()
        return render(request, "albums/add_album.html", {"form": form})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"album": album})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='show_albums')
    else:
        form = AlbumForm(instance=album)
        return render(request, "albums/edit_album.html", {
            "form": form, "album": album
        })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='show_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})

def toggle_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.is_favorite = not album.is_favorite
    album.save()
    return JsonResponse({"is_favorite": album.is_favorite})



# Add field to model
# Show for each album, is this a fav?
# Make "is this fav" clickable, just to log the click
# Can make fetch to console log JSON response
# Can add pk to click, so also logs PK
# Can update URL/view/template to send/receive/log PK, this ensures right one clicked and sent
# Can update view to actually toggle value (and send back updated value)
# Can change displayed fav/unfav depending on response from view

