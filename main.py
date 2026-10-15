import requests

star = 0
fork = 0
menu = """
[1] Check GitHub account by username
[2] Check public repositories by username
"""
print(menu)
choice = input("Choose an option [1, 2] ")

if choice == "1":
    username = input("Enter a GitHub username to analyze: ")
    r = requests.get(f"https://api.github.com/users/{username}")
    status = r.status_code
    if status == 200:
            content = r.json()
            login = content["login"]
            name = content["name"]
            public_repos = content["public_repos"]
            followers = content["followers"]
            following = content["following"]
            created_at = content["created_at"]
            bio = content["bio"]
            response = f"""
            Pseudo : {login}
            Name : {name}
            Repositories : {public_repos}
            Followers : {followers}
            Following : {following}
            Created at : {created_at}
            Bio : {bio}
            """
            print(response)
    else:
            print("Error, check the username exists.")
if choice == "2":
       user = input("Enter username : ")
       search = requests.get(f'https://api.github.com/users/{user}/repos')
       status = search.status_code
       if status == 200:
        content = search.json()
        nb = len(content)
        print(f"{nb} repositories found")
        for repo in content:
            name = repo["name"]
            description = repo["description"]
            language = repo["language"]
            stargazers_count = repo["stargazers_count"]
            star += stargazers_count
            forks_count = repo["forks_count"]
            fork += forks_count
            print(name, description, language, stargazers_count, forks_count)
            print("---------------------------")
       else:
                print("Please enter a good username")
       print(f"The account has {star} stars")
       print(f"The account has {fork} forks")


        
