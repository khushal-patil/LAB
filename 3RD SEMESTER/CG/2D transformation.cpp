#include <iostream>
#include <graphics.h>
#include <cmath>
using namespace std;

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);
    int b[3][3];
    int d;
    cout << "enter value of x1,y1";
    cin >> b[0][0] >> b[1][0];
    cout << "enter value of x2 & y2";
    cin >> b[0][1] >> b[1][1];
    cout << "enter value of x3 & y3";
    cin >> b[0][2] >> b[1][2];
    b[2][0] = b[2][1] = b[2][2] = 1;
    setcolor(RED);
    line(b[0][0], b[1][0], b[0][1], b[1][1]);
    line(b[0][1], b[1][1], b[0][2], b[1][2]);
    line(b[0][2], b[1][2], b[0][0], b[1][0]);

    delay(5000);
    cout << "Enter your choice\n1.Translation\n2.Scaling\n3.Rotation";
    cin >> d;
    switch (d)
    {
    case 1:
    {
        int a[3][3], c[3][3];
        cout << "enter value for tx,ty";
        cin >> a[0][2] >> a[1][2];
        a[0][0] = a[1][1] = a[2][2] = 1;
        a[1][0] = a[2][0] = a[0][1] = a[2][1] = 0;

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                c[i][j] = 0;
                for (int k = 0; k < 3; k++)
                {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        setcolor(BLUE);
        line(c[0][0], c[1][0], c[0][1], c[1][1]);
        line(c[0][1], c[1][1], c[0][2], c[1][2]);
        line(c[0][2], c[1][2], c[0][0], c[1][0]);
        delay(5000);
    }
    break;

    case 2:
    {
        float sx, sy;
        float a[3][3], c[3][3];
        cout << "enter scaling factor Sx and Sy";
        cin >> a[0][0] >> a[1][1];
        a[2][2] = 1;
        a[0][1] = a[0][2] = a[1][0] = a[1][2] = a[2][0] = a[2][1] = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                c[i][j] = 0;
                for (int k = 0; k < 3; k++)
                {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        setcolor(BLUE);
        line(c[0][0], c[1][0], c[0][1], c[1][1]);
        line(c[0][1], c[1][1], c[0][2], c[1][2]);
        line(c[0][2], c[1][2], c[0][0], c[1][0]);
        delay(5000);
    }
    break;

    case 3:
    {
        float z, A;
        float a[3][3];
        float c[3][3];
        cout << "enter the angle";
        cin >> z;

        A = (z * 3.14) / 180;
        a[2][2] = 1;
        a[0][2] = a[1][2] = a[2][0] = a[2][1] = 0;
        a[0][0] = a[1][1] = cos(A);
        a[0][1] = sin(A);
        a[1][0] = (-sin(A));

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                c[i][j] = 0;
                for (int k = 0; k < 3; k++)
                {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        setcolor(BLUE);
        line(c[0][0], c[1][0], c[0][1], c[1][1]);
        line(c[0][1], c[1][1], c[0][2], c[1][2]);
        line(c[0][2], c[1][2], c[0][0], c[1][0]);
        delay(5000);
    }
    break;

        closegraph();
    }
}