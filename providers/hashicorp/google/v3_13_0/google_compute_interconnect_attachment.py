
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




class GoogleComputeInterconnectAttachment(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is created. The
                    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
                    name must be 1-63 characters long and match the regular expression
                    '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a
                    lowercase letter, and all following characters must be a dash, lowercase
                    letter, or digit, except the last character, which cannot be a dash.
        router (str): URL of the cloud router to be used for dynamic routing. This router must be in
                    the same region as this InterconnectAttachment. The InterconnectAttachment will
                    automatically connect the Interconnect to the network & region within which the
                    Cloud Router is configured.
    """
    _type = 'google_compute_interconnect_attachment'
    
    def __init__(self,
        tf_id: str,
        name:str,
        router:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        admin_enabled: Optional[bool] = None,
        bandwidth: Optional[str] = None,
        candidate_subnets: Optional[List[str]] = None,
        description: Optional[str] = None,
        edge_availability_domain: Optional[str] = None,
        id: Optional[str] = None,
        interconnect: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        type: Optional[str] = None,
        vlan_tag8021q: Optional[float] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if router is not None:
                kwargs['router'] = router
            if admin_enabled is not None:
                kwargs['admin_enabled'] = admin_enabled
            if bandwidth is not None:
                kwargs['bandwidth'] = bandwidth
            if candidate_subnets is not None:
                kwargs['candidate_subnets'] = candidate_subnets
            if description is not None:
                kwargs['description'] = description
            if edge_availability_domain is not None:
                kwargs['edge_availability_domain'] = edge_availability_domain
            if id is not None:
                kwargs['id'] = id
            if interconnect is not None:
                kwargs['interconnect'] = interconnect
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if type is not None:
                kwargs['type'] = type
            if vlan_tag8021q is not None:
                kwargs['vlan_tag8021q'] = vlan_tag8021q
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
