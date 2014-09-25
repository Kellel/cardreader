import requests
import json 

class Parse(object):
    headers = {
        "X-Parse-Application-Id": "xxxxxxxxxxxxxxxxx",
        "X-Parse-REST-API-Key": "xxxxxxxxxxxxxxxx",
        'content-type': 'application/json'
            }

    def getId(self):
        query = { 
            'order': '-userId',
            'limit': 1
                }

        user = requests.get('https://api.parse.com/1/users', params=query, headers=self.headers)

        data = user.json()['results'][0]
        return data['userId'] + 1

    def is_user(self, email):
        query = {
            'where': json.dumps({ 'email': email}) ,
            'limit': 1,
            }
        user = requests.get('https://api.parse.com/1/users', params=query, headers=self.headers)

        if user.json()['results'] == []:
            return False
        return True

    def createUser(self, data):
        user = requests.post('https://api.parse.com/1/users', data=json.dumps(data), headers=self.headers)
        print (user.json())
        return user.status_code, user.json()

    def getUserByUsername(self, username):
        query = {
            'where': json.dumps({ 'username': username.lower() }),
            'limit': 1,
            }
        user = requests.get('https://api.parse.com/1/users', params=query, headers=self.headers)

        results = user.json()['results']

        if results == []:
            return False
        else:
            return results[0]

    def getUserById(self, id):
        query = {
            'where': json.dumps({ 'userId': int(id) }),
            'limit': 1,
            }

        print query

        user = requests.get('https://api.parse.com/1/users', params=query, headers=self.headers)

        results = user.json()['results']
        print (results)
        print (user.url)

        if results == []:
            return False
        else:
            return results[0]
