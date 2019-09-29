NEVER_LOVED_A_TRACK = "Boo boo... It seens you haven't loved any song yet... Start clicking the heart button on last.fm so we'll be able to help you remember the songs you really like!"
NEVER_LISTENED_TO_A_TRACK = "Hey! It seens you haven't listened to anything yet! What you're waiting for? Get it started!"
LASTFM_USER_NOT_FOUND = "We could not find the user you typed... Please check it and try again!"
SOMETHING_WENT_WRONG = "Something went wrong! Please try again later!"
REGISTERED_WITH_SUCCESS = "Success! Now we can start remembering! Type /loved or /listened to see the magic happening!"
HELP = """Type:
/start, to get ready to remember songs you may haven't listened in sooo long! We're sure they missed you!
/register [your last.fm user], so we can access your library
/loved, to get a random song from your list of favorited songs on your last.fm. So make sure to click the heart botton whenever you feel you'll always want to remember that specific song
/listened, to get a random (but relevant) artist from your last.fm library
"""


def LOVED_TRACK(
        track_name, track_url, artist_name,
        artist_url): return f"*Here's a track we think you'd like to remember:*\n[{track_name}]({track_url}) by [{artist_name}]({artist_url})"


def LISTENED_ARTIST(
        artist_name,
        artist_url): return f"*Here's an artist you might like to remember:*\n[{artist_name}]({artist_url})"
