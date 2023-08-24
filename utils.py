import re
import json


def extract_action(input_string):
    action_regex = r"Observation:.+Thought:.+Action: (.+)"
    match = re.search(action_regex, input_string, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_solution(input_string):
    if "@solution:" not in input_string:
        return None
    result = input_string.replace("@solution:", "").strip()
    return result


def extract_tools(input_string):
    tools_regex = r"tools: (.+)"
    match = re.search(tools_regex, input_string, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_function_calls(input_string):
    input_string = extract_tools(input_string)
    # print(f"Parsed Tools: {input_string}")
    matches = re.findall(r'(\w+)\(query: "(.*?)"\)', input_string)
    function_calls = [{"name": match[0], "query": match[1]} for match in matches]
    return function_calls
