import requests
import json

url_citi = 'http://localhost'


                                 #ACCOUNT


def get_list_name_accounts():

    response = requests.get(url_citi+'/accounts')
    array= response.text
    account = json.loads(array)
    tab_account = []
    #print(json.dumps(account, indent=4, sort_keys=True))

    for accounts in account['data']:
        accounts["name"]
        tab_account.append(accounts["name"])

    #print(tab_account)
    return tab_account



def get_accounts():

    response = requests.get(url_citi+'/accounts')
    array= response.text
    accounts = json.loads(array)

    #print(json.dumps(accounts, indent=4, sort_keys=True))
    return accounts



def get_account(name_account):

    response = requests.get(url_citi+'/accounts/'+name_account)
    array= response.text
    account = json.loads(array)

    #print(json.dumps(account, indent=4, sort_keys=True))
    return account



def delete_account(name_account):

    response = requests.delete(url_citi+'/accounts/'+name_account)
    array= response.text
    account = json.loads(array)

    #print(json.dumps(account, indent=4, sort_keys=True))
    return account



def put_account(name_account, host = '', username = '', new_account = '' ):

    if new_account != '' and host != '' and username != '':

        data = {"name":new_account, "host":host,"username":username}
        response = requests.put(url_citi+'/accounts/'+name_account,json=data)
        array= response.text
        account = json.loads(array)

    elif new_account!= '' and host == '' and username == '':

        data = {'name':new_account}
        response = requests.put(url_citi+'/accounts/'+name_account, json=data)
        array= response.text
        account = json.loads(array)

    elif new_account != '' and host != '' and username == '':

        data = {'name':new_account,"host":host}
        response = requests.put(url_citi+'/accounts/'+name_account, json=data)
        array= response.text
        account = json.loads(array)

    elif new_account != '' and host == '' and username != '':

        data = {'name':new_account,"username":username}
        response = requests.put(url_citi+'/accounts/'+name_account, json=data)
        array= response.text
        account = json.loads(array)

    elif new_account == '' and host != '' and username != '':

        data = {"host":host,"username":username}
        response = requests.put(url_citi+'/accounts/'+name_account,json=data)
        array= response.text
        account = json.loads(array)

    elif new_account == '' and host != '' and username == '':

        data = {"host":host}
        response = requests.put(url_citi+'/accounts/'+name_account,json=data)
        array= response.text
        account = json.loads(array)

    elif new_account == 'new_account' and host == 'host' and username != 'username':

        data = {"username":username}
        response = requests.put(url_citi+'/accounts/'+name_account,json=data)
        array= response.text
        account = json.loads(array)

    elif new_account == '' and host == '' and username == '':

        response = requests.put(url_citi+'/accounts/'+name_account)
        array= response.text
        account = json.loads(array)

    #print(json.dumps(account, indent=4, sort_keys=True))
    return account



                                    #GROUP


def get_list_name_groups():

    response = requests.get(url_citi+'/groups')
    array= response.text
    group = json.loads(array)
    tab_group = []

    for groups in group['data']:
        groups["name"]
        tab_group.append(groups["name"])

    #print(tab_group)
    return tab_group



def get_groups():

    response = requests.get(url_citi+'/groups')
    array= response.text
    groups = json.loads(array)

    #print(json.dumps(groups, indent=4, sort_keys=True))
    return groups



def get_group(name_group):

    response = requests.get(url_citi+'/groups/'+name_group)
    array= response.text
    group = json.loads(array)

    #print(json.dumps(group, indent=4, sort_keys=True))
    return group



def delete_group(name_group):

    response = requests.delete(url_citi+'/groups/'+name_group)
    array= response.text
    group = json.loads(array)

    #print(json.dumps(group, indent=4, sort_keys=True))
    return group



def put_group(name_group, new_name_group = ''):

    if new_name_group == '':
        response = requests.put(url_citi+'/groups/'+name_group)
        array= response.text
        group = json.loads(array)

    elif new_name_group != '':

        data = {'name':new_name_group}
        response = requests.put(url_citi+'/groups/'+name_group, json=data)
        array= response.text
        group = json.loads(array)

    #print(json.dumps(group, indent=4, sort_keys=True))
    return group



