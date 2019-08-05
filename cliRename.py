import argparse
import citi_lib
import json
import copy_context
import requests

url_citi = 'http://localhost'

parser = argparse.ArgumentParser()

parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")
parser.add_argument('--new_context', action="store", help="Enter --new_context and the new name context")
parser.add_argument('--rename_context', action="store", help="Enter --rename_context and the name context you want to rename")

args = parser.parse_args()

if args.rename_context:

    name_project = args.project
    name_context =  args.rename_context
    name_version = args.version
    new_name_context = args.new_context

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")


    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'

    while new_name_context is None or name_context == '':
        new_name_context =  input("Name new context? ")


    new_context = citi_lib.put_context(name_project, name_version, new_name_context)

    cop_context = copy_context.get_context_parameters(name_project, name_version, name_context)

    parameters = cop_context['parameters']

    for parameter in parameters:

        name_parameter = parameter['name']
        new_name_parameter = name_parameter.replace(name_context, new_name_context, 1)
        parameter['values'] = []

        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json = parameter)
        array= response.text
        parameter = json.loads(array)

    context = citi_lib.delete_context(name_project, name_version, name_context)


    print(json.dumps(new_context, indent=4, sort_keys=True))
