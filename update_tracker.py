import pytumblr
import passwords as p

#authenticate
def get_client():
  client = pytumblr.TumblrRestClient(
    p.consumer_key,
    p.consumer_secret,
    p.oauth_token,
    p.oauth_secret
  )
  return client

#reblog injury post after x time 
def get_update(client, blogName):
  if len(client.posts(blogName, tag = 'reblog')['posts']) == 0:
    rb_date = '0000-00-00 00:00:00 GMT'
  else: 
    recent_reblog = client.posts(blogName, tag = 'reblog')['posts'][0] #assume is in chronological order 
    rb_id = recent_reblog["id"]
    rb_date = recent_reblog["date"]
    rb_key = recent_reblog["reblog_key"]

  recent_injury = client.posts(blogName, tag = 'injury')['posts'][0] 
  injury_id = recent_injury['id']
  injury_date = recent_injury['date']
  injury_key = recent_injury['reblog_key']

  if (rb_date > injury_date):
    # print ("reblog reblog")
    rb_reblog = recent_reblog['reblog']['comment'] #look at this to see what number is next
    prev_day = rb_reblog.split("Since Last Injury: ", 1)[1].strip('<br></p>')
    curr_day = int(prev_day) + 1
    reblog_text = "Days Since Last Injury: {}".format(curr_day)
    client.reblog(blogName, id=rb_id, reblog_key=rb_key, comment=reblog_text, tags=['reblog'])
  else:
    # print ('reblog injury')
    reblog_text = "Days Since Last Injury: 1"
    client.reblog(blogName, id=injury_id, reblog_key=injury_key, comment=reblog_text, tags=['reblog'])

#run update  
client = get_client()
blogName = 'kelvin-injury-tracker'
get_update(client, blogName)

