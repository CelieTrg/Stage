import argparse
import citi_lib
import json
import copy_parameter
import move_parameter


parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")
parser.add_argument('--new_context', action="store", help="Enter --new_context and the name context where you want to move the parameter")
parser.add_argument('--context', action="store", help="Enter --context and the name context where the parameter is located")
parser.add_argument('--move_parameter',action='store', help="Enter --move_paramameter and the name of the parameter you want to move")

args = parser.parse_args()

if args.move_parameter:

    name_project = args.project
    name_context =  args.context
    name_version = args.version
    name_parameter = args.move_parameter
    new_name_context = args.new_context

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")

    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'

    while name_context is None or name_context == '':
        name_context =  input("Name context? ")

    while new_name_context is None or new_name_context == '':
        new_name_context =  input("Name new context? ")



    new_parameter = move_parameter.move_param(name_project, name_version, name_context, name_parameter, new_name_context)
    print(json.dumps(new_parameter, indent=4, sort_keys=True))
