
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DisruptionBudgetItem():
        # non-optional-blocks
        fixed: Optional[float] = None
        percent: Optional[float] = None
        
# wrapper list class
class DisruptionBudget(BlockList):
        items: List[DisruptionBudgetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AptItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Apt(BlockList):
        items: List[AptItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GooItem():
        name:str
        url:str
        # non-optional-blocks
        
# wrapper list class
class Goo(BlockList):
        items: List[GooItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class YumItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Yum(BlockList):
        items: List[YumItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ZypperItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Zypper(BlockList):
        items: List[ZypperItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GcsItem():
        bucket:str
        object:str
        # non-optional-blocks
        generation: Optional[float] = None
        
# wrapper list class
class Gcs(BlockList):
        items: List[GcsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RemoteItem():
        uri:str
        # non-optional-blocks
        sha256_checksum: Optional[str] = None
        
# wrapper list class
class Remote(BlockList):
        items: List[RemoteItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceItem():
        # non-optional-blocks
        allow_insecure: Optional[bool] = None
        local_path: Optional[str] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        
# wrapper list class
class Source(BlockList):
        items: List[SourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DebItem():
        # non-optional-blocks
        pull_deps: Optional[bool] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        
# wrapper list class
class Deb(BlockList):
        items: List[DebItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GoogetItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Googet(BlockList):
        items: List[GoogetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MsiItem():
        # non-optional-blocks
        properties: Optional[List[str]] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        
# wrapper list class
class Msi(BlockList):
        items: List[MsiItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RpmItem():
        # non-optional-blocks
        pull_deps: Optional[bool] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        
# wrapper list class
class Rpm(BlockList):
        items: List[RpmItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FileItem():
        path:str
        state:str
        # non-optional-blocks
        content: Optional[str] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        file: Optional[File]=None,
        
# wrapper list class
class File(BlockList):
        items: List[FileItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EnforceItem():
        interpreter:str
        # non-optional-blocks
        args: Optional[List[str]] = None
        output_file_path: Optional[str] = None
        script: Optional[str] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        file: Optional[File]=None,
        
# wrapper list class
class Enforce(BlockList):
        items: List[EnforceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ValidateItem():
        interpreter:str
        # non-optional-blocks
        args: Optional[List[str]] = None
        output_file_path: Optional[str] = None
        script: Optional[str] = None
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        file: Optional[File]=None,
        
# wrapper list class
class Validate(BlockList):
        items: List[ValidateItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExecItem():
        # non-optional-blocks
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        file: Optional[File]=None,
        enforce: Optional[Enforce]=None,
        validate: Optional[Validate]=None,
        
# wrapper list class
class Exec(BlockList):
        items: List[ExecItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PkgItem():
        desired_state:str
        # non-optional-blocks
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        apt: Optional[Apt]=None,
        deb: Optional[Deb]=None,
        googet: Optional[Googet]=None,
        msi: Optional[Msi]=None,
        rpm: Optional[Rpm]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        
# wrapper list class
class Pkg(BlockList):
        items: List[PkgItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RepositoryItem():
        # non-optional-blocks
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        
# wrapper list class
class Repository(BlockList):
        items: List[RepositoryItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InventoryFiltersItem():
        os_short_name:str
        # non-optional-blocks
        os_version: Optional[str] = None
        
# wrapper list class
class InventoryFilters(BlockList):
        items: List[InventoryFiltersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourcesItem():
        id:str
        # non-optional-blocks
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        deb: Optional[Deb]=None,
        googet: Optional[Googet]=None,
        msi: Optional[Msi]=None,
        rpm: Optional[Rpm]=None,
        file: Optional[File]=None,
        enforce: Optional[Enforce]=None,
        validate: Optional[Validate]=None,
        exec: Optional[Exec]=None,
        pkg: Optional[Pkg]=None,
        repository: Optional[Repository]=None,
        
# wrapper list class
class Resources(BlockList):
        items: List[ResourcesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResourceGroupsItem():
        # non-optional-blocks
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        deb: Optional[Deb]=None,
        googet: Optional[Googet]=None,
        msi: Optional[Msi]=None,
        rpm: Optional[Rpm]=None,
        file: Optional[File]=None,
        enforce: Optional[Enforce]=None,
        validate: Optional[Validate]=None,
        exec: Optional[Exec]=None,
        pkg: Optional[Pkg]=None,
        repository: Optional[Repository]=None,
        inventory_filters: Optional[InventoryFilters]=None,
        resources: Optional[Resources]=None,
        
# wrapper list class
class ResourceGroups(BlockList):
        items: List[ResourceGroupsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExclusionLabelsItem():
        # non-optional-blocks
        labels: Optional[Dict[str, str]] = None
        
# wrapper list class
class ExclusionLabels(BlockList):
        items: List[ExclusionLabelsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InclusionLabelsItem():
        # non-optional-blocks
        labels: Optional[Dict[str, str]] = None
        
# wrapper list class
class InclusionLabels(BlockList):
        items: List[InclusionLabelsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InventoriesItem():
        os_short_name:str
        # non-optional-blocks
        os_version: Optional[str] = None
        
# wrapper list class
class Inventories(BlockList):
        items: List[InventoriesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InstanceFilterItem():
        # non-optional-blocks
        all: Optional[bool] = None
        exclusion_labels: Optional[ExclusionLabels]=None,
        inclusion_labels: Optional[InclusionLabels]=None,
        inventories: Optional[Inventories]=None,
        
# wrapper list class
class InstanceFilter(BlockList):
        items: List[InstanceFilterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OsPoliciesItem():
        id:str
        mode:str
        # non-optional-blocks
        allow_no_resource_group_match: Optional[bool] = None
        description: Optional[str] = None
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        deb: Optional[Deb]=None,
        googet: Optional[Googet]=None,
        msi: Optional[Msi]=None,
        rpm: Optional[Rpm]=None,
        file: Optional[File]=None,
        enforce: Optional[Enforce]=None,
        validate: Optional[Validate]=None,
        exec: Optional[Exec]=None,
        pkg: Optional[Pkg]=None,
        repository: Optional[Repository]=None,
        inventory_filters: Optional[InventoryFilters]=None,
        resources: Optional[Resources]=None,
        resource_groups: Optional[ResourceGroups]=None,
        
# wrapper list class
class OsPolicies(BlockList):
        items: List[OsPoliciesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RolloutItem():
        min_wait_duration:str
        # non-optional-blocks
        disruption_budget: Optional[DisruptionBudget]=None,
        
# wrapper list class
class Rollout(BlockList):
        items: List[RolloutItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleOsConfigOsPolicyAssignment(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): Resource name.
    """
    _type = 'google_os_config_os_policy_assignment'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        disruption_budget: Optional[DisruptionBudget]=None,
        apt: Optional[Apt]=None,
        goo: Optional[Goo]=None,
        yum: Optional[Yum]=None,
        zypper: Optional[Zypper]=None,
        gcs: Optional[Gcs]=None,
        remote: Optional[Remote]=None,
        source: Optional[Source]=None,
        deb: Optional[Deb]=None,
        googet: Optional[Googet]=None,
        msi: Optional[Msi]=None,
        rpm: Optional[Rpm]=None,
        file: Optional[File]=None,
        enforce: Optional[Enforce]=None,
        validate: Optional[Validate]=None,
        exec: Optional[Exec]=None,
        pkg: Optional[Pkg]=None,
        repository: Optional[Repository]=None,
        inventory_filters: Optional[InventoryFilters]=None,
        resources: Optional[Resources]=None,
        resource_groups: Optional[ResourceGroups]=None,
        exclusion_labels: Optional[ExclusionLabels]=None,
        inclusion_labels: Optional[InclusionLabels]=None,
        inventories: Optional[Inventories]=None,
        instance_filter: Optional[InstanceFilter]=None,
        os_policies: Optional[OsPolicies]=None,
        rollout: Optional[Rollout]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if disruption_budget is not None:
                kwargs['disruption_budget'] = disruption_budget
            if apt is not None:
                kwargs['apt'] = apt
            if goo is not None:
                kwargs['goo'] = goo
            if yum is not None:
                kwargs['yum'] = yum
            if zypper is not None:
                kwargs['zypper'] = zypper
            if gcs is not None:
                kwargs['gcs'] = gcs
            if remote is not None:
                kwargs['remote'] = remote
            if source is not None:
                kwargs['source'] = source
            if deb is not None:
                kwargs['deb'] = deb
            if googet is not None:
                kwargs['googet'] = googet
            if msi is not None:
                kwargs['msi'] = msi
            if rpm is not None:
                kwargs['rpm'] = rpm
            if file is not None:
                kwargs['file'] = file
            if enforce is not None:
                kwargs['enforce'] = enforce
            if validate is not None:
                kwargs['validate'] = validate
            if exec is not None:
                kwargs['exec'] = exec
            if pkg is not None:
                kwargs['pkg'] = pkg
            if repository is not None:
                kwargs['repository'] = repository
            if inventory_filters is not None:
                kwargs['inventory_filters'] = inventory_filters
            if resources is not None:
                kwargs['resources'] = resources
            if resource_groups is not None:
                kwargs['resource_groups'] = resource_groups
            if exclusion_labels is not None:
                kwargs['exclusion_labels'] = exclusion_labels
            if inclusion_labels is not None:
                kwargs['inclusion_labels'] = inclusion_labels
            if inventories is not None:
                kwargs['inventories'] = inventories
            if instance_filter is not None:
                kwargs['instance_filter'] = instance_filter
            if os_policies is not None:
                kwargs['os_policies'] = os_policies
            if rollout is not None:
                kwargs['rollout'] = rollout
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