def get_group_permissions(name_group):

    response = requests.get(url_citi+'/groups/'+name_group+'/permissions')
    array= response.text
    group_permissions = json.loads(array)

    #print(json.dumps(group_permissions, indent=4, sort_keys=True))
    return group_permissions



                                       #PROJECT


def get_list_name_projects():

    response = requests.get(url_citi+'/projects')
    array= response.text
    project = json.loads(array)
    tab_project = []

    for projects in project['data']:

        projects["name"]
        tab_project.append(projects["name"])


    #print(tab_project)
    return tab_project



def get_projects():

    response = requests.get(url_citi+'/projects')
    array= response.text
    projects = json.loads(array)

    #print(json.dumps(projects, indent=4, sort_keys=True))
    return projects


def get_project(name_project):

    response = requests.get(url_citi+'/projects/'+name_project)
    array= response.text
    project = json.loads(array)

    #print(json.dumps(project, indent=4, sort_keys=True))
    return project



def delete_project(name_project):

    response = requests.delete(url_citi+'/projects/'+name_project)
    array= response.text
    project = json.loads(array)

    #print(json.dumps(project, indent=4, sort_keys=True))
    return project



def put_project(name_project, default_inventory = '', new_name_project = ''):

    if default_inventory == '' and new_name_project == '':

        response = requests.put(url_citi+'/projects/'+name_project)
        array= response.text
        project = json.loads(array)

    elif default_inventory!='' and new_name_project == '':

        data = {'default_inventory':default_inventory}
        response = requests.put(url_citi+'/projects/'+name_project, json=data)
        array= response.text
        project = json.loads(array)

    elif default_inventory=='' and new_name_project != '':

        data = {'name':new_name_project}
        response = requests.put(url_citi+'/projects/'+name_project, json=data)
        array= response.text
        project = json.loads(array)

    elif default_inventory!='' and new_name_project != '':

        data = {'name':new_name_project,'default_inventory':default_inventory}
        response = requests.put(url_citi+'/projects/'+name_project, json=data)
        array= response.text
        project = json.loads(array)

    #print(json.dumps(project, indent=4, sort_keys=True))
    return project



     #PLATEFORM


def get_project_plateforms(name_project):

    response = requests.get(url_citi +'/projects/'+name_project+'/plateforms')
    array= response.text
    project_plateforms = json.loads(array)

    #print(json.dumps(project_plateforms, indent=4, sort_keys=True))
    return project_plateforms



def get_plateform(name_project, name_plateform):

    response = requests.get(url_citi +'/projects/'+name_project+'/plateforms/'+name_plateform)
    array= response.text
    project_plateform  = json.loads(array)

    #print(json.dumps(project_plateform, indent=4, sort_keys=True))
    return project_plateform



def put_plateform_in_project(name_project, name_plateform, inventory = '', new_name_plateform = ''):

    if inventory != ''and new_name_plateform != '':

        data = {'name':new_name_plateform,'inventory':inventory}
        response = requests.put(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform, json = data)
        array= response.text
        plateform = json.loads(array)

    elif inventory == '' and new_name_plateform == '':

        response = requests.put(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform)
        array= response.text
        plateform = json.loads(array)

    elif inventory == '' and new_name_plateform != '':

        data = {'name':new_name_plateform}
        response = requests.put(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform, json = data)
        array= response.text
        plateform = json.loads(array)

    #print(json.dumps(plateform, indent=4, sort_keys=True))
    return plateform



def delete_plateform_in_project(name_project, name_plateform):

    response = requests.delete(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform)
    array= response.text
    plateform = json.loads(array)

    #print(json.dumps(plateform, indent=4, sort_keys=True))
    return plateform



       #ACCOUNT


def put_account_in_plateform(name_project, name_plateform, name_account):


    response = requests.put(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform+'/accounts/'+name_account)
    array= response.text
    account = json.loads(array)

    #print(json.dumps(account, indent=4, sort_keys=True))
    return account



def unset_accounts_from_plateform(name_project, name_plateform):

    response = requests.delete(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform+'/accounts')
    array= response.text
    unset = json.loads(array)

    #print(json.dumps(unset, indent=4, sort_keys=True))
    return unset



       #PERMISSIONS


