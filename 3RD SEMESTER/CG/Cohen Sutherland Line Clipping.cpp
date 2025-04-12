#include <iostream>
#include <graphics.h>
#include <math.h>
#include <cstdlib>

using namespace std;

static int LEFT = 1, RIGHT = 2, BOTTOM = 4, TOP = 8, xmin, ymin, xmax, ymax;

int getcode(int x, int y)
{
	int code = 0;
	if (y > ymax)
		code = code | TOP;
	if (y < ymin)
		code = code | BOTTOM;
	if (x > xmax)
		code = code | LEFT;
	if (x < xmin)
		code = code | RIGHT;

	return code;
}

int main()
{
	int gd = DETECT, gm;
	initgraph(&gd, &gm, NULL);

	setcolor(WHITE);
	delay(1500);
	cout << "Enter top left  and right bottom  coordinate of window :";
	cin >> xmin >> ymin >> xmax >> ymax;
	int x1, y1, x2, y2;
	cout << "Enter coordinate of  line: ";
	cin >> x1 >> y1 >> x2 >> y2;
	cout << "before clipping" << endl;
	rectangle(xmin, ymin, xmax, ymax);
	line(x1, y1, x2, y2);
	delay(10000);

	// clip started
	int code1 = getcode(x1, y1);
	int code2 = getcode(x2, y2);

	int accept = 0;
	while (1)
	{
		float m = float((y2 - y1) / (x2 - x1));
		if (code1 == 0 && code2 == 0)
		{
			accept = 1;
			break;
		}

		else if ((code1 & code2) != 0)
		{
			break;
		}
		else
		{
			int x, y;
			int temp;
			if (code1 == 0)
			{
				temp = code2;
			}
			else
			{
				temp = code1;
			}
			if (temp & TOP)
			{
				x = x1 + (ymax - y1) / m;
				y = ymax;
			}
			else if (temp & BOTTOM)
			{
				x = x1 + (ymin - y1) / m;
				y = ymin;
			}
			else if (temp & LEFT)
			{

				x = xmin;
				y = y1 + m * (xmin - x1);
			}
			else if (temp & RIGHT)
			{

				x = xmax;
				y = y1 + m * (xmax - x1);
			}
			if (temp == code1)
			{
				x1 = x;
				y1 = y;
				code1 = getcode(x1, y1);
			}
			else
			{
				x2 = x;
				y2 = y;
				code2 = getcode(x2, y2);
			}
		}
	}
	setcolor(YELLOW);
	if (accept)
	{
		cleardevice();
		cout << "\nAfter clipping" << endl;
		rectangle(xmin, ymin, xmax, ymax);
		line(x1, y1, x2, y2);
	}
	else
	{
		cleardevice();
		cout << "\nAfter clipping" << endl;
		rectangle(xmin, ymin, xmax, ymax);
	}

	getch();
	closegraph();
	return 0;
}