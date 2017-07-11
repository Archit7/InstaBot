import requests
from get_post_id import get_post_id
from constants import BASE_URL,APP_ACCESS_TOKEN

def list_of_comments(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    get_comment = requests.get(request_url).json()
    if get_comment['meta']['code'] == 200:
        print "Media with media id %s has comments from following users;" % media_id
        if get_comment['data'] > 0:
            for(index,user_comments) in enumerate(get_comment['data']):
                # print ("%s,%s,%s" % (index + 1, user_comments['id'], user_comments['username']))
                # print (user_comments)
                print ("%d. %s is commented by %s")%(index+1,user_comments['text'],user_comments['from']['full_name'])
    else:
         print "wrong input"

