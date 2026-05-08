from typing import Callable

#If a test is not present in the policy we consider it as satisfied but we return an empty list of matched conditions

def test_subject_role(policy : dict, subject : dict, **ignored_args) -> tuple[bool, list[str]]:
    
    try :
        policy_role : str = policy["subject"]["role"]
    except KeyError:
        return (True, [])
    
    if policy_role == subject["role"]:
        return (True, [f"subject.role={policy_role}"])
    
    return (False, [])

def test_subject_clearance_min(policy : dict, subject : dict, **ignored_args) -> tuple[bool, list[str]]:
    
    try :
        policy_clearance_min : int = policy["subject"]["clearance_min"]
    except KeyError:
        return (True, [])
    
    if subject["clearance"] >= policy_clearance_min:
        return (True, [f"subject.clearance>={policy_clearance_min}"])
    
    return (False, [])

def test_resource_ownership(policy : dict, subject_id: str, resource: dict, **ignored_args) -> tuple[bool, list[str]]:
    
    try : 
        policy_resource_ownership : bool = policy["resource"]["owner_is_subject"]
    except KeyError:
        return (True, [])
    
    if (subject_id == resource["owner"]) and policy_resource_ownership:
        return (True, [f"owner_is_subject={policy_resource_ownership}"])
    
    return (False, [])

def test_resource_type(policy : dict, resource: dict, **ignored_args) -> tuple[bool, list[str]]:
    try : 
        policy_resource_type : str = policy["resource"]["type"]
    except KeyError:
        return (True, [])
    
    if resource["type"] == policy_resource_type:
        return (True, [f"resource.type={policy_resource_type}"])
    
    return (False, [])

def test_resource_classification(policy : dict, resource: dict, **ignored_args) -> tuple[bool, list[str]]:
    try : 
        policy_resource_classification : str = policy["resource"]["classification"]
    except KeyError:
        return (True, [])
    
    if resource["classification"] == policy_resource_classification:
        return (True, [f"resource.classification={policy_resource_classification}"])
    
    return (False, [])

def test_action(policy : dict, request : dict, **ignored_args) -> tuple[bool, list[str]]:
    try : 
        policy_action: list = policy["action"]
    except KeyError:
        return (True, [])
    
    if request["action"] in policy_action:
        return (True, [f"action={request["action"]}"])
    
    return (False, [])

def test_context_mfa(policy : dict, request : dict, **ignored_args) -> tuple[bool, list[str]]:
    
    try : 
        policy_context_mfa_required: bool = policy["context"]["mfa_required"]
    except KeyError:
        return (True, [])
    
    if request["context"]["mfa"] == policy_context_mfa_required:
        return (True, [f"context.mfa={policy_context_mfa_required}"])
    
    return (False, [])

def test_context_time_interval(policy : dict, request : dict, **ignored_args) -> tuple[bool, list[str]]:
    try : #here its assumed that there must be both a min and max hour as only one is meaningless
        policy_context_hour_min: bool = policy["context"]["hour_min"]
        policy_context_hour_max: bool = policy["context"]["hour_max"]
    except KeyError:
        return (True, [])
    
    if request["context"]["hour"] >= policy_context_hour_min and request["context"]["hour"] <= policy_context_hour_max:
        return (True, [f"{policy_context_hour_min}<=hour<={policy_context_hour_max}"])
    
    return (False, [])

TEST_LIST : list[Callable] = [
    test_subject_role,
    test_subject_clearance_min,
    test_resource_ownership,
    test_resource_type,
    test_resource_classification,
    test_action,
    test_context_mfa,
    test_context_time_interval
]