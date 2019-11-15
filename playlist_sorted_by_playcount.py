import sys
import os

from simplejson import JSONDecodeError

# print(os.environ['SPOTIPY_CLIENT_ID'])
# print(os.environ['SPOTIPY_CLIENT_SECRET'])
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:1337/callback/'
import spotipy
import spotipy.util as util

import pickle

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-library-read'
try:
    token = util.prompt_for_user_token(username, scope, os.environ['SPOTIPY_CLIENT_ID'],
                                       os.environ['SPOTIPY_CLIENT_SECRET'], os.environ['SPOTIPY_REDIRECT_URI'])
except (AttributeError, JSONDecodeError):
    os.remove(".cache-{}".format(username))
    token = util.prompt_for_user_token(username, scope, os.environ['SPOTIPY_CLIENT_ID'],
                                       os.environ['SPOTIPY_CLIENT_SECRET'], os.environ['SPOTIPY_REDIRECT_URI'])


def show_tracks_iter(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(track['uri'])
        # print "   %d %32.32s %s" % (i, track['artists'][0]['name'],
        #    track['name'])
        break


def show_track_pointer(results):
    tracks = results['tracks']
    show_tracks_iter(tracks['items'])
    while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks_iter(tracks['items'])


if token:
    sp = spotipy.Spotify(auth=token)

    """
    o = 0
    exit_cond = False
    outfile = open("library", 'wb')
    all_tracks = []
    while not exit_cond:
        try:
            tracks = sp.current_user_saved_tracks(limit=50, offset=len(all_tracks))
            all_tracks.extend(tracks['items'])
            print(len(all_tracks), all_tracks[-1]['track']['uri'])
            if len(tracks['items']) < 50:
                exit_cond = True
        except:
            exit_cond = True

    pickle.dump(all_tracks, outfile)
    outfile.close()
    """

    """
    outfile = open("vselecta", 'wb')

    all_tracks = []

    results = sp.user_playlist('1166931226', '6OQPg7PXMHK5iCRPsndmdY', fields="tracks,next")
    tracks = results['tracks']
    all_tracks.extend(tracks['items'])
    # show_tracks(tracks)
    print(len(tracks))
    while tracks['next']:
        tracks = sp.next(tracks)
        all_tracks.extend(tracks['items'])
        print(len(all_tracks))

    pickle.dump(all_tracks, outfile)
    outfile.close()
    """

    """
    "
    with open("library", "rb") as infile:
        library = pickle.load(infile)

    with open("vselecta", "rb") as infile:
        vselecta = pickle.load(infile)

    print(len(library), len(vselecta))

    with open("intersect", 'wb') as outfile:
        intersection = [ltrack for ltrack in library for vtrack in vselecta if ltrack['track']['uri'] in vtrack['track']['uri']]
        pickle.dump(intersection, outfile)
    
    """

    with open("intersect", 'rb') as infile:
        intersect = pickle.load(infile)
        print(len(intersect))

        show_track_pointer(inter)

else:
    print("Can't get token for", username)
