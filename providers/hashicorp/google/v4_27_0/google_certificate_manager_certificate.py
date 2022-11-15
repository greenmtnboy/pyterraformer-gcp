
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ManagedItem():
        # non-optional-blocks
        dns_authorizations: Optional[List[str]] = None
        domains: Optional[List[str]] = None
        
# wrapper list class
class Managed(BlockList):
        items: List[ManagedItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SelfManagedItem():
        certificate_pem:str
        private_key_pem:str
        # non-optional-blocks
        
# wrapper list class
class SelfManaged(BlockList):
        items: List[SelfManagedItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCertificateManagerCertificate(ResourceObject):
    """    
    Args:
        name (str): A user-defined name of the certificate. Certificate names must be unique
                    The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
                    and all following characters must be a dash, underscore, letter or digit.
    """
    _type = 'google_certificate_manager_certificate'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        scope: Optional[str] = None,
        managed: Optional[Managed]=None,
        self_managed: Optional[SelfManaged]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if scope is not None:
                kwargs['scope'] = scope
            if managed is not None:
                kwargs['managed'] = managed
            if self_managed is not None:
                kwargs['self_managed'] = self_managed
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
