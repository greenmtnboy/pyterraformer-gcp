
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class BigqueryOptionsItem():
        use_partitioned_tables:bool
        # non-optional-blocks
        
# wrapper list class
class BigqueryOptions(BlockList):
        items: List[BigqueryOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExclusionsItem():
        filter:str
        name:str
        # non-optional-blocks
        description: Optional[str] = None
        disabled: Optional[bool] = None
        
# wrapper list class
class Exclusions(BlockList):
        items: List[ExclusionsItem]




class GoogleLoggingProjectSink(ResourceObject):
    """    
    Args:
        destination (str): The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource.
        name (str): The name of the logging sink.
    """
    _type = 'google_logging_project_sink'
    
    def __init__(self,
        tf_id: str,
        destination:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        unique_writer_identity: Optional[bool] = None,
        bigquery_options: Optional[BigqueryOptions]=None,
        exclusions: Optional[Exclusions]=None,
        ):
            kwargs = {}
            if destination is not None:
                kwargs['destination'] = destination
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if unique_writer_identity is not None:
                kwargs['unique_writer_identity'] = unique_writer_identity
            if bigquery_options is not None:
                kwargs['bigquery_options'] = bigquery_options
            if exclusions is not None:
                kwargs['exclusions'] = exclusions
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
