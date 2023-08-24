from prompts import solver_sys_prompt, solver_init, format_input_sys_prompt, format_input_init, planner_sys_prompt, \
    planner_init, presentation_prompt, soln_beautifier_sys_prompt, soln_beautifier_init
import openai
import concurrent.futures

from utils import extract_action, extract_function_calls, extract_solution
from wolfram_alpha import WolframAlphaAPI
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


class SolverAgent:
    def __init__(self, problem=" "):
        self.wolfram_alpha_api = WolframAlphaAPI()
        self.problem = self.format_input(problem)
        self.plans = self.planner(problem)

        self.conversation_history = [
            {
                'role': "system",
                'content': solver_sys_prompt
            },
            {
                'role': "user",
                'content': solver_init.format(problem=self.problem, plans=self.plans)
            }
        ]

        # tools_name - function_name mapping
        self.api_function_map = {
            "wolfram_alpha_api": self.wolfram_alpha_api.full_length_result_query,
            "python_calculator_api": self.python_calculator_api
        }

    def start(self):
        while True:
            # Create a chat completion with OpenAI
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.conversation_history,
                temperature=0,
                max_tokens=1024,
            )

            # Get the result from the completion
            assistant_response = completion.choices[0].message["content"]

            print(assistant_response)

            # Append the response to the messages
            self.conversation_history.append({"role": "assistant", "content": assistant_response})

            # Extract the action
            action = extract_action(assistant_response)

            # print(f"Action_Parsed: {action}")

            # Extract the result
            solution = extract_solution(action)

            if solution is not None:
                # using gpt-3.5-turbo to retrieve the solution in detailed and coincise way
                self.conversation_history.append({"role": "user", "content": presentation_prompt})

                completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=self.conversation_history,
                    temperature=0,
                    max_tokens=1024,
                )

                soln = completion.choices[0].message["content"]

                messages = [
                    {
                        'role': "system",
                        'content': soln_beautifier_sys_prompt
                    },
                    {
                        'role': "user",
                        'content': soln_beautifier_init.format(solution=soln)
                    }
                ]

                completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=messages,
                    temperature=0,
                    max_tokens=1024,
                )

                return completion.choices[0].message["content"]

            # Extract the function calls
            function_calls = extract_function_calls(action)

            # print(f"Function Calls Dict: {function_calls}")

            # Use a ThreadPoolExecutor to call all functions concurrently
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # For each dictionary in the list, call the appropriate function with the appropriate query
                function_results = [executor.submit(self.api_function_map[query["name"]], query["query"]) for query in
                                    function_calls]

            # Collect the results in an array in the order they appear in the JSON input
            user_response = [result.result() for result in function_results]
            print("Tools Response: ")
            print(user_response)

            # Append the response to the messages
            self.conversation_history.append({"role": "user", "content": ' '.join(map(str, user_response))})

            print("\n \n")

    def python_calculator_api(self, expression: str) -> float:
        try:
            result = eval(expression)
            return result
        except Exception as e:
            print(f"An error occurred while evaluating the expression: {e}")
            return "An error occurred while evaluating the expression"

    def format_input(self, problem):
        messages = [
            {
                'role': "system",
                'content': format_input_sys_prompt
            },
            {
                'role': "user",
                'content': format_input_init.format(content=problem)
            }
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            max_tokens=2048,
        )

        assistant_response = completion.choices[0].message["content"]

        return assistant_response

    def planner(self, problem):
        messages = [
            {
                'role': "system",
                'content': planner_sys_prompt
            },
            {
                'role': "user",
                'content': planner_init.format(problem=problem)
            }
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            max_tokens=1024,
        )

        assistant_response = completion.choices[0].message["content"]
        print(f"PLANS: \n{assistant_response}")
        return assistant_response
