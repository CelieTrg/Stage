import argparse
import citi_lib
import json
import  copy_context
import copy_parameter

parser = argparse.ArgumentParser()

parser.add_argument('--delete_parameter', action="store", help="Enter --delete_parameter and the name parameter you want to delete")
parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")
parser.add_argument('--context', action="store", help="Enter --context and the name context where the parameter is located")


args = parser.parse_args()


if args.delete_parameter:

    name_project = args.project
    name_context =  args.context
    name_version = args.version
    name_parameter = args.delete_parameter

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")

    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'

    while name_context is None or name_context == '':
        name_context =  input("Name context? ")


    parameter = citi_lib.delete_parameter_in_context(name_project, name_version, name_context, name_parameter)

    print(json.dumps(parameter, indent=4, sort_keys=True))
