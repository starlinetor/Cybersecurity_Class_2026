from typing import Any, TypedDict

class Summary(TypedDict):
    total_requests: int
    permitted_requests: int
    denied_requests: int

class Evaluated_Requests(TypedDict):
    summary: Summary
    results: list[dict[str,Any]]

def evaluate_requests(subjects_id : dict[str, dict], resources_id : dict[str, dict], policies_list : list[dict], requests_stack : list[dict]) -> Evaluated_Requests:
    
    evaluated_requests : Evaluated_Requests = {
        "summary": {
            "total_requests": 0,
            "permitted_requests": 0,
            "denied_requests": 0
        },
        "results" : []
    }

    for request in requests_stack:
        continue
    
    return evaluated_requests