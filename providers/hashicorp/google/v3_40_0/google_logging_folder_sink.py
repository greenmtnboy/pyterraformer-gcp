
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




class GoogleLoggingFolderSink(ResourceObject):
    """    
    Args:
        destination (str): The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource.
        folder (str): The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is accepted.
        name (str): The name of the logging sink.
    """
    _type = 'google_logging_folder_sink'
    
    def __init__(self,
        tf_id: str,
        destination:str,
        folder:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        include_children: Optional[bool] = None,
        bigquery_options: Optional[BigqueryOptions]=None,
        ):
            kwargs = {}
            if destination is not None:
                kwargs['destination'] = destination
            if folder is not None:
                kwargs['folder'] = folder
            if name is not None:
                kwargs['name'] = name
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if include_children is not None:
                kwargs['include_children'] = include_children
            if bigquery_options is not None:
                kwargs['bigquery_options'] = bigquery_options
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
