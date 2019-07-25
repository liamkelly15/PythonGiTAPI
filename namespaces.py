import gitlab

class Namespaces:
    """This is the Namespaces Class"""
    def __init__(self, namespaces):
        self.namespaces = namespaces

    def listNamespaces(self):
        """ This is the listNamespaces function-The function returns all the namespacess in the GitLab account """
        namespaces = self.namespaces.list(membership=True,all=True)
        namespaceList = []
        for n in namespaces: 
            namespaceDetails = {
                'namespace_id' : n.attributes['id'],
                'namespace_name' : n.attributes['name']
            }
            namespaceList.append(namespaceDetails)
        return namespaceList

   