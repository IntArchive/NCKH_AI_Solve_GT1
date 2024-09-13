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


    # if problem:
    #     # Solve the problem
    #     solution = solve_math_problem(problem)
        
    #     # Display the result with MathJax rendering
    #     st.markdown(f"**Solution:**")
    #     st.markdown(solution)
    
    if st.button("Giải bài"):
        if problem:
            solution = f"Lời giải cho bài toán '{problem}' sẽ được hiển thị ở đây."
        else:
            st.write("Vui lòng nhập đề bài trước khi bấm 'Giải bài.'")    

if __name__ == "__main__":
    main()
