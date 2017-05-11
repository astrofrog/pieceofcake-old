def push_to_github(local_folder, repo_slug, github_user, github_pass, description, new=True):

    print(local_folder)

    # Create repo on GitHub if needed
    import github
    gh = github.Github(login_or_token=github_user,
                       password=github_pass)
    user = gh.get_user()
    repo = user.create_repo(repo_slug, description=description)

    # Add remote to local git folder and push
    from git import Repo
    new_repo = Repo.init(local_folder)
    origin = new_repo.create_remote('origin', repo.clone_url)
    origin.push('master')
