from auth import Auth
from projects import Project
from groups import Groups
from namespaces import Namespaces
import logindetails
import json

with open(logindetails.ProjectList) as json_file:  
       ProjectList=json.loads(json_file.read())

class GitlabManager:
    #"""This is the main Class"""
    print('starting now to auth')
    auth = Auth(username = logindetails.user, token = logindetails.token )
    activeGitlab = auth.authorizeUser()

    #create a Project object called project
    project = Project(projects = activeGitlab.projects, namespaces=activeGitlab.namespaces)
    projpaths = project.listProjectsPaths()
    print('These are your Projects')
    for p in projpaths:
        print(p)
        #comment

    for key in ProjectList:
      projectname=key
      #print(projectname)
      projectnamespace=ProjectList[key]
      #print(projectnamespace)
      pathname=(projectnamespace+'/'+projectname)
      pathnamelower=pathname.lower()
      #print(pathnamelower)

      #check if the projects on ProjectList exist on Gitlab - If not add them to Gitlab - If exists then write the standard pushrules
      project_in_Gitlab=project.checkifprojectexistonGitlab(pathnamelower)
      if project_in_Gitlab is None:
        print ('creating a new project called '+pathnamelower)
        newproj=project.createProject(namespace=projectnamespace,name=projectname)
        print(newproj.pushrules.get())
        print(newproj.attributes)
      else:
        project.updateProjectpushrules(project_in_Gitlab)
        print ('The project '+pathnamelower+' already exists - no new project created - Push rules updated')



    #check if the projects on Gitlab still remain on the ProjectList - if not remove them from Gitlab
    for p in projpaths:
        print (p['name'])
        project_on_list=False
        for key in ProjectList:
           projectnameonlist=key
           #print(projectnameonlist)
           projectnamespaceonlist=ProjectList[key]
           #print(projectnamespaceonlist)
           pathname=(projectnamespaceonlist+'/'+projectnameonlist)
           pathnamelower=pathname.lower()
           #print(pathnamelower)
           #check if the project on Gitlab exists on ProjectList - If not remove from Gitlab
           if (p['name'] == pathnamelower):
            project_on_list=True
            print('setting Gitlab project on list to True-No action required')
            break
        
        if not (project_on_list):
          print('removing the following project from Gitlab no longer on list '+ p['name'].lower())
          project.deleteProject(p['id'])
          
        

    # create a Namespaces object called namespaces
    namespaces = Namespaces(activeGitlab.namespaces)
    namespaceList = namespaces.listNamespaces()

    print('These are all the namespaces')
    for n in namespaceList:
        print(n)

    # create a Groups object called groups
    groups = Groups(activeGitlab.groups)
    groupList = groups.listGroups()

    print('These are all the groups')
    for g in groupList:
        print(g)


    print('These are all the Members in the Group TestGitLabManage')
    members = groups.listGroupMembers('TestGitLabManage')
    for m in members:
        print(m)


    #print('Create a new project')

    #newproj = project.createProject(namespace='TestGitLabManage',name = 'liamtestingpro2')

    #need a new instance here to see updated projecs
    #print('These are your Projects after adding a new one')
    #for p in proj:
    #    print(p) 


    
   
    


    

    