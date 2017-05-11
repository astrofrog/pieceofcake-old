import click

@click.command()
def setup_astropy_project():

    redo = True
    while(redo):
    
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

        example_code = click.prompt('include example code[Y/n]?', default=True, type=bool, show_default=False)

        include_cextern_folder = click.prompt('Do you want a folder for non-python C code [y/N]', default=False, show_default=False)

    
        click.echo('\nyour project:')
        click.echo('package name: %s' %package_name)
        click.echo('licence: %d' %licence)
        click.echo('include example code: %s' %('yes' if example_code else 'no'))

        redo = click.prompt('\nDo you want to change anything [y/n]', type=bool)
    

    
if __name__ == '__main__':
    setup_astropy_project()



 #   @click.option('--include_example_code/--no-include_example_code', default=True, prompt=True,
  #            help='This includes a set of example python and cython files showing you how to use the package template. If you choose "n" then none of this will be included and you will have to populate the directory structure before you can import the package.')
