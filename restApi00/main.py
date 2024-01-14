import  requests


class Github:
    def __init__(self):
      self.api_url = "https://api.github.com/"

    def getUser(self,username):
        responce = requests.get(self.api_url + '/users/' + username)
        return responce.json()


github = Github()
while True:
    secim = input("\n1- Find User\n2- Get Resository\n3- Create Resository\n4- Exit\nSecim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            userName = input("Kullanıcı Adınızı Giriniz: ")
            result = github.getUser(userName)
            print(result)
        elif secim == "2":
            resositoryInput = input("Repo Adresini Giriniz: ")
        elif secim == "3":
            pass
        else:
            pass


