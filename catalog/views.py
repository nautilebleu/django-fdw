from django.shortcuts import render

from catalog.models import Album

def home(request):
    extra = {
        'select': {'artist_name':'"index_artist"."name"'},
        'tables': ['index_artist'],
        'where': ["index_artist.id=catalog_album.artist_id"]
    }
    albums = Album.objects.extra(**extra).all()

    return render(request, 'home.html', {
        'albums': albums
    })
