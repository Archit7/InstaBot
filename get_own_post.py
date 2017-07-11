import requests
import urllib
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_post_id import get_post_id

def get_own_post():
    #function logic
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        # extract post ID
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
            print own_media['data'][0]['id']
            return own_media['data'][0]['id']

        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'