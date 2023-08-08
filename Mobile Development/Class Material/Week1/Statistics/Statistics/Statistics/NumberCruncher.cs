using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Statistics
{
	internal class NumberCruncher
	{
		double[] data = new double[1000];
		int count;

		public void addNumber(double number)
		{
			data[count] = number;
			count++;
		}
		public void displayData() 
		{
			for (int i = 0; i < count; i++)
			{
				Console.Write(data[i]+"\t");
			}
		}

		public void removeLastNumber()
		{
			
			data = data.Take(data.Count() - 1).ToArray();
		}

		public double total()
		{
			double total = 0;
			foreach (double number in data)
			{
				total = total + number;
			}
			return total;
		}
	}
}
