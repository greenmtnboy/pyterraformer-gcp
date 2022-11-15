
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PullRequestItem():
        branch:str
        # non-optional-blocks
        comment_control: Optional[str] = None
        invert_regex: Optional[bool] = None
        
# wrapper list class
class PullRequest(BlockList):
        items: List[PullRequestItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PushItem():
        # non-optional-blocks
        branch: Optional[str] = None
        invert_regex: Optional[bool] = None
        tag: Optional[str] = None
        
# wrapper list class
class Push(BlockList):
        items: List[PushItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class VolumesItem():
        # non-optional-blocks
        name: Optional[str] = None
        path: Optional[str] = None
        
# wrapper list class
class Volumes(BlockList):
        items: List[VolumesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RepoSourceItem():
        repo_name:str
        # non-optional-blocks
        branch_name: Optional[str] = None
        commit_sha: Optional[str] = None
        dir: Optional[str] = None
        invert_regex: Optional[bool] = None
        project_id: Optional[str] = None
        substitutions: Optional[Dict[str, str]] = None
        tag_name: Optional[str] = None
        
# wrapper list class
class RepoSource(BlockList):
        items: List[RepoSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StorageSourceItem():
        bucket:str
        object:str
        # non-optional-blocks
        generation: Optional[str] = None
        
# wrapper list class
class StorageSource(BlockList):
        items: List[StorageSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecretManagerItem():
        env:str
        version_name:str
        # non-optional-blocks
        
# wrapper list class
class SecretManager(BlockList):
        items: List[SecretManagerItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ObjectsItem():
        # non-optional-blocks
        location: Optional[str] = None
        paths: Optional[List[str]] = None
        
# wrapper list class
class Objects(BlockList):
        items: List[ObjectsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ArtifactsItem():
        # non-optional-blocks
        images: Optional[List[str]] = None
        objects: Optional[Objects]=None,
        
# wrapper list class
class Artifacts(BlockList):
        items: List[ArtifactsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AvailableSecretsItem():
        # non-optional-blocks
        secret_manager: Optional[SecretManager]=None,
        
# wrapper list class
class AvailableSecrets(BlockList):
        items: List[AvailableSecretsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OptionsItem():
        # non-optional-blocks
        disk_size_gb: Optional[float] = None
        dynamic_substitutions: Optional[bool] = None
        env: Optional[List[str]] = None
        log_streaming_option: Optional[str] = None
        logging: Optional[str] = None
        machine_type: Optional[str] = None
        requested_verify_option: Optional[str] = None
        secret_env: Optional[List[str]] = None
        source_provenance_hash: Optional[List[str]] = None
        substitution_option: Optional[str] = None
        worker_pool: Optional[str] = None
        volumes: Optional[Volumes]=None,
        
# wrapper list class
class Options(BlockList):
        items: List[OptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecretItem():
        kms_key_name:str
        # non-optional-blocks
        secret_env: Optional[Dict[str, str]] = None
        
# wrapper list class
class Secret(BlockList):
        items: List[SecretItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceItem():
        # non-optional-blocks
        repo_source: Optional[RepoSource]=None,
        storage_source: Optional[StorageSource]=None,
        
# wrapper list class
class Source(BlockList):
        items: List[SourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StepItem():
        name:str
        # non-optional-blocks
        args: Optional[List[str]] = None
        dir: Optional[str] = None
        entrypoint: Optional[str] = None
        env: Optional[List[str]] = None
        id: Optional[str] = None
        secret_env: Optional[List[str]] = None
        timeout: Optional[str] = None
        timing: Optional[str] = None
        wait_for: Optional[List[str]] = None
        volumes: Optional[Volumes]=None,
        
# wrapper list class
class Step(BlockList):
        items: List[StepItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BuildItem():
        # non-optional-blocks
        images: Optional[List[str]] = None
        logs_bucket: Optional[str] = None
        queue_ttl: Optional[str] = None
        substitutions: Optional[Dict[str, str]] = None
        tags: Optional[List[str]] = None
        timeout: Optional[str] = None
        volumes: Optional[Volumes]=None,
        repo_source: Optional[RepoSource]=None,
        storage_source: Optional[StorageSource]=None,
        secret_manager: Optional[SecretManager]=None,
        objects: Optional[Objects]=None,
        artifacts: Optional[Artifacts]=None,
        available_secrets: Optional[AvailableSecrets]=None,
        options: Optional[Options]=None,
        secret: Optional[Secret]=None,
        source: Optional[Source]=None,
        step: Optional[Step]=None,
        
# wrapper list class
class Build(BlockList):
        items: List[BuildItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GitFileSourceItem():
        path:str
        repo_type:str
        # non-optional-blocks
        revision: Optional[str] = None
        uri: Optional[str] = None
        
# wrapper list class
class GitFileSource(BlockList):
        items: List[GitFileSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GithubItem():
        # non-optional-blocks
        name: Optional[str] = None
        owner: Optional[str] = None
        pull_request: Optional[PullRequest]=None,
        push: Optional[Push]=None,
        
# wrapper list class
class Github(BlockList):
        items: List[GithubItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PubsubConfigItem():
        topic:str
        # non-optional-blocks
        service_account_email: Optional[str] = None
        
# wrapper list class
class PubsubConfig(BlockList):
        items: List[PubsubConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceToBuildItem():
        ref:str
        repo_type:str
        uri:str
        # non-optional-blocks
        
# wrapper list class
class SourceToBuild(BlockList):
        items: List[SourceToBuildItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TriggerTemplateItem():
        # non-optional-blocks
        branch_name: Optional[str] = None
        commit_sha: Optional[str] = None
        dir: Optional[str] = None
        invert_regex: Optional[bool] = None
        project_id: Optional[str] = None
        repo_name: Optional[str] = None
        tag_name: Optional[str] = None
        
# wrapper list class
class TriggerTemplate(BlockList):
        items: List[TriggerTemplateItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WebhookConfigItem():
        secret:str
        # non-optional-blocks
        
# wrapper list class
class WebhookConfig(BlockList):
        items: List[WebhookConfigItem]




class GoogleCloudbuildTrigger(ResourceObject):
    """    
    Args:
    """
    _type = 'google_cloudbuild_trigger'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        filename: Optional[str] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        ignored_files: Optional[List[str]] = None,
        included_files: Optional[List[str]] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        service_account: Optional[str] = None,
        substitutions: Optional[Dict[str, str]] = None,
        tags: Optional[List[str]] = None,
        pull_request: Optional[PullRequest]=None,
        push: Optional[Push]=None,
        volumes: Optional[Volumes]=None,
        repo_source: Optional[RepoSource]=None,
        storage_source: Optional[StorageSource]=None,
        secret_manager: Optional[SecretManager]=None,
        objects: Optional[Objects]=None,
        artifacts: Optional[Artifacts]=None,
        available_secrets: Optional[AvailableSecrets]=None,
        options: Optional[Options]=None,
        secret: Optional[Secret]=None,
        source: Optional[Source]=None,
        step: Optional[Step]=None,
        build: Optional[Build]=None,
        git_file_source: Optional[GitFileSource]=None,
        github: Optional[Github]=None,
        pubsub_config: Optional[PubsubConfig]=None,
        source_to_build: Optional[SourceToBuild]=None,
        timeouts: Optional[Timeouts]=None,
        trigger_template: Optional[TriggerTemplate]=None,
        webhook_config: Optional[WebhookConfig]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if filename is not None:
                kwargs['filename'] = filename
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if ignored_files is not None:
                kwargs['ignored_files'] = ignored_files
            if included_files is not None:
                kwargs['included_files'] = included_files
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if service_account is not None:
                kwargs['service_account'] = service_account
            if substitutions is not None:
                kwargs['substitutions'] = substitutions
            if tags is not None:
                kwargs['tags'] = tags
            if pull_request is not None:
                kwargs['pull_request'] = pull_request
            if push is not None:
                kwargs['push'] = push
            if volumes is not None:
                kwargs['volumes'] = volumes
            if repo_source is not None:
                kwargs['repo_source'] = repo_source
            if storage_source is not None:
                kwargs['storage_source'] = storage_source
            if secret_manager is not None:
                kwargs['secret_manager'] = secret_manager
            if objects is not None:
                kwargs['objects'] = objects
            if artifacts is not None:
                kwargs['artifacts'] = artifacts
            if available_secrets is not None:
                kwargs['available_secrets'] = available_secrets
            if options is not None:
                kwargs['options'] = options
            if secret is not None:
                kwargs['secret'] = secret
            if source is not None:
                kwargs['source'] = source
            if step is not None:
                kwargs['step'] = step
            if build is not None:
                kwargs['build'] = build
            if git_file_source is not None:
                kwargs['git_file_source'] = git_file_source
            if github is not None:
                kwargs['github'] = github
            if pubsub_config is not None:
                kwargs['pubsub_config'] = pubsub_config
            if source_to_build is not None:
                kwargs['source_to_build'] = source_to_build
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if trigger_template is not None:
                kwargs['trigger_template'] = trigger_template
            if webhook_config is not None:
                kwargs['webhook_config'] = webhook_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
