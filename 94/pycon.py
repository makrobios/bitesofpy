from collections import namedtuple
import os
import pickle
import urllib.request
import re
# from isodate import parse_duration

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, "rb") as pycon:
        data=pickle.load(pycon) 
    return data


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos, key= lambda v: int(v.metrics['viewCount']), reverse=True) 

def _like_ratio(video):
    likes = video.metrics['likeCount']
    dislikes = video.metrics['dislikeCount']
    views = video.metrics['viewCount']
    return (int(likes) - int(dislikes)) / int(views)

def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(videos, key=_like_ratio, reverse=True) 


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [video for video in videos if 'H' in video.duration] 


def _format_time(video):
    factor = {"H": 3600, "M": 60, "S": 1}
    seconds = []
    for match in re.finditer(r"(\d+)([HMS])", video.duration.strip("PT")):
        val = match.group(1)
        fact = match.group(2)
        seconds.append(int(val) * factor[fact])
    return sum(seconds)
    

def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    TWENTYFOUR = 24 * 60
    return [ v for v in videos if _format_time(v) < TWENTYFOUR ] 
    # return [v for v in videos if parse_duration(v.duration).seconds < TWENTYFOUR ]
