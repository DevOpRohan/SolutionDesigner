from langchain import PromptTemplate

planner_sys_prompt = """
You are a super intelligent math assistant and expert of Latex.
"""

planner_init_prompt = """Envision a trio of AI specialists, consisting of a Planner, a Solver, and a Verifier, collaborating to tackle a specific mathematical problem.

Problem:
```
{problem}
```

The Planner initiates the process by devising a strategy to solve the problem, which the Solver then implements. Upon completion, the Solver presents the results to the Verifier for validation. The Verifier provides feedback to the Planner, who may need to revise the plan. This cycle can be repeated up to two times until the Verifier confirms the accuracy of the solution.

- In case of MCQs, PLANNER observe the options carefully. Because options can be a constant or expressions consits of variable and constant.
Planner's Strategy: {{Please provide a maximum of four steps or points in a single line}}
"""


solver_sys_prompt = """
You are a super intelligent math assistant and expert of Latex.
"""

solver_init_prompt = '''
Envision a trio of AI specialists, consisting of a Planner, a Solver, and a Verifier, collaborating to tackle a specific mathematical problem.

Problem:
```
{problem}
```

The Planner initiates the process by devising a strategy to solve the problem, which the Solver then implements.

Planner's Strategy:
{plans}


SOLVER can choose to take one of the following actions:
**Action-Format Map**
{{
    1. Solution  -> "@solution: <concise_solution>"
    - To provide a final, detailed solution (minimum 2 - maximum 5 steps).
    2. Tools -> "@tools: [tool_name(query: <input_query>), tool_name(<input_query>), ...]"
    - To utilize tools (each can take an independent query)
}}

TOOLS:
[
    {{
        "name": "wolfram_alpha_api",
        "description": """
            This tool can be used to gather facts,symbolic calculations, solve equations, perform calculus, and other mathematical operations directly. It is not suitable for word problems. 
            The input query should be a single line.
        """,
        "example": "wolfram_alpha_api(query: "Solve x^2 + 5x + 6 = 0")", "wolfram_alpha_api(query: "Integrate x^2 + 5x + 6")"
    }},
    
    {{
        "name": "python_calculator_api",
        "description": """
            This tool can be used to perform integer calculations. It takes a Python expression (string) as input and uses eval().
            - Don't expect float results. For float results, prefer wolfram_alpha_api.
        """,
        "example": "python_calculator_api(query: "2 + (3-8) * 4**2")"
    }}
]

**Algorithms**
SOLVER job is to solve the problem using plans and tools as needed.
While using tools, wait for tools to respond.
- In case of MCQs, Be careful because options an be tricky or in form of variable or constant.

**Principles**
1. Use one action at a time and aim to come up with the final solution in a maximum of 7 iterations/conversations.
2. Always provide responses in the following format:
```
Observation: <one_linen_observation>
Thought: <thought>
Action: <appropriate_action>
'''

wolfram_alpha_parser_sys_prompt = """You are an intelligent AI parser.
"""
wolfram_alpha_parser_init_prompt = """Given a query and wolfram_api_output:
Query:
```
{Query}
```
WolframApiOutput:
```
{WolframApiOutput}
```

Retrieve a perfect result/answer from the api output.
If answer isn't present in the api output respond with @error.

Answer(One Linen):
"""

format_input_sys_prompt = """You are an intelligent AI , and expert of maths and latex."""
format_input_init_prompt = """
Content:
```
{content}
```
Please rewrite the above problem in beautified formatted way. So, that anyone can read and understand it.
- e.g. Remove "string(" to new line/line_break etc.

Formatted_Content:
"""

presentation_prompt = """Nice, 
Now present the solution in detailed and coincised way(neither too shorted and nor too detailed), like you are writing an exam paper docs. And please don't use any formatting keywords like frac, backslash, sqrt( like instead of it use original sign of root), any latex etc. Because directly have to copy in the exam paper, use proper superscript ,subscript etc.
SOLUTION:
"""

soln_beautifier_sys_prompt = """You are a solution designer for mathematics.
"""

soln_beautifier_init_prompt = """Rewrite this solution in better and concise way.
Avoid too much of words, omit the steps instructions, step numbering etc.. 
Pleas make use of proper lines (instead of writing the solution like essay)
Also use proper superscript, subscript, root sign etc.
And please don't use any formatting keywords like frac, backslash, sqrt( like instead of it use original sign of root), any latex etc. Because directly have to copy in the exam paper, use proper superscript ,subscript etc.
Write like, we are writing  for an exam paper.

SOLUTION:
```
{solution}.
```

REVISED SOLUTION:
"""


planner_init = PromptTemplate(
    input_variables=["problem"],
    template = planner_init_prompt
)

solver_init = PromptTemplate(
    input_variables=["problem", "plans"],
    template = solver_init_prompt
)

wolfram_alpha_parser_init = PromptTemplate(
    input_variables=["Query", "WolframApiOutput"],
    template = wolfram_alpha_parser_init_prompt
)

format_input_init = PromptTemplate(
    input_variables=["content"],
    template = format_input_init_prompt
)

soln_beautifier_init = PromptTemplate(
    input_variables=["solution"],
    template = soln_beautifier_init_prompt
)