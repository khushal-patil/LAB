#include <iostream>
#include <vector>
#include <cstddef>
#include <thread>
#include <chrono>     // For high-resolution time measurement
#include <random>     // For generating random matrices
#include <algorithm>  // For std::min
#include <stdexcept>  // For std::runtime_error
#include <functional> // For std::ref, std::cref
#include <atomic>

std::atomic<int> counter;

// Function to multiply a single row of matrix A with matrix B
void multiplyRow(const std::vector<std::vector<int>>& A,
                 const std::vector<std::vector<int>>& B,
                 std::vector<std::vector<int>>& C,
                 int row_idx)
{
    int num_cols_B = B[0].size();
    int num_rows_B = B.size();

    for (int j = 0; j < num_cols_B; ++j) {
        int sum = 0;
        for (int k = 0; k < num_rows_B; ++k) {
            sum += A[row_idx][k] * B[k][j];
        }
        C[row_idx][j] = sum;
    }
}

// Single-threaded matrix multiplication
std::vector<std::vector<int>> singleThreadedMultiply(const std::vector<std::vector<int>>& A,
                                                     const std::vector<std::vector<int>>& B)
{
    int rows_A = A.size();
    int cols_A = A[0].size();
    int rows_B = B.size();
    int cols_B = B[0].size();

    if (cols_A != rows_B) {
        throw std::runtime_error("Matrices cannot be multiplied: inner dimensions must match.");
    }

    std::vector<std::vector<int>> C(rows_A, std::vector<int>(cols_B, 0));

    for (int i = 0; i < rows_A; ++i) {
        for (int j = 0; j < cols_B; ++j) {
            for (int k = 0; k < cols_A; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return C;
}

// Multithreaded matrix multiplication (row-wise)
std::vector<std::vector<int>> multiThreadedMultiply(const std::vector<std::vector<int>>& A,
                                                    const std::vector<std::vector<int>>& B)
{
    int rows_A = A.size();
    int cols_A = A[0].size();
    int rows_B = B.size();
    int cols_B = B[0].size();

    if (cols_A != rows_B) {
        throw std::runtime_error("Matrices cannot be multiplied: inner dimensions must match.");
    }

    std::vector<std::vector<int>> C(rows_A, std::vector<int>(cols_B, 0));
    std::vector<std::thread> thread_list;

    // Launch one thread per row
    for (int i = 0; i < rows_A; ++i) {
        thread_list.emplace_back(multiplyRow, std::cref(A), std::cref(B), std::ref(C), i);
    }

    // Join all threads
    for (auto& t : thread_list) {
        if (t.joinable())
            t.join();
    }

    return C;
}

// Function to generate a random matrix
std::vector<std::vector<int>> generateRandomMatrix(int rows, int cols)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(0, 10);

    std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            matrix[i][j] = distrib(gen);

    return matrix;
}

// Function to print matrix (partial)
void printMatrix(const std::vector<std::vector<int>>& M, int limit = 3)
{
    int rows = M.size();
    int cols = M[0].size();

    for (int i = 0; i < std::min(rows, limit); ++i) {
        for (int j = 0; j < std::min(cols, limit); ++j)
            std::cout << M[i][j] << "\t";
        if (cols > limit) std::cout << "...";
        std::cout << std::endl;
    }
    if (rows > limit) std::cout << "..." << std::endl;
}

int main()
{
    int MATRIX_SIZE;
    std::cout << "Enter matrix size (e.g., 200, 500): ";
    std::cin >> MATRIX_SIZE;

    std::cout << "\nPerforming Matrix Multiplication for "
              << MATRIX_SIZE << "x" << MATRIX_SIZE << " matrices\n";

    // Generate random matrices
    std::vector<std::vector<int>> A = generateRandomMatrix(MATRIX_SIZE, MATRIX_SIZE);
    std::vector<std::vector<int>> B = generateRandomMatrix(MATRIX_SIZE, MATRIX_SIZE);

    // --- Single-threaded Execution ---
    auto start_single = std::chrono::high_resolution_clock::now();
    std::vector<std::vector<int>> C_single = singleThreadedMultiply(A, B);
    auto end_single = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> time_single = end_single - start_single;

    std::cout << "Single-threaded Time: " << time_single.count() << " seconds\n";

    // --- Multithreaded Execution ---
    auto start_multi = std::chrono::high_resolution_clock::now();
    std::vector<std::vector<int>> C_multi = multiThreadedMultiply(A, B);
    auto end_multi = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> time_multi = end_multi - start_multi;

    std::cout << "Multithreaded Time: " << time_multi.count() << " seconds\n";

    // --- Check correctness ---
    if (C_single == C_multi)
        std::cout << "\n✅ Results match! Both implementations are correct.\n";
    else
        std::cout << "\n⚠️ Results differ! Please check implementation.\n";

    // --- Speedup Calculation ---
    if (time_multi.count() > 0)
    {
        double speedup = time_single.count() / time_multi.count();
        double improvement = ((time_single.count() - time_multi.count()) / time_single.count()) * 100;

        std::cout << "\n⚙️ Performance Summary:\n";
        std::cout << "Speedup: " << speedup << "x\n";
        std::cout << "Percentage Improvement: " << improvement << "%\n";
    }

    // --- Optional Small Matrix Print ---
    if (MATRIX_SIZE <= 5)
    {
        std::cout << "\nMatrix A (partial):\n";
        printMatrix(A);
        std::cout << "\nMatrix B (partial):\n";
        printMatrix(B);
        std::cout << "\nResult Matrix (Single-threaded, partial):\n";
        printMatrix(C_single);
    }

    return 0;
}
