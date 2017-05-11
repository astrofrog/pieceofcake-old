import click

@click.command()
def setup_astropy_project():

    finish = False
    while not (finish):
    
        package_name = click.prompt('Your package name')

        module_name = click.prompt('The name of your module')

        short_description = click.prompt('Please enter a one sentence description of your package', default='', show_default=False)

        long_description = click.prompt('Please give a longer discription of your package',default='',show_default=False)

        author_name = click.prompt('Please give the names of the authors', default='', show_default=False)

        author_email = click.prompt('Please give a contact email', default='', show_default=False)
    
        licence = click.prompt(
            '''Please choose a licence [1]:
            1 - BSD 3-Clause
            2 - GNU GPL v3+
            3 - Apache Software Licence 2.0
            4 - BSD 2-Clause
            5 - Other''',
            default=1, type=click.IntRange(1, 5), show_default=False)

        project_url = click.prompt('Please give the project URL', default='', show_default=False)

        example_code = click.prompt('Do you want a folder for example code [Y/n]?', default=True, type=bool, show_default=False)

        include_cextern_folder = click.prompt('Do you want a folder for non-python C code [y/N]', default=False, show_default=False)

        project_version = click.prompt('What is the current version number of your project', default='0.0.dev')

        if (licence==1):
            licence_str = 'BSD 3-Clause'
        elif (licence==2):
            licence_str = 'GNU GPL v3+'
        elif (licence==3):
            licence_str = 'Apache Software Licence 2.0'
        elif (licence==4):
            licence_str = 'BSD 2-Clause'
        else:
            licence_str = 'Other'
    
        click.echo('\nHere is the project you set up:')
        click.echo('----------------------------------------')
        click.echo('package name:\t\t%s' %package_name)
        click.echo('module name:\t\t%s' %module_name)
        click.echo('author name:\t\t%s' %author_name)
        click.echo('author email:\t\t%s' %author_email)
        click.echo('licence:\t\t%s' %licence_str)
        click.echo('project version:\t%s' %project_version)
        click.echo('project url:\t\t%s' %project_url)
        click.echo('contains example code:\t%s' %('yes' if example_code else 'no'))
        click.echo('contains C code:\t%s' %('yes' if include_cextern_folder else 'no'))
        click.echo('short description:\t %s' %short_description)
        click.echo('long description:\n\t%s' %long_description)
        

        finish = click.prompt('\nAre you happy with your project? [y/n]', type=bool)

    project_values = { 'package name' : package_name,
                       'module name' : module_name,
                       'author name' : author_name,
                       'author email' : author_email,
                       'licence' : licence,
                       'project version' : project_version,
                       'project url' : project_url,
                       'example code' : example_code,
                       'cextern folder' : include_cextern_folder,
                       'short description' : short_description,
                       'long description' : long_description
                       }
    return project_values
    

    
if __name__ == '__main__':
    setup_astropy_project()



 #   @click.option('--include_example_code/--no-include_example_code', default=True, prompt=True,
  #            help='This includes a set of example python and cython files showing you how to use the package template. If you choose "n" then none of this will be included and you will have to populate the directory structure before you can import the package.')
