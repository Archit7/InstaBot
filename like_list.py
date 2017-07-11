import requests
from get_post_id import get_post_id
from constants import BASE_URL,APP_ACCESS_TOKEN
def like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    get_like = requests.get(request_url).json()
    if get_like['meta']['code'] == 200:
        print "Media with media id %s is liked by following users;" % media_id
        if get_like['data'] > 0:
            for(index,user_likes) in enumerate(get_like['data']):
                print "%s,%s,%s,%s"%(index+1,user_likes['full_name'],user_likes['id'],user_likes['username'])
    else:
         print "wrong input"
