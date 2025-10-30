import numpy as np
import threading
import time


# ---------- Single-threaded Matrix Multiplication ----------
def single_threaded_mult(A, B):
    """
    Performs single-threaded matrix multiplication using NumPy's dot product.
    """
    return np.dot(A, B)


# ---------- Multithreaded Matrix Multiplication (One thread per row) ----------
def multithreaded_mult(A, B):
    """
    Performs multithreaded matrix multiplication with one thread per row.
    """
    result = np.zeros((A.shape[0], B.shape[1]))

    def compute_row(i):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i][j] += A[i][k] * B[k][j]

    threads = []
    for i in range(A.shape[0]):
        thread = threading.Thread(target=compute_row, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


# ---------- Main Function ----------
def main():
    print("🧮 Matrix Multiplication (Single-threaded vs Multithreaded)\n")

    # --- Input Matrix Dimensions ---
    r1 = int(input("Enter number of rows for Matrix A: "))
    c1 = int(input("Enter number of columns for Matrix A: "))
    r2 = int(input("Enter number of rows for Matrix B: "))
    c2 = int(input("Enter number of columns for Matrix B: "))

    # --- Check Matrix Multiplication Rule ---
    if c1 != r2:
        print("\n❌ Matrix multiplication not possible! (Columns of A ≠ Rows of B)")
        return

    # --- Input Matrices ---
    print("\nEnter elements for Matrix A:")
    A = np.zeros((r1, c1))
    for i in range(r1):
        for j in range(c1):
            A[i][j] = float(input(f"A[{i+1}][{j+1}]: "))

    print("\nEnter elements for Matrix B:")
    B = np.zeros((r2, c2))
    for i in range(r2):
        for j in range(c2):
            B[i][j] = float(input(f"B[{i+1}][{j+1}]: "))

    # --- Single-threaded Execution ---
    start_single = time.time()
    result_single = single_threaded_mult(A, B)
    end_single = time.time()

    # --- Multithreaded Execution ---
    start_multi = time.time()
    result_multi = multithreaded_mult(A, B)
    end_multi = time.time()

    # --- Display Results ---
    print("\n✅ Result of Matrix Multiplication (Single-threaded):")
    print(result_single)

    print("\n✅ Result of Matrix Multiplication (Multithreaded):")
    print(result_multi)

    print("\n⚙️  Performance Comparison:")
    print(f"Single-threaded Time: {(end_single - start_single) * 1000:.4f} ms")
    print(f"Multithreaded Time: {(end_multi - start_multi) * 1000:.4f} ms")

    # --- Analysis ---
    print("\n🧠 Analysis:")
    if (end_multi - start_multi) < (end_single - start_single):
        print("➡️ Multithreaded approach performed faster (benefits from parallel computation).")
    else:
        print("➡️ Single-threaded approach performed faster (overhead of threading on small data).")


if __name__ == "__main__":
    main()
