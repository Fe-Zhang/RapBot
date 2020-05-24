import lyricsgenius
import json
import os

artists = []
with open('artist_names.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line != '' and line != ' ':
            artists.append(line)


f_missed = open('missed.txt', 'w+')
max_songs = 5 #50
genius = lyricsgenius.Genius("oRpUdk-bSIRE7Yy5LuA-aerqpFPWjt5AH3oRnqdar-PraN7heBqL74Qze3ibvOSd")

# sys.stdout = open('log.txt', "w")
artist_objs = []
for name in artists[881:]:
    print('Searching ', name)
    artist = genius.search_artist(name, max_songs=max_songs, get_full_info = False)

    if artist == None:
        f_missed.write(name)
    else:
        if not os.path.isdir('./lyrics/'+artist._body['name'].replace(os.path.sep, '_')): 
            os.mkdir('./lyrics/'+artist._body['name'].replace(os.path.sep, '_'))

        for song in artist._songs:
            with open(os.path.join('lyrics',artist._body['name'].replace(os.path.sep, '_'),song._body['full_title'].replace(os.path.sep, '_')), 'w') as f:
                f.write(song._body['lyrics'])

        artist_objs.append(artist)

# sys.stdout = sys.__stdout__

# one_artist = artist_objs[0]
# for artist in artist_objs:
#     for song in artist._songs:
#         print(artist._body['name'])
#         if not os.path.isdir('./lyrics/'+artist._body['name']): os.mkdir('./lyrics/'+artist._body['name'])

#         with open('lyrics/'+artist._body['name']+'/'+song._body['full_title'], 'w+') as f:
#             f.write(song._body['lyrics'])
#         break