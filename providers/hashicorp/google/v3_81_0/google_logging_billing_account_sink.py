
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




class GoogleLoggingBillingAccountSink(ResourceObject):
    """    
    Args:
        billing_account (str): The billing account exported to the sink.
        destination (str): The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource.
        name (str): The name of the logging sink.
    """
    _type = 'google_logging_billing_account_sink'
    
    def __init__(self,
        tf_id: str,
        billing_account:str,
        destination:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        bigquery_options: Optional[BigqueryOptions]=None,
        exclusions: Optional[Exclusions]=None,
        ):
            kwargs = {}
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
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
            if bigquery_options is not None:
                kwargs['bigquery_options'] = bigquery_options
            if exclusions is not None:
                kwargs['exclusions'] = exclusions
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
