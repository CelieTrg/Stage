import argparse
import citi_lib
import json
import  copy_context
import copy_parameter

parser = argparse.ArgumentParser()

parser.add_argument('--delete_context', action="store", help="Enter --delete_context and the name context you want to delete")
parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")

args = parser.parse_args()


if args.delete_context:

    name_project = args.project
    name_context =  args.delete_context
    name_version = args.version

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")

    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'


    context = citi_lib.delete_context(name_project, name_version, name_context)

    print(json.dumps(context, indent=4, sort_keys=True))
