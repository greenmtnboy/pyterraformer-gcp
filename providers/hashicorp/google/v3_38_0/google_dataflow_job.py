
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        update: Optional[str] = None




class GoogleDataflowJob(ResourceObject):
    """    
    Args:
        name (str): A unique name for the resource, required by Dataflow.
        temp_gcs_location (str): A writeable location on GCS for the Dataflow job to dump its temporary data.
        template_gcs_path (str): The GCS path to the Dataflow job template.
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
        additional_experiments: Optional[Set[str]] = None,
        id: Optional[str] = None,
        ip_configuration: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        machine_type: Optional[str] = None,
        max_workers: Optional[float] = None,
        network: Optional[str] = None,
        on_delete: Optional[str] = None,
        parameters: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        service_account_email: Optional[str] = None,
        subnetwork: Optional[str] = None,
        zone: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if temp_gcs_location is not None:
                kwargs['temp_gcs_location'] = temp_gcs_location
            if template_gcs_path is not None:
                kwargs['template_gcs_path'] = template_gcs_path
            if additional_experiments is not None:
                kwargs['additional_experiments'] = additional_experiments
            if id is not None:
                kwargs['id'] = id
            if ip_configuration is not None:
                kwargs['ip_configuration'] = ip_configuration
            if labels is not None:
                kwargs['labels'] = labels
            if machine_type is not None:
                kwargs['machine_type'] = machine_type
            if max_workers is not None:
                kwargs['max_workers'] = max_workers
            if network is not None:
                kwargs['network'] = network
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
            if subnetwork is not None:
                kwargs['subnetwork'] = subnetwork
            if zone is not None:
                kwargs['zone'] = zone
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
