"""
pymake
-------------------------------

pymake package

 - E. Marinetto
 - nenetto@gmail.com
"""
import os
import json
import subprocess
import pkg_resources
from time import gmtime, strftime
from pymake.project_vars import project_vars, PrettyMessaging


def docker_ignore():

    file_path = os.path.join(root_path, '.dockerignore')
    if os.path.exists(file_path) and os.path.isfile(file_path):
        PrettyMessaging.print_info('Deleting old .dockerignore')
        os.remove(file_path)

    setup_template = pkg_resources.resource_filename(__name__, 'dockerignore.template')

    # Replacing variables
    with open(setup_template, 'r') as setup_file:
        setup_text = setup_file.read()

    PrettyMessaging.print_info('Saving .dockerignore')
    with open(file_path, 'w') as file_file:
        file_file.write(setup_text)


def docker_file():
    file_path = os.path.join(root_path, 'Dockerfile')
    if os.path.exists(file_path) and os.path.isfile(file_path):
        PrettyMessaging.print_info('Saving old Dockerfile')
        os.rename(file_path, os.path.join(root_path, 'Dockerfile' + strftime("%Y_%m_%d_%H_%M_%S", gmtime())))

    file_template = pkg_resources.resource_filename(__name__, 'Dockerfile.template')

    # Replacing variables
    with open(file_template, 'r') as file_file:
        file_text = file_file.read()

    file_text = file_text.replace('{project_root}', project_vars['project-name'].replace(' ', '_').lower())

    PrettyMessaging.print_info('Saving Dockerfile')
    with open(file_path, 'w') as file_file:
        file_file.write(file_text)

PrettyMessaging.print_separator()
PrettyMessaging.print_info('Configuring docker for project')

# Read pymake folder
PrettyMessaging.print_info('Reading docker configuration')
pymake_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), os.pardir))

# main package folder
package_path = os.path.abspath(os.path.join(pymake_path, os.pardir))

# root path
root_path = os.path.abspath(os.path.join(package_path, os.pardir))

# Read docker tag

pymakefile = os.path.abspath(os.path.join(package_path, 'pymakefile.json'))
pymakefile = json.load(open(pymakefile))

if ('docker-tag' in pymakefile.keys()) and (pymakefile['docker-tag'] == ''):
    PrettyMessaging.print_error('Tag not configured')
    PrettyMessaging.print_error('  Please set the tag for the docker image in pymakefile.json')
else:
    docker_tag = pymakefile['docker-tag']

PrettyMessaging.print_info('Docker tag is: [{0}]'.format(docker_tag))

# Creating Docker ignore
docker_ignore()

# Creating Dockerfile
docker_file()

# Scripts

# Create image
file_path = os.path.join(root_path, 'create_image.sh')
if os.path.exists(file_path) and os.path.isfile(file_path):
    PrettyMessaging.print_info('Deleting old create_image.sh')
    os.remove(file_path)

file_template = pkg_resources.resource_filename(__name__, 'create_image.template')

# Replacing variables
with open(file_template, 'r') as file_file:
    file_text = file_file.read()

file_text = file_text.replace('{docker_tag}', docker_tag)

PrettyMessaging.print_info('Saving create_image.sh')
with open(file_path, 'w') as file_file:
    file_file.write(file_text)

# Change permissions
subprocess.check_call(['chmod', '777', '{0}'.format(file_path)])

# Run container local
file_path = os.path.join(root_path, 'run_container_local.sh')
if os.path.exists(file_path) and os.path.isfile(file_path):
    PrettyMessaging.print_info('Deleting old run_container_local.sh')
    os.remove(file_path)

file_template = pkg_resources.resource_filename(__name__, 'run_container_local.template')

# Replacing variables
with open(file_template, 'r') as file_file:
    file_text = file_file.read()

file_text = file_text.replace('{docker_tag}', docker_tag)

PrettyMessaging.print_info('Saving run_container_local.sh')
with open(file_path, 'w') as file_file:
    file_file.write(file_text)

# Change permissions
subprocess.check_call(['chmod', '777', '{0}'.format(file_path)])

# aws push
file_path = os.path.join(root_path, 'aws_push.sh')
if os.path.exists(file_path) and os.path.isfile(file_path):
    PrettyMessaging.print_info('Deleting old aws_push.sh')
    os.remove(file_path)

file_template = pkg_resources.resource_filename(__name__, 'aws_push.template')

# Replacing variables
with open(file_template, 'r') as file_file:
    file_text = file_file.read()

file_text = file_text.replace('{docker_tag}', docker_tag)

PrettyMessaging.print_info('Saving aws_push.sh')
with open(file_path, 'w') as file_file:
    file_file.write(file_text)

# Change permissions
subprocess.check_call(['chmod', '777', '{0}'.format(file_path)])
PrettyMessaging.print_info('Docker helpers created successfully')
PrettyMessaging.print_separator()
