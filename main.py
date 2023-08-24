import time

from solver_agent import SolverAgent

problem_gmat_18 = """
[,string(18. If latex(n) is the product of the integers from 1 to 8 , inclusive, how many different prime factors greater than 1 does latex(n) have?),string((A) Four),string((B) Five),string((C) Six),string((D) Seven),string((E) Eight),]"""

problem_gmat_16 = """
[,string(16. If latex(\\sqrt{3-2 x}=\\sqrt{2 x}+1) then, latex(4 x^{2}=)),string((A) 1),string((B) 4),string((C) latex(2-2 x)),string((D) latex(4 x-2)),string((E) latex(6 x-1)),]
"""
problem_gmat_15 = """
[,string(The product of all the prime numbers less than 20 is closest to which of the following powers of 10 ?),string((A) latex(10^{9})),string((B) latex(10^{8})),string((C) latex(10^{7})),string((D) latex(10^{6})),string((E) latex(\\quad 10^{5})),]
"""
problem_gmat_13 = """
[,string(If latex(s) and latex(t) are positive integers such that latex(\\dfrac{s}{t}=64.12), which of the following could be the remainder when latex(s) is divided by latex(t) ?),string((A) 2),string((B) 4),string((C) 8),string((D) 20),string((E) 45),]
"""
problem_gmat_22="""
[,string(A container in the shape of a right circular cylinder is latex(\\dfrac{1}{2}) full of water. If the volume of water in the container is 36 cubic inches and the height of the container is 9 inches, what is the diameter of the base of the cylinder, in inches?),string((A) latex(\\dfrac{16}{9 \\pi})),string((B) latex(\\dfrac{4}{\\sqrt{\\pi}})),string((C) latex(\\dfrac{12}{\\sqrt{\\pi}})),string((D) latex(\\sqrt{\\dfrac{2}{\\pi}})),string((E) latex(\\quad 4 \\sqrt{\\dfrac{2}{\\pi}})),]
"""
problem_gmat_19="""
If k is an integer and 2 < k < 7, for how many different
values of k is there a triangle with sides of lengths 2,
7, and k?
a. One
b. Two
c. Three
d. Four
e. Five
"""
problem_gmat_17="""
If n = sqrt(16/81). What is the value of sqrt(n)
a. 1/9
b. 1/4
c. 4/9
d. 2/3
e. 9/2
"""
cat_20_f = """
Find the quadratic equation whose roots are 2 more than the roots of the equation
 x2 – 6x + 4 = 0.
"""
gmat_20 = """
A right circular cone is inscribed in a hemisphere such that the base of the cone coincides with the base of the hemisphere. What is the ratio of the height of the cone to the radius of the hemisphere?
(A) √3:1
(B) 1:1
(C) 1:1
(D) √2:1
(E) 2:1
"""
solver_agent = SolverAgent(problem=cat_20_f)
soln = solver_agent.start()
print("\n===========SOLUTION==============")
print(soln)
#
# # Let's create a array of dectionary {probem_name, problem} and loop through it and solve it and print the result:
# problems = [
#     # {"name": "problem_gmat_18", "problem": problem_gmat_18},
#     # {"name": "problem_gmat_16", "problem": problem_gmat_16},
#     # {"name": "problem_gmat_15", "problem": problem_gmat_15},
#     # {"name": "problem_gmat_13", "problem": problem_gmat_13},
#     # {"name": "problem_gmat_22", "problem": problem_gmat_22},
#     # {"name": "problem_gmat_19", "problem": problem_gmat_19},
#     # {"name": "problem_gmat_17", "problem": problem_gmat_17},
#     # {"name": "cat_20_f", "problem": cat_20_f},
#     {"name": "gmat_20", "problem": gmat_20},
# ]
#
# # Also write the solution to a file
# with open("solution.txt", "a", encoding='utf-8') as f:
#     for problem in problems:
#         print(f"\n\nProblem: {problem['name']}")
#         f.write("\n\n***********************************")
#         f.write(f"\nProblem: {problem['name']}")
#         f.write("\n***********************************")
#         solver_agent = SolverAgent(problem=problem["problem"])
#         soln = solver_agent.start()
#         print("\n===========SOLUTION==============\n")
#         print(soln)
#         f.write("\n===========SOLUTION==============\n")
#         f.write(soln)
#         #wait for 5 seconds
#         time.sleep(5)