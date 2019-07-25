import click
from auth import Auth
from projects import Project

class GitlabCli:
    
    @click.group()
    @click.option('-u', prompt='Enter username', help='Gitlab account username')
    @click.option('-k', prompt='Enter personal access key', help='Personal access key')
    @click.pass_context
    def cli(context, u, k):
        context.ensure_object(dict)
        username=u
        accessKey=k
        auth = Auth(username= username, token=accessKey)
        activeGitlab = auth.getActiveGitlab()
        context.obj['active_gitlab'] = activeGitlab

    @cli.command()  # @cli, not @click!
    @click.option('-l', is_flag=True, help='List all owned projects')
    @click.option('-c', is_flag=True, help='Create a project')
    @click.option('--namespace', help='The namespace to create a project in' )
    @click.option('--name', help='The name of a project to create' )
    @click.pass_context
    def project(context, l, c, namespace, name): 
        activeGitlab = context.obj['active_gitlab']
        project = Project(projects = activeGitlab.projects, namespaces=activeGitlab.namespaces)
        if l:
            projects = project.listProjectsPaths()
            for proj in projects:
                print(proj) 
        if c:
            project.createProject(namespace=namespace, name=name)


if __name__ == '__main__':
    GitlabCli().cli()
