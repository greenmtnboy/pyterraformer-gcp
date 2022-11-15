
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConsumerAcceptListsItem():
        connection_limit:float
        project_id_or_num:str
        # non-optional-blocks
        
# wrapper list class
class ConsumerAcceptLists(BlockList):
        items: List[ConsumerAcceptListsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeServiceAttachment(ResourceObject):
    """    
    Args:
        connection_preference (str): The connection preference to use for this service attachment. Valid
                    values include "ACCEPT_AUTOMATIC", "ACCEPT_MANUAL".
        enable_proxy_protocol (bool): If true, enable the proxy protocol which is for supplying client TCP/IP
                    address data in TCP connections that traverse proxies on their way to
                    destination servers.
        name (str): Name of the resource. The name must be 1-63 characters long, and
                    comply with RFC1035. Specifically, the name must be 1-63 characters
                    long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?'
                    which means the first character must be a lowercase letter, and all
                    following characters must be a dash, lowercase letter, or digit,
                    except the last character, which cannot be a dash.
        nat_subnets (List[str]): An array of subnets that is provided for NAT in this service attachment.
        target_service (str): The URL of a forwarding rule that represents the service identified by
                    this service attachment.
    """
    _type = 'google_compute_service_attachment'
    
    def __init__(self,
        tf_id: str,
        connection_preference:str,
        enable_proxy_protocol:bool,
        name:str,
        nat_subnets:List[str],
        target_service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        consumer_reject_lists: Optional[List[str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        consumer_accept_lists: Optional[ConsumerAcceptLists]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if connection_preference is not None:
                kwargs['connection_preference'] = connection_preference
            if enable_proxy_protocol is not None:
                kwargs['enable_proxy_protocol'] = enable_proxy_protocol
            if name is not None:
                kwargs['name'] = name
            if nat_subnets is not None:
                kwargs['nat_subnets'] = nat_subnets
            if target_service is not None:
                kwargs['target_service'] = target_service
            if consumer_reject_lists is not None:
                kwargs['consumer_reject_lists'] = consumer_reject_lists
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if consumer_accept_lists is not None:
                kwargs['consumer_accept_lists'] = consumer_accept_lists
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
