import click

from .utils import click_prompt_multiple_choice


def setup_astropy_project():

    finish = False

    while not finish:

        package_name = click.prompt('Your package name')

        module_name = click.prompt('The name of your module')

        short_description = click.prompt('Please enter a one sentence description of your package', default='', show_default=False)

        long_description = click.prompt('Please give a longer discription of your package',default='',show_default=False)

        author_name = click.prompt('Please give the names of the authors', default='', show_default=False)

        author_email = click.prompt('Please give a contact email', default='', show_default=False)

        licenses = ['BSD 3-Clause', 'GNU GPL v3+', 'Apache Software Licence 2.0', 'BSD 2-Clause', 'Other']

        licence = click_prompt_multiple_choice('Please choose a license', licenses)

        project_url = click.prompt('Please give the project URL', default='', show_default=False)

        example_code = click.prompt('Do you want a folder for example code [Y/n]?', default=True, type=bool, show_default=False)

        include_cextern_folder = click.prompt('Do you want a folder for non-python C code [y/N]', default=False, show_default=False)

        project_version = click.prompt('What is the current version number of your project', default='0.0.dev')

        initialize_git_repo = click.prompt('Should we initialize a git repository?', default='y')

        click.echo('\nHere is the project you set up:')
        click.echo('----------------------------------------')
        click.echo('package name:\t\t%s' % package_name)
        click.echo('module name:\t\t%s' % module_name)
        click.echo('author name:\t\t%s' % author_name)
        click.echo('author email:\t\t%s' % author_email)
        click.echo('licence:\t\t%s' % licence)
        click.echo('project version:\t%s' % project_version)
        click.echo('project url:\t\t%s' % project_url)
        click.echo('contains example code:\t%s' % ('yes' if example_code else 'no'))
        click.echo('contains C code:\t%s' % ('yes' if include_cextern_folder else 'no'))
        click.echo('short description:\t%s' % short_description)
        click.echo('long description:\t%s' % long_description)
        click.echo('initialize git repo:\t%s' % initialize_git_repo)

        finish = click.prompt('\nAre you happy with your project? [y/n]', type=bool)

    project_values = {'package_name': package_name,
                      'module_name': module_name,
                      'author_name': author_name,
                      'author_email': author_email,
                      'licence': licence,
                      'project_version': project_version,
                      'project_url': project_url,
                      'example_code': example_code,
                      'cextern_folder': include_cextern_folder,
                      'short_description': short_description,
                      'long_description': long_description,
                      'initialize_git_repo': initialize_git_repo
                      }

    return project_values
