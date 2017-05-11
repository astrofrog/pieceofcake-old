import os
import json
import shutil
import tempfile

from cookiecutter.main import cookiecutter


def render_template(template_url, parameters, local_folder):

    tmpdir = tempfile.mkdtemp()

    cookiecutter(template_url,
                 extra_context=parameters,
                 overwrite_if_exists=True,
                 default_config=False,
                 no_input=True,
                 output_dir=tmpdir)

    project_path = os.path.join(tmpdir, parameters['package_name'])

    with open(os.path.join(project_path, "cookiecutter.json"), "w") as f:
        json.dump(parameters, f, ensure_ascii=False, indent=2, sort_keys=True)

    shutil.copytree(project_path, local_folder)