def get_plateform_permissions(name_project, name_plateform):

    response = requests.get(url_citi +'/projects/'+name_project+'/plateforms/'+name_plateform+'/permissions')
    array= response.text
    project_plateform_permissions = json.loads(array)

    #print(json.dumps(project_plateform_permissions, indent=4, sort_keys=True))
    return project_plateform_permissions



def get_group_plateform_permissions(name_project, name_plateform, name_group):

    response = requests.get(url_citi +'/projects/'+name_project+'/plateforms/'+name_plateform+'/groups/'+name_group+'/permissions')
    array= response.text
    project_plateform_group_permissions = json.loads(array)

    #print(json.dumps(project_plateform_group_permissions, indent=4, sort_keys=True))
    return project_plateform_group_permissions



def delete_permissions_in_group(name_project, name_plateform, name_group):

    response = requests.delete(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform+'/groups/'+name_group+'/permissions')
    array= response.text
    permissions = json.loads(array)

    #print(json.dumps(permissions, indent=4, sort_keys=True))
    return permissions



#TO DO:

def post_permissions_in_group(name_project, name_plateform, name_group):

    response = requests.post(url_citi+'/projects/'+name_project+'/plateforms/'+name_plateform+'/groups/'+name_group+'/permissions')
    array= response.text
    new_version = json.loads(array)
    return False




        #TAG


def get_project_tags(name_project):

    response = requests.get(url_citi +'/projects/'+name_project+'/tags')
    array= response.text
    project_tags = json.loads(array)

    #print(json.dumps(project_tags, indent=4, sort_keys=True))
    return project_tags




def get_project_tag(name_project, name_tag):

    response = requests.get(url_citi +'/projects/'+name_project+'/tags/'+name_tag)
    array= response.text
    project_tag = json.loads(array)

    #print(json.dumps(project_tag, indent=4, sort_keys=True))
    return project_tag




def get_project_tag_latest(name_project, name_tag):

    response = requests.get(url_citi +'/projects/'+name_project+'/tags/'+name_tag+'/latest')
    array= response.text
    project_tag_latest = json.loads(array)

    #print(json.dumps(project_tag_latest, indent=4, sort_keys=True))
    return project_tag_latest



def get_project_tag_plateform_check(name_project, name_tag, name_plateform):

    response = requests.get(url_citi +'/projects/'+name_project+'/tags/'+name_tag+'/plateforms/'+name_plateform+'/check')
    array= response.text
    project_tag_plateform_check = json.loads(array)

    #print(json.dumps(project_tag_plateform_check, indent=4, sort_keys=True))
    return project_tag_plateform_check



        #VERSION


def get_project_tag_versions(name_project, name_tag):

    response = requests.get(url_citi+'/projects/'+name_project+'/tags/'+name_tag+'/versions')
    array= response.text
    project_tag_versions = json.loads(array)
    #print(json.dumps(project_tag_versions, indent=4, sort_keys=True))
    return project_tag_versions



def post_version_in_tag(name_project, name_tag, name_version = ''):

    if name_version == '' :

        response = requests.post(url_citi+'/projects/'+name_project+'/tags/'+name_tag+'/versions')
        array= response.text
        new_version = json.loads(array)

    elif name_version != '':

        data= {'version': name_version}
        response = requests.post(url_citi+'/projects/'+name_project+'/tags/'+name_tag+'/versions', json=data)
        array= response.text
        new_version = json.loads(array)

    #print(json.dumps(new_version, indent=4, sort_keys=True))
    return new_version




def get_project_versions(name_project):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions')
    array= response.text
    project_versions = json.loads(array)

    #print(json.dumps(project_versions, indent=4, sort_keys=True))
    return project_versions



def post_version_in_project(name_project, name_version = ''):

    if name_version == '':

        response = requests.post(url_citi+'/projects/'+name_project+'/versions')
        array= response.text
        new_version = json.loads(array)

    elif name_version != '':

        data= {'version': name_version}
        response = requests.post(url_citi+'/projects/'+name_project+'/versions', json=data)
        array= response.text
        new_version = json.loads(array)

    print(json.dumps(new_version, indent=4, sort_keys=True))
    return new_version



def get_project_version(name_project, name_version):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version)
    array= response.text
    project_version = json.loads(array)

    #print(json.dumps(project_version, indent=4, sort_keys=True))
    return project_version



        #CONTEXT


