
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SnapshotEncryptionKeyItem():
        # non-optional-blocks
        kms_key_self_link: Optional[str] = None
        kms_key_service_account: Optional[str] = None
        raw_key: Optional[str] = None
        
# wrapper list class
class SnapshotEncryptionKey(BlockList):
        items: List[SnapshotEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceDiskEncryptionKeyItem():
        # non-optional-blocks
        kms_key_service_account: Optional[str] = None
        raw_key: Optional[str] = None
        
# wrapper list class
class SourceDiskEncryptionKey(BlockList):
        items: List[SourceDiskEncryptionKeyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeSnapshot(ResourceObject):
    """    
    Args:
        name (str): Name of the resource; provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
        source_disk (str): A reference to the disk used to create this snapshot.
    """
    _type = 'google_compute_snapshot'
    
    def __init__(self,
        tf_id: str,
        name:str,
        source_disk:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        storage_locations: Optional[List[str]] = None,
        zone: Optional[str] = None,
        snapshot_encryption_key: Optional[SnapshotEncryptionKey]=None,
        source_disk_encryption_key: Optional[SourceDiskEncryptionKey]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if source_disk is not None:
                kwargs['source_disk'] = source_disk
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if storage_locations is not None:
                kwargs['storage_locations'] = storage_locations
            if zone is not None:
                kwargs['zone'] = zone
            if snapshot_encryption_key is not None:
                kwargs['snapshot_encryption_key'] = snapshot_encryption_key
            if source_disk_encryption_key is not None:
                kwargs['source_disk_encryption_key'] = source_disk_encryption_key
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
