import requests
#AccessToken
ACCESS_TOKEN = '1735257996.ba62c56.251e4ca2a3584ac29cc4482f396dfcb9'
BASE_URL = 'https://api.instagram.com/v1/'

# function to print personal instagram information
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % ACCESS_TOKEN
    print('REQUESTING URL FOR DATA:' + request_url)
    my_info = requests.get(request_url).json()
    print('\n MY INFO IS: \n')
    print(my_info)

self_info()

print('\n')

instagram_username = input("Enter the username for which you want to perform any of the action?\n\n")

# Take input from the user to execute any one from the following tasks
print("What do you wish to do from the following tasks:\n\n"
      "1.Get the user's Instagram ID\n"
      "2.Get the user's recent posts\n"
      "3.Like the posts\n"
      "4.See the user's comments\n"
      "5.Comment on a user's post\n"
      "6.Get comments including specific words\n"
      "7.Print average number of words of a comment\n"
      "8.Delete a comment\n")

make_a_choice = input("Select from the above options\n\n")
print("\nYou have entered %s\n" % make_a_choice)


# Function to print the user instagram id
def get_user_id_by_username(username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (username, ACCESS_TOKEN)
    print('\nREQUESTING URL FOR DATA : \n' + request_url)

    search_results = requests.get(request_url).json()

    if search_results['meta']['code'] == 200:
        if len(search_results['data']):
            print('\nUser Id: \n')
            print(search_results['data'][0]['id'])
            return search_results['data'][0]['id']
        else:
            print('\nUser does not exist!\n')
    else:
        print('\nStatus code other than 200 was received!\n')

    return None


# Function to print all the posts of instagram
def get_users_recent_posts(username):
    global all_posts
    instagram_user_id = get_user_id_by_username(username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (instagram_user_id, ACCESS_TOKEN)

    print('\nREQUESTING URL FOR DATA : \n' + request_url)

    recent_posts = requests.get(request_url).json()

    if recent_posts['meta']['code'] == 200:
        if len(recent_posts['data']):
            for all_posts in recent_posts['data']:
                print('\n')
                print('Image url :')
                print(all_posts['images']['thumbnail']['url'])
                print('Number of likes :')
                print(all_posts['likes']['count'])
                print('Id Number :')
                print(all_posts['id'])

            return all_posts['id']

        else:
            print('\n No recent post by this user!\n')

    else:
        print('\nStatus code other than 200 was received!\n')


def select_post():
    # global variable can be used in any of the functions
    global post_id
    get_users_recent_posts(instagram_username)
    post_id = input("\nEnter the post id you want to select\n")


# Function to like the any instagram post by id
def like_post_for_user(username):
    get_users_recent_posts(username)
    select_post()

    payload = {'access_token': ACCESS_TOKEN}
    request_url = (BASE_URL + 'media/%s/likes') % post_id

    response_to_like = requests.post(request_url, payload).json()

    print(response_to_like)

    if response_to_like['meta']['code'] == 200:
        print('\nLiked Successfully\n')
    else:
        print('\nPlease try again!\n')


# function to print all the comments for any post by id
def get_comment_id_for_a_post(username):
    post_id = get_users_recent_posts(username)

    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, ACCESS_TOKEN)

    print('\nREQUESTING COMMENTS FROM INSTAGRAM USING %s\n' % request_url)

    global comments
    # global variable can be used in any of the functions

    comments = requests.get(request_url).json()

    for comment in comments['data']:
        print('%s commented: %s' % (comment['from']['username'], comment['text']))
        print(comment['id'])
        print('\n')


# Function to post a new comment on any post
def post_a_new_comment(username):
    write_a_comment = input("Enter the comment you want to post.\n")
    get_users_recent_posts(username)
    select_post()
    request_url = (BASE_URL + 'media/%s/comments') % post_id

    request_data = {'access_token': ACCESS_TOKEN, 'text': '%s' % write_a_comment}

    comment_request = requests.post(request_url, request_data).json()

    print(comment_request)

    if comment_request['meta']['code'] == 200:
        print("\nComment posted\n")

    else:
        print("\nPlease try again!\n")


# function to print all the comments containing a specific word

def get_a_comment_by_word(username):
    searched = input('Enter the text to search in comments : ')
    post_id = get_users_recent_posts(username)

    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, ACCESS_TOKEN)

    print('\nREQUESTING COMMENTS FROM INSTAGRAM USING %s\n' % request_url)
    global comments
    # global variable can be used in any of the functions

    comments = requests.get(request_url).json()

    for comment in comments['data']:
        if searched in comment['text']:
            print('%s commented: %s' % (comment['from']['username'], comment['text']))
            print(comment['id'])
            print('\n')
        else:
            print('Comment not found')


# Prints the number of words of every comment of the post
def average_number_of_words_in_comment(username):
    get_comment_id_for_a_post(username)

    for comment in comments['data']:
        print(comment['text'].split())
        print("Number of words in the comment = %s\n" % (len(comment['text'].split())))


# function to delete a comment by post id and comment id
def delete_a_comment(username):
    select_post()
    get_comment_id_for_a_post(username)
    comment_id = input("Enter the comment id you want to delete\n")
    # takes input from the user for comment id to be deleted

    request_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (post_id, comment_id, ACCESS_TOKEN)

    print('\nREQUESTING DELETING COMMENTS FROM INSTAGRAM USING %s\n' % request_url)

    request = requests.delete(request_url)

    print(request)

    if request['meta']['code'] == 200:
        print('\nComment deleted successfully\n')

    else:
        print('\nTry again...........!!!!\n')


# conditions to call the function based upon the choice input from the user
if make_a_choice == "1":
    print(get_user_id_by_username(instagram_username))

elif make_a_choice == "2":
    get_users_recent_posts(instagram_username)

elif make_a_choice == "3":
    like_post_for_user(instagram_username)

elif make_a_choice == "4":
    get_comment_id_for_a_post(instagram_username)

elif make_a_choice == "5":
    post_a_new_comment(instagram_username)

elif make_a_choice == "6":
    get_a_comment_by_word(instagram_username)

elif make_a_choice == "7":
    average_number_of_words_in_comment(instagram_username)

elif make_a_choice == "8":
    delete_a_comment(instagram_username)

else:
    print("Select a suitable option.....................!!!!!!!!")