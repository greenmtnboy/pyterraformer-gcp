
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleFirestoreDocument(ResourceObject):
    """    
    Args:
        collection (str): The collection ID, relative to database. For example: chatrooms or chatrooms/my-document/private-messages.
        document_id (str): The client-assigned document ID to use for this document during creation.
        fields (str): The document's [fields](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents) formated as a json string.
    """
    _type = 'google_firestore_document'
    
    def __init__(self,
        tf_id: str,
        collection:str,
        document_id:str,
        fields:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        database: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if collection is not None:
                kwargs['collection'] = collection
            if document_id is not None:
                kwargs['document_id'] = document_id
            if fields is not None:
                kwargs['fields'] = fields
            if database is not None:
                kwargs['database'] = database
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
