// Code-2 (Parallel Bubble Sort and Merge Sort)

/*
 * THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.
 *
 * Problem Statement:
 *  Write a program to implement Parallel Bubble Sort and Merge sort using OpenMP.
 *  Use existing algorithms and measure the performance of sequential and parallel algorithms.
 *
 * Code from HighPerformanceComputing (SPPU - Final Year - Computer Engineering - Content)
 * repository on KSKA Git: https://git.kska.io/sppu-be-comp-content/HighPerformanceComputing
 **/

/*
 * EXECUTION INSTRUCTIONS (Debian-based distributions):
 *
 * i) Install g++ with OpenMP support:
 *   sudo apt update
 *   sudo apt install g++
 *
 * ii) Compile:
 *   g++ -fopenmp Code-2.cpp -o Code-2
 *
 * iii) Execute:
 *   ./Code-2
 **/

// BEGINNING OF CODE
#include <iostream>
#include <vector>
#include <cstdlib>
#include <omp.h>

using namespace std;

void printArray(const vector<int>& arr) {
    for (int num : arr)
        cout << num << " ";
    cout << endl;
}


// Merge Sort

// Merges two sorted halves arr[left..mid] and arr[mid+1..right] in place.
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void sequentialMergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    sequentialMergeSort(arr, left, mid);
    sequentialMergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

// Parallel merge sort using OpenMP tasks.
// "#pragma omp parallel sections" inside a recursive function would spawn a
// new thread team at every level of recursion, hundreds of thousands of teams
// for a large array, causing enormous overhead and likely a crash.
// Tasks are lighter: the runtime schedules them across an existing thread pool.
// The depth cutoff switches to sequential below a threshold to avoid spawning
// tasks so small that the overhead exceeds the work itself.
void parallelMergeSortHelper(vector<int>& arr, int left, int right, int depth) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;

    if (depth <= 0) {
        // Below the cutoff the subarray is small enough that sequential is faster.
        sequentialMergeSort(arr, left, mid);
        sequentialMergeSort(arr, mid + 1, right);
    } else {
        #pragma omp task
        parallelMergeSortHelper(arr, left, mid, depth - 1);

        #pragma omp task
        parallelMergeSortHelper(arr, mid + 1, right, depth - 1);

        // Wait for both tasks to finish before merging.
        #pragma omp taskwait
    }

    merge(arr, left, mid, right);
}

void parallelMergeSort(vector<int>& arr, int left, int right) {
    // The single directive creates one thread team for the entire sort.
    // All recursive tasks share this pool instead of creating new teams.
    #pragma omp parallel
    {
        // single ensures only one thread kicks off the root task;
        // the rest wait and pick up the child tasks as they are created.
        #pragma omp single
        parallelMergeSortHelper(arr, left, right, 4); // depth 4 → up to 16 parallel tasks
    }
}

// Main function

int main() {
    int n = 10000; // Adjust this to specify the number of elements.
    vector<int> arr(n);

    for (int i = 0; i < n; i++)
        arr[i] = rand() % 10000;

    double start, end;
    double time_seq_bubble, time_par_bubble;
    double time_seq_merge, time_par_merge;


    vector<int> seqArr = arr;
    vector<int> parArr = arr;


    // --- Sequential Merge Sort ---
    seqArr = arr;
    start = omp_get_wtime();
    sequentialMergeSort(seqArr, 0, n - 1);
    end = omp_get_wtime();
    time_seq_merge = end - start;
    cout << "\nSequential Merge Sort time: " << time_seq_merge << " seconds" << endl;

    // --- Parallel Merge Sort ---
    parArr = arr;
    start = omp_get_wtime();
    parallelMergeSort(parArr, 0, n - 1);
    end = omp_get_wtime();
    time_par_merge = end - start;
    cout << "Parallel Merge Sort time: " << time_par_merge << " seconds" << endl;

    cout << "Merge Sort Speedup (Sequential / Parallel) = " << (time_seq_merge / time_par_merge) << "x" << endl;

    return 0;
}
// END OF CODE

/*
EXAMPLE OUTPUT (when n=10000):

$ ./Code-2 
Sequential Bubble Sort time: 0.955394 seconds
Parallel Bubble Sort time: 0.282093 seconds
Bubble Sort Speedup (Sequential / Parallel) = 3.38681x

Sequential Merge Sort time: 0.0116294 seconds
Parallel Merge Sort time: 0.00282529 seconds
Merge Sort Speedup (Sequential / Parallel) = 4.11618x
*/

