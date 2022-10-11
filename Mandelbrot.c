// gcc -shared -o Mandelbrot.o .\Mandelbrot.c
#include <stdio.h>
#include <stdlib.h>

int mandelbrot_calc(double real, double imag)
{
	int limit = 100;
	double zReal = real;
	double zImag = imag;

	for (int i = 0; i < limit; ++i)
	{
		double r2 = zReal * zReal;
		double i2 = zImag * zImag;

		if (r2 + i2 > 4.0)
			return i;

		zImag = 2.0 * zReal * zImag + imag;
		zReal = r2 - i2 + real;
	}
	return limit;
}

int main()
{
	return 0;
}

int *teste()
{

	int *i = malloc(sizeof(int) * 2);

	i[0] = 5;
	i[1] = 20;
	return i;
}

double center_x = -1.04082816210546;
double center_y = 0.346341718848392;

int *mandelbrot(int width, int height, double factor)
{
	static int *vector = 0;

	// int width = 379; // number of characters fitting horizontally on my screen
	// int height = 98; // number of characters fitting vertically on my screen

	// double x_start = -2.0;
	// double x_fin = 1.0;
	// double y_start = -1.0;
	// double y_fin = 1.0;

	//~ double x_start = -0.25;
	//~ double x_fin = 0.05;
	//~ double y_start = -0.95;
	//~ double y_fin = -0.75;

	//~ double x_start = -0.13;
	//~ double x_fin = -0.085;
	//~ double y_start = -0.91;
	//~ double y_fin = -0.88;

	double x_start = center_x - 1.5 * factor;
	double x_fin = center_x + 1.5 * factor;
	double y_start = center_y - factor;
	double y_fin = center_y + factor;

	double dx = (x_fin - x_start) / (width - 1);
	double dy = (y_fin - y_start) / (height - 1);

	if (vector != 0)
		free(vector);
	vector = malloc(sizeof(int) * width * height);

	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{

			double x = x_start + j * dx; // current real value
			double y = y_fin - i * dy;	 // current imaginary value

			int value = mandelbrot_calc(x, y);
			int color = 10;
			if (value == 100)
				color = 0;
			else if (value >= 90)
				color = 1;
			else if (value >= 70)
				color = 2;
			else if (value >= 50)
				color = 5;
			else if (value >= 30)
				color = 6;
			else if (value >= 20)
				color = 4;
			else if (value >= 10)
				color = 3;
			else if (value >= 5)
				color = 12;
			else if (value >= 4)
				color = 11;
			else if (value >= 3)
				color = 8;
			else if (value >= 2)
				color = 7;
			else if (value >= 1)
				color = 9;

			vector[j * height + i] = color;
		}
		//		cout << endl;
	}

	return vector;
}