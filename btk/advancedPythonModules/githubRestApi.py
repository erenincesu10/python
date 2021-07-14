

import requests
import json

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def getUser(self,username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

github = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Exit\n Seçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            username = input("Kullanıcı adını giriniz : ")
            result = github.getUser(username)
            print(f' name : {result["name"]} public repos : {result["public_repos"]} follower : {result["followers"]}')

        elif secim == "2":
            username = input("Kullanıcı adını giriniz : ")
            result = github.getRepositories(username)
            for repo in result:
               print(repo['name'])

        else:
            print("Yanlış seçim")
