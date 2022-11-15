
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AcceleratorConfigItem():
        core_count:float
        type:str
        # non-optional-blocks
        
# wrapper list class
class AcceleratorConfig(BlockList):
        items: List[AcceleratorConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContainerImageItem():
        repository:str
        # non-optional-blocks
        tag: Optional[str] = None
        
# wrapper list class
class ContainerImage(BlockList):
        items: List[ContainerImageItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VmImageItem():
        project:str
        # non-optional-blocks
        image_family: Optional[str] = None
        image_name: Optional[str] = None
        
# wrapper list class
class VmImage(BlockList):
        items: List[VmImageItem]




class GoogleNotebooksInstance(ResourceObject):
    """    
    Args:
        location (str): A reference to the zone where the machine resides.
        machine_type (str): A reference to a machine type which defines VM kind.
        name (str): The name specified for the Notebook instance.
    """
    _type = 'google_notebooks_instance'
    
    def __init__(self,
        tf_id: str,
        location:str,
        machine_type:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        boot_disk_size_gb: Optional[float] = None,
        boot_disk_type: Optional[str] = None,
        create_time: Optional[str] = None,
        custom_gpu_driver_path: Optional[str] = None,
        data_disk_size_gb: Optional[float] = None,
        data_disk_type: Optional[str] = None,
        disk_encryption: Optional[str] = None,
        id: Optional[str] = None,
        install_gpu_driver: Optional[bool] = None,
        instance_owners: Optional[List[str]] = None,
        kms_key: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        network: Optional[str] = None,
        no_proxy_access: Optional[bool] = None,
        no_public_ip: Optional[bool] = None,
        no_remove_data_disk: Optional[bool] = None,
        post_startup_script: Optional[str] = None,
        project: Optional[str] = None,
        service_account: Optional[str] = None,
        subnet: Optional[str] = None,
        update_time: Optional[str] = None,
        accelerator_config: Optional[AcceleratorConfig]=None,
        container_image: Optional[ContainerImage]=None,
        timeouts: Optional[Timeouts]=None,
        vm_image: Optional[VmImage]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if machine_type is not None:
                kwargs['machine_type'] = machine_type
            if name is not None:
                kwargs['name'] = name
            if boot_disk_size_gb is not None:
                kwargs['boot_disk_size_gb'] = boot_disk_size_gb
            if boot_disk_type is not None:
                kwargs['boot_disk_type'] = boot_disk_type
            if create_time is not None:
                kwargs['create_time'] = create_time
            if custom_gpu_driver_path is not None:
                kwargs['custom_gpu_driver_path'] = custom_gpu_driver_path
            if data_disk_size_gb is not None:
                kwargs['data_disk_size_gb'] = data_disk_size_gb
            if data_disk_type is not None:
                kwargs['data_disk_type'] = data_disk_type
            if disk_encryption is not None:
                kwargs['disk_encryption'] = disk_encryption
            if id is not None:
                kwargs['id'] = id
            if install_gpu_driver is not None:
                kwargs['install_gpu_driver'] = install_gpu_driver
            if instance_owners is not None:
                kwargs['instance_owners'] = instance_owners
            if kms_key is not None:
                kwargs['kms_key'] = kms_key
            if labels is not None:
                kwargs['labels'] = labels
            if metadata is not None:
                kwargs['metadata'] = metadata
            if network is not None:
                kwargs['network'] = network
            if no_proxy_access is not None:
                kwargs['no_proxy_access'] = no_proxy_access
            if no_public_ip is not None:
                kwargs['no_public_ip'] = no_public_ip
            if no_remove_data_disk is not None:
                kwargs['no_remove_data_disk'] = no_remove_data_disk
            if post_startup_script is not None:
                kwargs['post_startup_script'] = post_startup_script
            if project is not None:
                kwargs['project'] = project
            if service_account is not None:
                kwargs['service_account'] = service_account
            if subnet is not None:
                kwargs['subnet'] = subnet
            if update_time is not None:
                kwargs['update_time'] = update_time
            if accelerator_config is not None:
                kwargs['accelerator_config'] = accelerator_config
            if container_image is not None:
                kwargs['container_image'] = container_image
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if vm_image is not None:
                kwargs['vm_image'] = vm_image
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
