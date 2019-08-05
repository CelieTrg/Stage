import argparse
import citi_lib
import json
import  copy_context
import copy_parameter

parser = argparse.ArgumentParser()

parser.add_argument('--copy_context', action="store", help="Enter --copy_context and the name context you want to copy")
parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")
parser.add_argument('--new_context', action="store", help="Enter --new_context and the name context you want to create with the copy")

args = parser.parse_args()


if args.copy_context:

    name_project = args.project
    name_context =  args.copy_context
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


    copy = copy_context.get_context_parameters(name_project,name_version,name_context)
    new_context = copy_context.copy_new_context(name_project, name_version, name_context, new_name_context)

    print(json.dumps(new_context, indent=4, sort_keys=True))
