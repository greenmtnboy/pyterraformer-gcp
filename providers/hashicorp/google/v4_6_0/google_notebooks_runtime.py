
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class InitializeParamsItem():
        # non-optional-blocks
        description: Optional[str] = None
        disk_name: Optional[str] = None
        disk_size_gb: Optional[float] = None
        disk_type: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        
# wrapper list class
class InitializeParams(BlockList):
        items: List[InitializeParamsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AcceleratorConfigItem():
        # non-optional-blocks
        core_count: Optional[float] = None
        type: Optional[str] = None
        
# wrapper list class
class AcceleratorConfig(BlockList):
        items: List[AcceleratorConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContainerImagesItem():
        repository:str
        # non-optional-blocks
        tag: Optional[str] = None
        
# wrapper list class
class ContainerImages(BlockList):
        items: List[ContainerImagesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DataDiskItem():
        # non-optional-blocks
        interface: Optional[str] = None
        mode: Optional[str] = None
        source: Optional[str] = None
        type: Optional[str] = None
        initialize_params: Optional[InitializeParams]=None,
        
# wrapper list class
class DataDisk(BlockList):
        items: List[DataDiskItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EncryptionConfigItem():
        # non-optional-blocks
        kms_key: Optional[str] = None
        
# wrapper list class
class EncryptionConfig(BlockList):
        items: List[EncryptionConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ShieldedInstanceConfigItem():
        # non-optional-blocks
        enable_integrity_monitoring: Optional[bool] = None
        enable_secure_boot: Optional[bool] = None
        enable_vtpm: Optional[bool] = None
        
# wrapper list class
class ShieldedInstanceConfig(BlockList):
        items: List[ShieldedInstanceConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class VirtualMachineConfigItem():
        machine_type:str
        # non-optional-blocks
        internal_ip_only: Optional[bool] = None
        labels: Optional[Dict[str, str]] = None
        metadata: Optional[Dict[str, str]] = None
        network: Optional[str] = None
        nic_type: Optional[str] = None
        subnet: Optional[str] = None
        tags: Optional[List[str]] = None
        initialize_params: Optional[InitializeParams]=None,
        accelerator_config: Optional[AcceleratorConfig]=None,
        container_images: Optional[ContainerImages]=None,
        data_disk: Optional[DataDisk]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        
# wrapper list class
class VirtualMachineConfig(BlockList):
        items: List[VirtualMachineConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AccessConfigItem():
        # non-optional-blocks
        access_type: Optional[str] = None
        runtime_owner: Optional[str] = None
        
# wrapper list class
class AccessConfig(BlockList):
        items: List[AccessConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SoftwareConfigItem():
        # non-optional-blocks
        custom_gpu_driver_path: Optional[str] = None
        enable_health_monitoring: Optional[bool] = None
        idle_shutdown: Optional[bool] = None
        idle_shutdown_timeout: Optional[float] = None
        install_gpu_driver: Optional[bool] = None
        notebook_upgrade_schedule: Optional[str] = None
        post_startup_script: Optional[str] = None
        
# wrapper list class
class SoftwareConfig(BlockList):
        items: List[SoftwareConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VirtualMachineItem():
        # non-optional-blocks
        initialize_params: Optional[InitializeParams]=None,
        accelerator_config: Optional[AcceleratorConfig]=None,
        container_images: Optional[ContainerImages]=None,
        data_disk: Optional[DataDisk]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        virtual_machine_config: Optional[VirtualMachineConfig]=None,
        
# wrapper list class
class VirtualMachine(BlockList):
        items: List[VirtualMachineItem]




class GoogleNotebooksRuntime(ResourceObject):
    """    
    Args:
        location (str): A reference to the zone where the machine resides.
        name (str): The name specified for the Notebook instance.
    """
    _type = 'google_notebooks_runtime'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        initialize_params: Optional[InitializeParams]=None,
        accelerator_config: Optional[AcceleratorConfig]=None,
        container_images: Optional[ContainerImages]=None,
        data_disk: Optional[DataDisk]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        shielded_instance_config: Optional[ShieldedInstanceConfig]=None,
        virtual_machine_config: Optional[VirtualMachineConfig]=None,
        access_config: Optional[AccessConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        timeouts: Optional[Timeouts]=None,
        virtual_machine: Optional[VirtualMachine]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if initialize_params is not None:
                kwargs['initialize_params'] = initialize_params
            if accelerator_config is not None:
                kwargs['accelerator_config'] = accelerator_config
            if container_images is not None:
                kwargs['container_images'] = container_images
            if data_disk is not None:
                kwargs['data_disk'] = data_disk
            if encryption_config is not None:
                kwargs['encryption_config'] = encryption_config
            if shielded_instance_config is not None:
                kwargs['shielded_instance_config'] = shielded_instance_config
            if virtual_machine_config is not None:
                kwargs['virtual_machine_config'] = virtual_machine_config
            if access_config is not None:
                kwargs['access_config'] = access_config
            if software_config is not None:
                kwargs['software_config'] = software_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if virtual_machine is not None:
                kwargs['virtual_machine'] = virtual_machine
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
