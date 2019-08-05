import argparse
import citi_lib
import json
import  copy_context
import copy_parameter

parser = argparse.ArgumentParser()

parser.add_argument('--add_parameter', action="store", help="Enter --add_parameter and the name parameter you want to add")
parser.add_argument('--project', action="store", help="Enter --project and the name of the project")
parser.add_argument('--version', action="store", help="Enter --version and the name of the version")
parser.add_argument('--context', action="store", help="Enter --context and the name context where you want to add your parameter")
parser.add_argument('--type', action="store", help="Enter --type and the type of your parameter")
parser.add_argument('--comment', action="store", help="Enter --comment and the comment of your parameter")
parser.add_argument('--required', action="store", type=int, help="Enter --required and the required of your parameter (boolean)")
parser.add_argument('--default_value', action="store", help="Enter --required and the default_value of your parameter")
parser.add_argument('--important', action="store", type=int, help="Enter --important and the important of your parameter (boolean)")
parser.add_argument('--plateform', action="store", help="Enter --plateform and the plateform of your parameter")
parser.add_argument('--value', action="store", type=int, help="Enter --value and the value of your parameter only if plateform is inform")


args = parser.parse_args()


if args.add_parameter:

    name_project = args.project
    name_context =  args.context
    name_version = args.version
    name_parameter = args.add_parameter
    type = args.type
    comment = args.comment
    required = args.required
    default_value = args.default_value
    important = args.important
    plateform = args.plateform
    value = args.value

    while name_project is None or name_project == '':
        print(citi_lib.get_list_name_projects())
        name_project = input("Name project? ")

    while name_version is None:
        name_version = input("Name version? ")
        if name_version == '':
            name_version = 'latest'

    while name_context is None or name_context == '':
        name_context =  input("Name context? ")

    while name_parameter is None or name_parameter == '':
        name_parameter =  input("Name parameter? ")

    while type is None:
        type =  input("Type? ")

    while comment is None:
        comment =  input("Comment? ")

    while required is None:
        required =  input("Required? (boolean) ")

    while default_value is None:
        default_value =  input("Default_value? ")

    while important is None:
        important =  input("Important? (boolean) ")

    while plateform is None:
        plateform =  input("Plateform? ")

    while value is None:
        value =  input("Value? ")


    new_parameter = citi_lib.put_parameter_in_context(name_project, name_version, name_context, name_context+'_'+name_parameter, type, comment, required, default_value, important, plateform, value)

    print(json.dumps(new_parameter, indent=4, sort_keys=True))
