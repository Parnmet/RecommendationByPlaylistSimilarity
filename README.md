# RecommendationByPlaylistSimilarity

This recommendation using playlist's text similarity and track similarity inside it
The concept is to recommend track to the users who named the playlist similarity and maybe have some tracks similarity!

First, The input is an incomplete playlist may or may not contains track, but they certaintly have a playlist name.
Then we check the similarity between input playlist name and playlist test set (It's HUGE!)
If the incomplete playlist has some tracks then we check the similarity of the contained track with other playlist.
Now we can recommend the track which user maybe like it, based on the similarity of other user's playlist.

This is not a good practice for recommender system but it good to realise that you should use Machine Learing or Neural Network, LOL!
