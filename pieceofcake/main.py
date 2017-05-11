import sys
import click

from . import __version__

from .github import push_to_github


@click.group()
def main():
    pass


@click.command()
def quickstart():

    click.echo(click.style("Piece of Cake v{0}".format(__version__), 'red'))
    print('')
    print('Please answer the following questions to set up your project '
          '(just press Enter to accept default values when available)')

    # Set up repo

    print('')
    click.echo(click.style("Step 1 - Creating package", 'magenta'))
    print('')

    # parameters = setup_astropy_project()
    parameters = {'package_name': 'test', 'description': 'my package', 'initialize_git_repo':True}

    local_repo = click.prompt('Where should the package be created on your computer?',
                              default='./{0}'.format(parameters['package_name']))

    if parameters['initialize_git_repo'] == 'n':
        click.echo("Since you chose to not initialize a git repo, there isn't"
                   "much more we can do here at this stage!")
        sys.exit(0)

    print('')
    click.echo(click.style("Step 2 - Publishing to GitHub", 'magenta'))
    print('')

    github_push = click.prompt('Select one of the following options:\n'
                               '  [1] Push to a new repository on GitHub\n'
                               '  [2] Push to an existing repository on GitHub\n'
                               "  [3] Don't push to GitHub\n",
                               default=3,
                               type=click.IntRange(1, 3))

    if github_push != 3:

        github_user = click.prompt('What is your GitHub username?')
        github_pass = click.prompt('What is your GitHub password?', hide_input=True)

        if github_push == 1:
            question = 'Which GitHub repository should be created?'
        else:
            question = 'Which GitHub repository should we push to?'

        repo_slug = click.prompt(question, default='{1}'.format(parameters['package_name']))

        push_to_github(local_repo, repo_slug, github_user, github_pass, parameters['description'])


main.add_command(quickstart)