def get_contexts(name_project, name_version):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts')
    array= response.text
    project_version_contexts = json.loads(array)

    #print(json.dumps(project_version_contexts, indent=4, sort_keys=True))
    return project_version_contexts



def get_context(name_project, name_version, name_context):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context)
    array= response.text
    project_version_context = json.loads(array)

    #print(json.dumps(project_version_context, indent=4, sort_keys=True))
    return project_version_context



#TO DO:

def copy_context_with_version(name_project, name_version, name_context):

    data = {"name":name_context}
    response = requests.post(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/copy', json = data)
    array= response.text
    copy = json.loads(array)

    #print(json.dumps(copy, indent=4, sort_keys=True))
    return False




def delete_context(name_project, name_version, name_context):

    response = requests.delete(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context)
    array= response.text
    context = json.loads(array)

    #print(json.dumps(context, indent=4, sort_keys=True))
    return context



def put_context(name_project, name_version, name_context, new_name_context = ''):

    if new_name_context == '':

        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context)
        array= response.text
        context = json.loads(array)


    elif new_name_context != '':

        data = {'name':new_name_context}
        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context, json=data)
        array= response.text
        context = json.loads(array)

    #print(json.dumps(context, indent=4, sort_keys=True))
    return context




        #PARAMETER


def get_parameters(name_project, name_version, name_context):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context+'/parameters')
    array= response.text
    get_project_version_context_parameters = json.loads(array)

    #print(json.dumps(get_project_version_context_parameters, indent=4, sort_keys=True))
    return get_project_version_context_parameters



def get_parameter(name_project, name_version, name_context, name_parameter):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context+'/parameters/'+name_parameter)
    array= response.text
    project_tag_version_context_parameter = json.loads(array)

    #print(json.dumps(project_tag_version_context_parameter, indent=4, sort_keys=True))
    return project_tag_version_context_parameter



def delete_parameter_in_context(name_project, name_version, name_context, name_parameter):

    response = requests.delete(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context+'/parameters/'+name_parameter)
    array= response.text
    parameter = json.loads(array)

    #print(json.dumps(parameter, indent=4, sort_keys=True))
    return parameter



def put_parameter_in_context(name_project, name_version, name_context, name_parameter, type, comment, required, default_value, important, plateform = '', value = ''):

    if plateform == '' and value != '':

        raise ValueError("You must inform the plateform to inform the parameter value.")

    else:

        data = {'type':type, 'commentaire':comment,'required':required,'default_value':default_value,'important':important,'plateform':plateform,'value':value}
        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+name_context+'/parameters/'+name_parameter, json = data)
        array= response.text
        parameter = json.loads(array)

        #print(json.dumps(parameter, indent=4, sort_keys=True))
        return parameter


#try:

    #put_parameter_in_context()

#except ValueError as error:

    #print(error)



        #PLATEFORM

#TO DO:

def builds(name_project, name_version, name_plateform):
    response = requests.post(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/plateforms/'+name_plateform+'/builds')
    array= response.text
    build = json.loads(array)

    #print(json.dumps(build, indent=4, sort_keys=True))
    return False



def get_project_version_plateform_check(name_project, name_version, name_plateform):

    response = requests.get(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/plateforms/'+ name_plateform +'/check')
    array= response.text
    project_version_plateform_check = json.loads(array)

    #print(json.dumps(project_version_plateform_check, indent=4, sort_keys=True))
    return project_version_plateform_check



#TO DO:

def export_parameters_from_plateform(name_project, name_version, name_plateform):
    response = requests.post(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/plateforms/'+name_plateform+'/export')
    array= response.text
    parameters = json.loads(array)

    #print(json.dumps(parameters, indent=4, sort_keys=True))
    return False


                                                #TYPE


def get_types():

    response = requests.get(url_citi+'/types')
    array= response.text
    types = json.loads(array)

    #"print(json.dumps(types, indent=4, sort_keys=True))
    return types



                                                #WhoAmI


def get_whoAmI():

    response = requests.get(url_citi+'/whoAmI')
    array= response.text
    whoAmI = json.loads(array)

    #print(json.dumps(whoAmI, indent=4, sort_keys=True))
    return whoAmI
