#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to find the optimal page to replace
int findOptimal(int pages[], int frames[], int current_index, int frames_count, int total_pages)
{
    int pos = -1, farthest = current_index;
    for (int i = 0; i < frames_count; i++)
    {
        int j;
        for (j = current_index; j < total_pages; j++)
        {
            if (frames[i] == pages[j])
            {
                if (j > farthest)
                {
                    farthest = j;
                    pos = i;
                }
                break;
            }
        }
        if (j == total_pages) // Page not found in future references
            return i;
    }
    return (pos == -1) ? 0 : pos;
}

int main()
{
    int pages[50], frames[10];
    int pages_count, frames_count, page_faults = 0;

    cout << "Enter total number of pages: ";
    cin >> pages_count;
    
    cout << "Enter page reference string:" << endl;
    for (int i = 0; i < pages_count; i++)
    {
        cin >> pages[i];
    }

    cout << "Enter total number of frames: ";
    cin >> frames_count;

    for (int i = 0; i < frames_count; i++)
    {
        frames[i] = -1; // Initialize frames to -1 (indicating empty)
    }

    // Main loop to go through each page in the reference string
    for (int i = 0; i < pages_count; i++)
    {
        bool page_found = false;
        
        // Check if page is already in a frame
        for (int j = 0; j < frames_count; j++)
        {
            if (frames[j] == pages[i])
            {
                page_found = true;
                break;
            }
        }

        if (!page_found)
        {
            int pos;
            if (i < frames_count) // Fill up empty frames initially
            {
                pos = i;
            }
            else
            {
                pos = findOptimal(pages, frames, i + 1, frames_count, pages_count);
            }
            
            frames[pos] = pages[i]; // Replace the frame with the new page
            page_faults++;
        }

        cout << "Frames: ";
        for (int j = 0; j < frames_count; j++)
        {
            if (frames[j] != -1)
                cout << frames[j] << " ";
            else
                cout << "- ";
        }
        cout << endl;
    }

    cout << "Total number of page faults: " << page_faults << endl;

    return 0;
}
