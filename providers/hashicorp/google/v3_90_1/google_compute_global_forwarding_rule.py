
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FilterLabelsItem():
        name:str
        value:str
        # non-optional-blocks
        
# wrapper list class
class FilterLabels(BlockList):
        items: List[FilterLabelsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MetadataFiltersItem():
        filter_match_criteria:str
        # non-optional-blocks
        filter_labels: Optional[FilterLabels]=None,
        
# wrapper list class
class MetadataFilters(BlockList):
        items: List[MetadataFiltersItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeGlobalForwardingRule(ResourceObject):
    """    
    Args:
        name (str): Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        target (str): The URL of the target resource to receive the matched traffic. For regional forwarding rules, this target must live in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource. The forwarded traffic must be of a type appropriate to the target object. For `INTERNAL_SELF_MANAGED` load balancing, only `targetHttpProxy` is valid, not `targetHttpsProxy`.
    """
    _type = 'google_compute_global_forwarding_rule'
    
    def __init__(self,
        tf_id: str,
        name:str,
        target:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ip_address: Optional[str] = None,
        ip_protocol: Optional[str] = None,
        ip_version: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        load_balancing_scheme: Optional[str] = None,
        network: Optional[str] = None,
        port_range: Optional[str] = None,
        project: Optional[str] = None,
        filter_labels: Optional[FilterLabels]=None,
        metadata_filters: Optional[MetadataFilters]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if target is not None:
                kwargs['target'] = target
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if ip_protocol is not None:
                kwargs['ip_protocol'] = ip_protocol
            if ip_version is not None:
                kwargs['ip_version'] = ip_version
            if labels is not None:
                kwargs['labels'] = labels
            if load_balancing_scheme is not None:
                kwargs['load_balancing_scheme'] = load_balancing_scheme
            if network is not None:
                kwargs['network'] = network
            if port_range is not None:
                kwargs['port_range'] = port_range
            if project is not None:
                kwargs['project'] = project
            if filter_labels is not None:
                kwargs['filter_labels'] = filter_labels
            if metadata_filters is not None:
                kwargs['metadata_filters'] = metadata_filters
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
