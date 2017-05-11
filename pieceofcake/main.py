import sys
import click

from . import __version__

from .astropy_template import setup_astropy_project
from .github import push_to_github
from .utils import click_prompt_multiple_choice
from .cookiecutter_wrapper import render_template

TEMPLATE = '/Users/tom/Dropbox/Code/Astropy/package-template'

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

    parameters = setup_astropy_project()

    local_folder = click.prompt('Where should the package be created on your computer?',
                                default='./{0}'.format(parameters['package_name']))

    render_template(TEMPLATE, parameters, local_folder)

    if parameters['initialize_git_repo'] == 'n':
        click.echo("Since you chose to not initialize a git repo, there isn't"
                   "much more we can do here at this stage!")
        sys.exit(0)

    print('')
    click.echo(click.style("Step 2 - Publishing to GitHub", 'magenta'))
    print('')

    push_options = ['Push to a new repository on GitHub',
                    'Push to an existing repository on GitHub',
                    'Don\'t push to GitHub']

    github_push = click_prompt_multiple_choice('Select one of the following options', push_options)

    if github_push.startswith('Push'):

        github_user = click.prompt('What is your GitHub username?')
        github_pass = click.prompt('What is your GitHub password?', hide_input=True)

        if 'new' in github_push:
            question = 'Which GitHub repository should be created?'
        else:
            question = 'Which GitHub repository should we push to?'

        repo_slug = click.prompt(question, default='{0}'.format(parameters['package_name']))

        push_to_github(local_folder, repo_slug, github_user, github_pass,
                       parameters['short_description'], new='new' in github_push)


main.add_command(quickstart)
