import argparse
import json
from pathlib import Path
from src.loader import load_json
from src.engine import EvaluatedRequests, evaluate_requests
from src.verify_json import parse_subjects, parse_resources, parse_policies, parse_requests

def parse_args() -> argparse.Namespace:
    """Defines arguments for the script and loads them as Namespaces

    Returns:
        argparse.Namespace: parsed arguments (input,output)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input directory")
    parser.add_argument("--output", required=True, help="Output JSON file")
    return parser.parse_args()

def main():
    args : argparse.Namespace = parse_args()
    input_dir : Path = Path(args.input)
    
    subjects = load_json(input_dir.joinpath("subjects.json"))
    resources = load_json(input_dir.joinpath("resources.json"))
    policies = load_json(input_dir.joinpath("policies.json"))
    requests = load_json(input_dir.joinpath("requests.json"))

    subjects_id : dict[str, dict] = parse_subjects(subjects)
    resources_id : dict[str, dict] = parse_resources(resources)
    policies_list : list[dict] = parse_policies(policies)
    requests_stack : list[dict] = parse_requests(requests)

    result : EvaluatedRequests = evaluate_requests(subjects_id , resources_id, policies_list, requests_stack)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()