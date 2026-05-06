from typing import Any

def parse_subjects(subjects_raw : Any) -> dict[str, dict]:
    """Checks for correct formatting of the subject json file and returns a dictionary of the subjects
    Args:
        subjects_raw (Any): Subject raw data from json file
    Raises:
        ValueError: Json file wrongly formatted : expected format : {"subjects": [{"id": str, "role": str, "clearance": int},..]}
    Returns:
        dict[str, dict]: The dictionary by id of the subjects
    """    
    if not isinstance(subjects_raw, dict) : 
        raise ValueError("File wrongly formatted" + """\nexpected format : {subjects": [{"id": str, "role": str, "clearance": int},..]}""")
    parsed_subjects : dict[str, dict] = {}
    try:
        for subject in subjects_raw["subjects"]:
            subject_data = {
                "role" : subject["role"],
                "clearance" : subject["clearance"]
            }
            parsed_subjects[subject["id"]] = subject_data
    except KeyError as e: 
        raise ValueError(f"File wrongly formatted, missing key : {e}" + """\nexpected format : {subjects": [{"id": str, "role": str, "clearance": int},..]}""")
    return parsed_subjects

def parse_resources(resources_raw : Any) -> dict[str, dict]:
    """Checks for correct formatting of the resources json file and returns a dictionary of the resources
    Args:
        resources_raw (Any): Resources raw data from json file
    Raises:
        ValueError: Json file wrongly formatted : expected format : {"resources": [{"id": str,"type": str,"owner": str,"classification": str},...]}
    Returns:
        dict[str, dict]: The dictionary by id of the resources
    """    
    if not isinstance(resources_raw, dict) : 
        raise ValueError("File wrongly formatted" + """\nexpected format : {"resources": [{"id": str,"type": str,"owner": str,"classification": str},...]}""")
    parsed_resources : dict[str, dict] = {}
    try:
        for resource in resources_raw["resources"]:
            resource_data = {
                "type" : resource["type"],
                "owner" : resource["owner"],
                "classification" : resource["classification"]
            }
            parsed_resources[resource["id"]] = resource_data
    except KeyError as e: 
        raise ValueError(f"File wrongly formatted, missing key : {e}" + """\nexpected format : {"resources": [{"id": str,"type": str,"owner": str,"classification": str},...]}""")
    return parsed_resources

def parse_policies(policies_raw : Any) -> list[dict]: 
    """Checks for correct formatting of the policies json file and returns a list of the policies
    Args:
        policies_raw (Any): Policies raw data from json file
    Raises:
        ValueError: Json file wrongly formatted : expected format : {"policies": [{"id": str,"subject": {},"resource": {},"actions": []},...]}
    Returns:
        list[dict]: The list of parsed policies
    """    
    if not isinstance(policies_raw, dict) : 
        raise ValueError("File wrongly formatted" + """\nexpected format : {"policies": [{"id": str,"subject": {},"resource": {},"actions": []},...]}""")
    parsed_policies : list[dict] = []
    try:
        for policy in policies_raw["policies"]:
            optional_context = policy.get("context", {}) #context might be optional, get prevents errors when missing
            policy_data = {
                "id" : policy["id"],
                "subject" : policy["subject"],
                "resource" : policy["resource"],
                "actions" : policy["actions"],
                "context" : optional_context
            }
            parsed_policies.append(policy_data)
    except KeyError as e: 
        raise ValueError(f"File wrongly formatted, missing key : {e}" + """\nexpected format : {"policies": [{"id": str,"subject": {},"resource": {},"actions": []},...]}""")
    return parsed_policies

def parse_requests(requests_raw : Any) -> list[dict]:
    """Checks for correct formatting of the requests json file and returns a list of the requests
    Args:
        requests_raw (Any): Requests raw data from json file
    Raises:
        ValueError: Json file wrongly formatted : expected format : {"requests": [{"request_id": str,"subject_id": str,"resource_id": str,"action": str,"context": {"hour": int,"mfa": bool}},...]}
    Returns:
        list[dict]: The list of parsed requests
    """    
    if not isinstance(requests_raw, dict) : 
        raise ValueError("File wrongly formatted" + """\nexpected format : {"requests": [{"request_id": str,"subject_id": str,"resource_id": str,"action": str,"context": {"hour": int,"mfa": bool}},...]}""")
    parsed_requests : list[dict] = []
    try:
        for request in requests_raw["requests"]:
            optional_context = request.get("context", {}) #context might be optional, get prevents errors when missing
            request_data = {
                "request_id" : request["request_id"],
                "subject_id" : request["subject_id"],
                "resource_id" : request["resource_id"],
                "action" : request["action"],
                "context" : optional_context
            }
            parsed_requests.append(request_data)
    except KeyError as e: 
        raise ValueError(f"File wrongly formatted, missing key : {e}" + """\nexpected format : {"requests": [{"request_id": str,"subject_id": str,"resource_id": str,"action": str,"context": {"hour": int,"mfa": bool}},...]}""")
    return parsed_requests