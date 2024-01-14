import requests
#bu proje githubda ki dosyaları cekmeye yarıyor
# ücretsiz api kullanılarak yapılmıştır sorgu limiti : 1.5k
class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    def createUser(self, name):
        responce = requests.post(self.api_url + '/users/repos?access_token' + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https: //mecellem.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has _wiki": True
        })
        return responce.json()


github = Github()

while True:
    secim = input("1- Find User:  \n2- Get Repositories:  \n3- Create Repositories:  \n4- Exit:  \nSeçim: ")

    if secim == "4":
        print("Çıkış Yaptınız")
        break
    else:
        if secim == "1":
            username = input("Kullanıcı Adı Giriniz: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public Repos: {result['public_repos']} follower: {result['followers']}")

        elif secim == "2":
            username = input('Username Giriniz: : ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == "3":
            name = input("Repo Address Giriniz:")
            result = github.createUser(name)
            print(result)
        else:
            print("Yanlış Secim Yaptınız")
