using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;


class Result
{
    public static int CountValleys(int steps, string path)
    {
        int altitude = 0;
        int valleys = 0;
        int mountains = 0;

        foreach (char step in path)
        {
            if (step == 'U')
            {
                altitude++;
                if (altitude == 0)
                {
                    valleys++;
                }
            }
            else if (step == 'D')
            {
                altitude--;
                if (altitude == 0)
                {
                    mountains++;
                }
            }
        }

        return valleys;
    }

    public static void countingValleys(int steps, string path)
    {
        int valleys = CountValleys(steps, path);
        Console.WriteLine(valleys);
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int steps = Convert.ToInt32(Console.ReadLine().Trim());
        string path = Console.ReadLine();

        int result = Result.CountValleys(steps, path);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
