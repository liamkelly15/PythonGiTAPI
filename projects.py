import gitlab
import json
import logindetails


with open(logindetails.baseAttributes) as json_file:  
       baseAttributes=json.loads(json_file.read())
#print(json.dumps(baseAttributes,indent=4))

with open(logindetails.pushrules) as json_file:  
       pushrules=json.loads(json_file.read())
#print(json.dumps(pushrules,indent=4))


class MockProject:
    """The MockProject Class is used to Mock the GitLab API calls for Testing"""

    def __init__(self,attributes):
        self.attributes = attributes
    


class Project:
    """The Project Class represents an instance of all the GitLab Projects and associated Namespaces - The projects paramater is an API call 
    on a GitLab object to all the projects"""

    def __init__(self, projects, namespaces):
        self.projects = projects
        self.namespaces = namespaces
        self.baseAttributes = baseAttributes
        self.pushrules=pushrules
    

    def listProjectsPaths(self):
        """The listProjectsPath function will list all the GitLab projects the current user has membership of"""
        
        projects =  self.projects.list(membership=True,all=True,perpage=30)
    
        #print(projects)
        projectPaths = []
        for p in projects:
            #print(p['attributes'])
            projectDetails = {
                'id': p.attributes['id'],
                'name': p.attributes['path_with_namespace']
            }
            projectPaths.append(projectDetails)
            
        return projectPaths
        #return projects
        

    def checkifprojectexistonGitlab(self,pathnamelower):
        """The checkifprojectexistsonGitlab function is used to check if a Project name is already in use before attempting 
        to create a new Project using that name"""
        projects =  self.projects.list(membership=True,all=True)
        for p in projects:
            #print(p.attributes['path_with_namespace'])
            #print(newpathnamelower)
            #if the project exists in Gltlab return the project and update the push rules
            if (p.attributes['path_with_namespace']==pathnamelower):
               return p  
        #if the project does not exist on Gitlab return empty and create a new project      
        return None
         

    def updateProjectpushrules(self,project):
        """The createProject function is used to update the Project pushrules in GitLab - The Project object is required as paramater"""
            
        prules=project.pushrules.get()
        prules.commit_message_regex=pushrules['commit_message_regex']
        prules.commit_message_negative_regex=pushrules['commit_message_negative_regex']
        prules.branch_name_regex= pushrules['branch_name_regex']
        prules.deny_delete_tag=pushrules['deny_delete_tag']
        prules.member_check=pushrules['member_check']
        prules.prevent_secrets=pushrules['prevent_secrets']
        prules.author_email_regex=pushrules['author_email_regex']
        prules.file_name_regex=pushrules['file_name_regex']
        prules.max_file_size=pushrules['max_file_size']
        
        #The commit_committer_chck requires a higher level of Gitlab access
        #prules.commit_committer_check=pushrules['commit_committer_check']
        #prules.save()
        
        prules.save()
        
        



    def createProject(self,namespace,name):
        """The createProject function is used to create a new Project in GitLab - The namespace and a Project name are required as paramaters
        These paramaters are stored in the ProjectList JSON file"""
        
        namespaceid = self.namespaces.get(namespace).attributes['id']
        self.baseAttributes['namespace_id'] = namespaceid
        self.baseAttributes['name'] = name

        newProject = self.projects.create(self.baseAttributes)
        
        #newProject.pushrules.create(self.pushrules)
        #newProject.save()       

        prules=newProject.pushrules.get()
        prules.commit_message_regex=pushrules['commit_message_regex']
        prules.commit_message_negative_regex=pushrules['commit_message_negative_regex']
        prules.branch_name_regex= pushrules['branch_name_regex']
        prules.deny_delete_tag=pushrules['deny_delete_tag']
        prules.member_check=pushrules['member_check']
        prules.prevent_secrets=pushrules['prevent_secrets']
        prules.author_email_regex=pushrules['author_email_regex']
        prules.file_name_regex=pushrules['file_name_regex']
        prules.max_file_size=pushrules['max_file_size']
        
        #The commit_committer_chck requires a higher level of Gitlab access
        #prules.commit_committer_check=pushrules['commit_committer_check']
        #prules.save()
        
        prules.save()
        
        return newProject
    
    def deleteProject(self,id):
        """The createProject function is used to delete a Project in GitLab - The Project ID is passed to the function to identify the Project to be deleted
        The function will be called if the Project in GitLab no longr exists on the ProjectList SON file"""
        
        #self.projects.delete(id)
        #return newProject
    
    def addUserToProject(self, projectId, userId, accessLevel ):
        project = self.projects.get(projectId)
        project.members.create(
            {
                'user_id': userId,
                'access_level': accessLevel
            } 
        )
    

    def addGroupToProject(self, projectId, groupId, accessLevel):
        project = self.projects.get(projectId)
        project.share(groupId, accessLevel)

