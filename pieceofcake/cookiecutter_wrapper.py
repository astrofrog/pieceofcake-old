import os
import json
import tempfile

from cookiecutter.main import cookiecutter


def render_template(template_url, parameters):

    tmpdir = tempfile.mkdtemp()

    cookiecutter(template_url,
                 extra_context=parameters,
                 overwrite_if_exists=True,
                 default_config=False,
                 no_input=True,
                 output_dir=tmpdir)

    project_path = os.path.join(tmpdir, parameters['project_name'])

    with open(os.path.join(project_path, "cookiecutter.json"), "w") as f:
        json.dump(parameters, f, ensure_ascii=False, indent=2, sort_keys=True)

    return project_path
