import argparse
import citi_lib
import json
import  copy_context
import copy_parameter

parser = argparse.ArgumentParser()

parser.add_argument('--create_context', action="store", help="Enter --create_context and the name context you want to create")
parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")

args = parser.parse_args()

if args.create_context:

    name_project = args.project
    name_context =  args.create_context
    name_version = args.version

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")

    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'


    new_context = citi_lib.put_context(name_project, name_version, name_context)

    print(json.dumps(new_context, indent=4, sort_keys=True))
