from typing import TypedDict
from src.tests import TEST_LIST

class Summary(TypedDict):
    total_requests: int
    permitted_requests: int
    denied_requests: int

class RequestResult(TypedDict):
    request_id : str
    decision : str
    matched_policy : str | None
    matched_conditions : list[str]

class EvaluatedRequests(TypedDict):
    summary: Summary
    results: list[RequestResult]

def evaluate_requests(subjects_id : dict[str, dict], resources_id : dict[str, dict], policies_list : list[dict], requests_stack : list[dict]) -> EvaluatedRequests:
    """Policy evaluation engine that evaluates a list of requests against the provided subjects, resources and policies.

    Args:
        subjects_id (dict[str, dict]): The dictionary by id of the subjects
        resources_id (dict[str, dict]): The dictionary by id of the resources
        policies_list (list[dict]): The list of policies
        requests_stack (list[dict]): The list of requests to evaluate

    Returns:
        EvaluatedRequests: The evaluated requests with summary and results
    """
    evaluated_requests : EvaluatedRequests = {
        "summary": {
            "total_requests": 0,
            "permitted_requests": 0,
            "denied_requests": 0
        },
        "results" : []
    }

    for request in requests_stack:
        request_result = evaluate_request(subjects_id, resources_id, policies_list, request)
        update_summary(evaluated_requests["summary"], request_result)
        evaluated_requests["results"].append(request_result)
    
    return evaluated_requests

def evaluate_request(subjects_id : dict[str, dict], resources_id : dict[str, dict], policies_list : list[dict], request : dict) -> RequestResult:
    """Evaluates a single request against the provided subjects, resources and policies and returns the evaluation result.

    Args:
        subjects_id (dict[str, dict]): The dictionary by id of the subjects
        resources_id (dict[str, dict]): The dictionary by id of the resources
        policies_list (list[dict]): The list of policies
        request (dict): The request to evaluate

    Returns:
        RequestResult: Result of the request evaluation with evaluation details
    """
    evaluated_request : RequestResult = {
        "request_id" : request["request_id"],
        "decision" : "Deny",
        "matched_policy" : None,
        "matched_conditions" : []
    }
    subject_id = request["subject_id"]
    resource_id = request["resource_id"]
    
    try:
        subject = subjects_id[subject_id]
        resource = resources_id[resource_id]
    except KeyError: #if retrieval fails return Deny, no need to check policies
        return evaluated_request
    
    for policy in policies_list: 
        result, matched_conditions = test_policy(policy, subject_id, subject, resource_id, resource, request)
        if result:
            evaluated_request["decision"] = "Permit"
            evaluated_request["matched_policy"] = policy["id"]
            evaluated_request["matched_conditions"] = matched_conditions
            return evaluated_request #policy found that matches the request, return Permit and stop searching for other policies

    return evaluated_request

def update_summary(summary : Summary, request_result : RequestResult) -> None:
    """Updates the summary of the evaluated requests with the result of a single request evaluation

    Args:
        summary (Summary): The summary of the evaluated requests to update
        request_result (dict[str,Any]): The result of the request evaluation to update the summary with
    """
    summary["total_requests"] += 1
    if request_result["decision"] == "Permit":
        summary["permitted_requests"] += 1
    else:
        summary["denied_requests"] += 1
    return

def test_policy(policy : dict, subject_id : str, subject : dict, resource_id : str, resource : dict, request : dict) -> tuple[bool, list[str]]:
    """Tests if a policy satisfies a request by testing all conditions and returns the result of the test and the matched conditions.

    Args:
        policy (dict): Policy to test
        subject_id (str): Id of the subject
        subject (dict): Subject data
        resource_id (str): Resource id
        resource (dict): Resource data
        request (dict): Request to evaluate

    Returns:
        tuple[bool, list[str]]: Result of the evaluation and the list of the matched conditions
    """
    total_matched_conditions : list[str] = []
    result : bool = False
    matched_condition : list[str] = []
    
    for test in TEST_LIST:
        result, matched_condition = test(policy = policy, subject_id = subject_id, subject = subject, resource_id = resource_id, resource = resource, request = request)
        if not result:
            return(result, [])
        if matched_condition : #empty lists are evaluated as false by python
            #a test might return true because its not in the policy, we ignore the matched condition as there isn't one
            total_matched_conditions.extend(matched_condition)
    
    return (result, total_matched_conditions)

