#include <iostream>
using namespace std;

int findLru(int time[], int n)
{
    int minimum = time[0], pos = 0;
    for (int i = 1; i < n; i++)
    {
        if (time[i] < minimum)
        {
            minimum = time[i];
            pos = i;
        }
    }
    return pos;
}

int main()
{
    int pages, frames, page[50], frame[10], time[10], counter = 0, flag1, flag2, pos, page_faults = 0;

    cout << "enter total number of pages:";
    cin >> pages;

    cout << "enter page reference string:" << endl;
    for (int i = 0; i < pages; i++)
    {
        cin >> page[i];
    }

    cout << "enter total number of frames:";
    cin >> frames;

    for (int i = 0; i < frames; i++)
    {
        frame[i] = -1;
    }

    // main for loop

    for (int i = 0; i < pages; i++)
    {
        flag1 = flag2 = 0;

        for (int j = 0; j < frames; j++)
        {
            if (frame[j] == page[i])
            {
                counter++;
                time[j] = counter;
                flag1 = flag2 = 1;
                break;
            }
        }
        if (flag1 == 0)
        {
            for (int j = 0; j < frames; j++)
            {
                if (frame[j] == -1)
                {
                    counter++;
                    page_faults++;
                    frame[j] = page[i];
                    time[j] = counter;
                    flag2 = 1;
                    break;
                }
            }
        }
        if (flag2 == 0)
        {
            pos = findLru(time, frames);
            counter++;
            page_faults++;
            frame[pos] = page[i];
            time[pos] = counter;
            // break;
        }

        cout << "frames:";
        for (int j = 0; j < frames; j++)
        {
            if (frame[j] != -1)
            {
                cout << frame[j] << " ";
            }
            else
            {
                cout << "- ";
            }
        }
        cout << endl;
    }
    cout << "total number of page faults:" << page_faults;
}

/*
Total number of pages: 6
Page reference string: 1 2 3 4 1 2
Total number of frames: 3
*/