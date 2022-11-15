
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class RequestHeadersToAddItem():
        header_name:str
        header_value:str
        replace:bool
        # non-optional-blocks
        
# wrapper list class
class RequestHeadersToAdd(BlockList):
        items: List[RequestHeadersToAddItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResponseHeadersToAddItem():
        header_name:str
        header_value:str
        replace:bool
        # non-optional-blocks
        
# wrapper list class
class ResponseHeadersToAdd(BlockList):
        items: List[ResponseHeadersToAddItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HeaderActionItem():
        # non-optional-blocks
        request_headers_to_remove: Optional[List[str]] = None
        response_headers_to_remove: Optional[List[str]] = None
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        
# wrapper list class
class HeaderAction(BlockList):
        items: List[HeaderActionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PerTryTimeoutItem():
        seconds:str
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class PerTryTimeout(BlockList):
        items: List[PerTryTimeoutItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FixedDelayItem():
        seconds:str
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class FixedDelay(BlockList):
        items: List[FixedDelayItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AbortItem():
        http_status:float
        percentage:float
        # non-optional-blocks
        
# wrapper list class
class Abort(BlockList):
        items: List[AbortItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DelayItem():
        percentage:float
        # non-optional-blocks
        fixed_delay: Optional[FixedDelay]=None,
        
# wrapper list class
class Delay(BlockList):
        items: List[DelayItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CorsPolicyItem():
        disabled:bool
        # non-optional-blocks
        allow_credentials: Optional[bool] = None
        allow_headers: Optional[List[str]] = None
        allow_methods: Optional[List[str]] = None
        allow_origin_regexes: Optional[List[str]] = None
        allow_origins: Optional[List[str]] = None
        expose_headers: Optional[List[str]] = None
        max_age: Optional[float] = None
        
# wrapper list class
class CorsPolicy(BlockList):
        items: List[CorsPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FaultInjectionPolicyItem():
        # non-optional-blocks
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        
# wrapper list class
class FaultInjectionPolicy(BlockList):
        items: List[FaultInjectionPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RequestMirrorPolicyItem():
        backend_service:str
        # non-optional-blocks
        
# wrapper list class
class RequestMirrorPolicy(BlockList):
        items: List[RequestMirrorPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RetryPolicyItem():
        # non-optional-blocks
        num_retries: Optional[float] = None
        retry_conditions: Optional[List[str]] = None
        per_try_timeout: Optional[PerTryTimeout]=None,
        
# wrapper list class
class RetryPolicy(BlockList):
        items: List[RetryPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimeoutItem():
        seconds:str
        # non-optional-blocks
        nanos: Optional[float] = None
        
# wrapper list class
class Timeout(BlockList):
        items: List[TimeoutItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UrlRewriteItem():
        # non-optional-blocks
        host_rewrite: Optional[str] = None
        path_prefix_rewrite: Optional[str] = None
        
# wrapper list class
class UrlRewrite(BlockList):
        items: List[UrlRewriteItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WeightedBackendServicesItem():
        backend_service:str
        weight:float
        # non-optional-blocks
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        
# wrapper list class
class WeightedBackendServices(BlockList):
        items: List[WeightedBackendServicesItem]




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
class RangeMatchItem():
        range_end:float
        range_start:float
        # non-optional-blocks
        
# wrapper list class
class RangeMatch(BlockList):
        items: List[RangeMatchItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HeaderMatchesItem():
        header_name:str
        # non-optional-blocks
        exact_match: Optional[str] = None
        invert_match: Optional[bool] = None
        prefix_match: Optional[str] = None
        present_match: Optional[bool] = None
        regex_match: Optional[str] = None
        suffix_match: Optional[str] = None
        range_match: Optional[RangeMatch]=None,
        
# wrapper list class
class HeaderMatches(BlockList):
        items: List[HeaderMatchesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MetadataFiltersItem():
        filter_match_criteria:str
        # non-optional-blocks
        filter_labels: Optional[FilterLabels]=None,
        
# wrapper list class
class MetadataFilters(BlockList):
        items: List[MetadataFiltersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class QueryParameterMatchesItem():
        name:str
        # non-optional-blocks
        exact_match: Optional[str] = None
        present_match: Optional[bool] = None
        regex_match: Optional[str] = None
        
# wrapper list class
class QueryParameterMatches(BlockList):
        items: List[QueryParameterMatchesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MatchRulesItem():
        # non-optional-blocks
        full_path_match: Optional[str] = None
        ignore_case: Optional[bool] = None
        prefix_match: Optional[str] = None
        regex_match: Optional[str] = None
        filter_labels: Optional[FilterLabels]=None,
        range_match: Optional[RangeMatch]=None,
        header_matches: Optional[HeaderMatches]=None,
        metadata_filters: Optional[MetadataFilters]=None,
        query_parameter_matches: Optional[QueryParameterMatches]=None,
        
# wrapper list class
class MatchRules(BlockList):
        items: List[MatchRulesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RouteActionItem():
        # non-optional-blocks
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        per_try_timeout: Optional[PerTryTimeout]=None,
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        cors_policy: Optional[CorsPolicy]=None,
        fault_injection_policy: Optional[FaultInjectionPolicy]=None,
        request_mirror_policy: Optional[RequestMirrorPolicy]=None,
        retry_policy: Optional[RetryPolicy]=None,
        timeout: Optional[Timeout]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        weighted_backend_services: Optional[WeightedBackendServices]=None,
        
# wrapper list class
class RouteAction(BlockList):
        items: List[RouteActionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UrlRedirectItem():
        strip_query:bool
        # non-optional-blocks
        host_redirect: Optional[str] = None
        https_redirect: Optional[bool] = None
        path_redirect: Optional[str] = None
        prefix_redirect: Optional[str] = None
        redirect_response_code: Optional[str] = None
        
# wrapper list class
class UrlRedirect(BlockList):
        items: List[UrlRedirectItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultUrlRedirectItem():
        strip_query:bool
        # non-optional-blocks
        host_redirect: Optional[str] = None
        https_redirect: Optional[bool] = None
        path_redirect: Optional[str] = None
        prefix_redirect: Optional[str] = None
        redirect_response_code: Optional[str] = None
        
# wrapper list class
class DefaultUrlRedirect(BlockList):
        items: List[DefaultUrlRedirectItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PathRuleItem():
        paths:Set[str]
        # non-optional-blocks
        service: Optional[str] = None
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        per_try_timeout: Optional[PerTryTimeout]=None,
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        cors_policy: Optional[CorsPolicy]=None,
        fault_injection_policy: Optional[FaultInjectionPolicy]=None,
        request_mirror_policy: Optional[RequestMirrorPolicy]=None,
        retry_policy: Optional[RetryPolicy]=None,
        timeout: Optional[Timeout]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        weighted_backend_services: Optional[WeightedBackendServices]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        
# wrapper list class
class PathRule(BlockList):
        items: List[PathRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RouteRulesItem():
        priority:float
        # non-optional-blocks
        service: Optional[str] = None
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        per_try_timeout: Optional[PerTryTimeout]=None,
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        cors_policy: Optional[CorsPolicy]=None,
        fault_injection_policy: Optional[FaultInjectionPolicy]=None,
        request_mirror_policy: Optional[RequestMirrorPolicy]=None,
        retry_policy: Optional[RetryPolicy]=None,
        timeout: Optional[Timeout]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        weighted_backend_services: Optional[WeightedBackendServices]=None,
        filter_labels: Optional[FilterLabels]=None,
        range_match: Optional[RangeMatch]=None,
        header_matches: Optional[HeaderMatches]=None,
        metadata_filters: Optional[MetadataFilters]=None,
        query_parameter_matches: Optional[QueryParameterMatches]=None,
        match_rules: Optional[MatchRules]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        
# wrapper list class
class RouteRules(BlockList):
        items: List[RouteRulesItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class HostRuleItem():
        hosts:Set[str]
        path_matcher:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class HostRule(BlockSet):
        items: Set[HostRuleItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class PathMatcherItem():
        default_service:str
        name:str
        # non-optional-blocks
        description: Optional[str] = None
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        per_try_timeout: Optional[PerTryTimeout]=None,
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        cors_policy: Optional[CorsPolicy]=None,
        fault_injection_policy: Optional[FaultInjectionPolicy]=None,
        request_mirror_policy: Optional[RequestMirrorPolicy]=None,
        retry_policy: Optional[RetryPolicy]=None,
        timeout: Optional[Timeout]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        weighted_backend_services: Optional[WeightedBackendServices]=None,
        filter_labels: Optional[FilterLabels]=None,
        range_match: Optional[RangeMatch]=None,
        header_matches: Optional[HeaderMatches]=None,
        metadata_filters: Optional[MetadataFilters]=None,
        query_parameter_matches: Optional[QueryParameterMatches]=None,
        match_rules: Optional[MatchRules]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        default_url_redirect: Optional[DefaultUrlRedirect]=None,
        path_rule: Optional[PathRule]=None,
        route_rules: Optional[RouteRules]=None,
        
# wrapper list class
class PathMatcher(BlockList):
        items: List[PathMatcherItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TestItem():
        host:str
        path:str
        service:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class Test(BlockList):
        items: List[TestItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeRegionUrlMap(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_region_url_map'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        default_service: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        request_headers_to_add: Optional[RequestHeadersToAdd]=None,
        response_headers_to_add: Optional[ResponseHeadersToAdd]=None,
        header_action: Optional[HeaderAction]=None,
        per_try_timeout: Optional[PerTryTimeout]=None,
        fixed_delay: Optional[FixedDelay]=None,
        abort: Optional[Abort]=None,
        delay: Optional[Delay]=None,
        cors_policy: Optional[CorsPolicy]=None,
        fault_injection_policy: Optional[FaultInjectionPolicy]=None,
        request_mirror_policy: Optional[RequestMirrorPolicy]=None,
        retry_policy: Optional[RetryPolicy]=None,
        timeout: Optional[Timeout]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        weighted_backend_services: Optional[WeightedBackendServices]=None,
        filter_labels: Optional[FilterLabels]=None,
        range_match: Optional[RangeMatch]=None,
        header_matches: Optional[HeaderMatches]=None,
        metadata_filters: Optional[MetadataFilters]=None,
        query_parameter_matches: Optional[QueryParameterMatches]=None,
        match_rules: Optional[MatchRules]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        default_url_redirect: Optional[DefaultUrlRedirect]=None,
        path_rule: Optional[PathRule]=None,
        route_rules: Optional[RouteRules]=None,
        host_rule: Optional[HostRule]=None,
        path_matcher: Optional[PathMatcher]=None,
        test: Optional[Test]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if default_service is not None:
                kwargs['default_service'] = default_service
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if request_headers_to_add is not None:
                kwargs['request_headers_to_add'] = request_headers_to_add
            if response_headers_to_add is not None:
                kwargs['response_headers_to_add'] = response_headers_to_add
            if header_action is not None:
                kwargs['header_action'] = header_action
            if per_try_timeout is not None:
                kwargs['per_try_timeout'] = per_try_timeout
            if fixed_delay is not None:
                kwargs['fixed_delay'] = fixed_delay
            if abort is not None:
                kwargs['abort'] = abort
            if delay is not None:
                kwargs['delay'] = delay
            if cors_policy is not None:
                kwargs['cors_policy'] = cors_policy
            if fault_injection_policy is not None:
                kwargs['fault_injection_policy'] = fault_injection_policy
            if request_mirror_policy is not None:
                kwargs['request_mirror_policy'] = request_mirror_policy
            if retry_policy is not None:
                kwargs['retry_policy'] = retry_policy
            if timeout is not None:
                kwargs['timeout'] = timeout
            if url_rewrite is not None:
                kwargs['url_rewrite'] = url_rewrite
            if weighted_backend_services is not None:
                kwargs['weighted_backend_services'] = weighted_backend_services
            if filter_labels is not None:
                kwargs['filter_labels'] = filter_labels
            if range_match is not None:
                kwargs['range_match'] = range_match
            if header_matches is not None:
                kwargs['header_matches'] = header_matches
            if metadata_filters is not None:
                kwargs['metadata_filters'] = metadata_filters
            if query_parameter_matches is not None:
                kwargs['query_parameter_matches'] = query_parameter_matches
            if match_rules is not None:
                kwargs['match_rules'] = match_rules
            if route_action is not None:
                kwargs['route_action'] = route_action
            if url_redirect is not None:
                kwargs['url_redirect'] = url_redirect
            if default_url_redirect is not None:
                kwargs['default_url_redirect'] = default_url_redirect
            if path_rule is not None:
                kwargs['path_rule'] = path_rule
            if route_rules is not None:
                kwargs['route_rules'] = route_rules
            if host_rule is not None:
                kwargs['host_rule'] = host_rule
            if path_matcher is not None:
                kwargs['path_matcher'] = path_matcher
            if test is not None:
                kwargs['test'] = test
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
