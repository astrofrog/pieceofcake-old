def push_to_github(local_folder, repo_slug, github_user, github_pass, description):
    import github
    gh = github.Github(login_or_token=github_user,
                       password=github_pass)
    user = gh.get_user()
    repo = user.create_repo(repo_slug, description=description, auto_init=True)
    return repo
