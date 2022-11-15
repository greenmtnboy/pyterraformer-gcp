
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CustomerManagedEncryptionItem():
        kms_key_name:str
        # non-optional-blocks
        
# wrapper list class
class CustomerManagedEncryption(BlockList):
        items: List[CustomerManagedEncryptionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReplicasItem():
        location:str
        # non-optional-blocks
        customer_managed_encryption: Optional[CustomerManagedEncryption]=None,
        
# wrapper list class
class Replicas(BlockList):
        items: List[ReplicasItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UserManagedItem():
        # non-optional-blocks
        customer_managed_encryption: Optional[CustomerManagedEncryption]=None,
        replicas: Optional[Replicas]=None,
        
# wrapper list class
class UserManaged(BlockList):
        items: List[UserManagedItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReplicationItem():
        # non-optional-blocks
        automatic: Optional[bool] = None
        customer_managed_encryption: Optional[CustomerManagedEncryption]=None,
        replicas: Optional[Replicas]=None,
        user_managed: Optional[UserManaged]=None,
        
# wrapper list class
class Replication(BlockList):
        items: List[ReplicationItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleSecretManagerSecret(ResourceObject):
    """    
    Args:
        secret_id (str): This must be unique within the project.
    """
    _type = 'google_secret_manager_secret'
    
    def __init__(self,
        tf_id: str,
        secret_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        customer_managed_encryption: Optional[CustomerManagedEncryption]=None,
        replicas: Optional[Replicas]=None,
        user_managed: Optional[UserManaged]=None,
        replication: Optional[Replication]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if secret_id is not None:
                kwargs['secret_id'] = secret_id
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if customer_managed_encryption is not None:
                kwargs['customer_managed_encryption'] = customer_managed_encryption
            if replicas is not None:
                kwargs['replicas'] = replicas
            if user_managed is not None:
                kwargs['user_managed'] = user_managed
            if replication is not None:
                kwargs['replication'] = replication
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
