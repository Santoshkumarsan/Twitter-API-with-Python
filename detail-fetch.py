
import twitter
api = twitter.Api(consumer_key='x**************************',
  consumer_secret='Rz********************************************',
    access_token_key='7**************************************************',
    access_token_secret='c*************************************************')

print(api.VerifyCredentials())
# get list of friends
users = api.GetFriends()
print([u.name for u in users])
