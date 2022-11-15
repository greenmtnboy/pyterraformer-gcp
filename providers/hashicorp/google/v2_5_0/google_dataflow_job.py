
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleDataflowJob(ResourceObject):
    """    
    Args:
        name (str): 
        temp_gcs_location (str): 
        template_gcs_path (str): 
    """
    _type = 'google_dataflow_job'
    
    def __init__(self,
        tf_id: str,
        name:str,
        temp_gcs_location:str,
        template_gcs_path:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        max_workers: Optional[float] = None,
        on_delete: Optional[str] = None,
        parameters: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        service_account_email: Optional[str] = None,
        zone: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if temp_gcs_location is not None:
                kwargs['temp_gcs_location'] = temp_gcs_location
            if template_gcs_path is not None:
                kwargs['template_gcs_path'] = template_gcs_path
            if id is not None:
                kwargs['id'] = id
            if max_workers is not None:
                kwargs['max_workers'] = max_workers
            if on_delete is not None:
                kwargs['on_delete'] = on_delete
            if parameters is not None:
                kwargs['parameters'] = parameters
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if service_account_email is not None:
                kwargs['service_account_email'] = service_account_email
            if zone is not None:
                kwargs['zone'] = zone
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
