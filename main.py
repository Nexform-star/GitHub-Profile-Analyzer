import requests


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
       page = 1
       star = 0
       fork = 0
       user = input("Enter username : ")
       best_stargazers_count = 0
       best_name = ""
       total_repos = 0
       while True:
        search = requests.get(
        f"https://api.github.com/users/{user}/repos?page={page}",
        params={"per_page": 100}
    )
        status = search.status_code
        if status == 200:
            content = search.json()
            nb = len(content)
            print(f"{total_repos} repositories found")
            if len(content) == 0:
                 break
            else:
                for repo in content:
                    total_repos += 1
                    name = repo["name"]
                    description = repo["description"]
                    language = repo["language"]
                    stargazers_count = repo["stargazers_count"]
                    star += stargazers_count
                    forks_count = repo["forks_count"]
                    fork += forks_count
                    if language is None:
                        language = "Not specified"
                    if description is None:
                        description = "No description"
                    if stargazers_count > best_stargazers_count:
                        best_stargazers_count = stargazers_count
                        best_name = name
                    print(f"Name : {name} | Description : {description} | Language : {language} | Stars : {stargazers_count} | Forks : {forks_count}")
                    print("---------------------------")
            page += 1
        else:
            print("Please enter a good username")
            break

       print(f"The account has {star} stars")
       print(f"The account has {fork} forks")
       print(f"The best repo is {best_name} with {best_stargazers_count} stars")

