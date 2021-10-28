import wolframalpha
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# Taking input from user
question = input('Question: ')
  
# App id obtained by the above steps
app_id = '9AWJ23-A38Q37YQRE'
  
# Instance of wolf ram alpha 
# client class
client = wolframalpha.Client(app_id)
  
# Stores the response from 
# wolf ram alpha
res = client.query(question)
  
# Includes only text from the response
answer = next(res.results).text
  
print(answer)