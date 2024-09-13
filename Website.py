import streamlit as st
import sympy as sp

def solve_math_problem(problem):
    try:
        # Parse and solve the mathematical expression
        # expr = sp.sympify(problem)
        # solution = sp.simplify(expr)
        solution = problem
        return solution
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Mathematics Solver")

    # Input box for the user to type a mathematical problem
    problem = st.text_area("Enter a mathematical problem:")

    if st.button("Giải bài"):
        if problem:

            # Solve the problem
            st.write("Lời giải\n")
            solution = solve_math_problem(problem)

            # Display the result with MathJax rendering
            st.markdown(solution)    
        else:
            st.write("Vui lòng nhập đề bài trước khi bấm 'Giải bài.'")    

if __name__ == "__main__":
    main()
