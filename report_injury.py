import pytumblr
import sys
import passwords as p

# to run: python report_injury.py area_injured cause
#authenticate
def get_client():
  client = pytumblr.TumblrRestClient(
    p.consumer_key,
    p.consumer_secret,
    p.oauth_token,
    p.oauth_secret
  )
  return client

def report_injury(client, blogName, area, cause):
  bodytext = "<p>Affected area: {}</p> <p>Cause: {}</p> <p><b>Days Since Last Injury: 0</b><p>".format(area, cause)
  client.create_text(blogName, state="published", slug="testing-text-posts", title="Injury Report", body=bodytext, tags = ['injury', area, cause])
  print ("injury reported")

client = get_client()
blogName = 'kelvin-injury-tracker'

if (len(sys.argv) != 3):
    raise TypeError("must be run with two arguments, the area_injured and the cause")
area_injured = sys.argv[1]
cause = sys.argv[2]

# print (area_injured, cause)
report_injury(client, blogName, area_injured, cause) 


