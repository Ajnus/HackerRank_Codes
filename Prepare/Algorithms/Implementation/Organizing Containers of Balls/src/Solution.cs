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

    /*
     * Complete the 'organizingContainers' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts 2D_INTEGER_ARRAY container as parameter.
     */
     
    public static void bubbleSort(int[] array)
    {
        int n = array.Length;
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (array[j] > array[j + 1])
                {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    public static string organizingContainers(List<List<int>> containers)
    {
        int[] containersCapacities = new int[containers.Count];        // n
        int[] EachBallTypeQuantities = new int[containers[0].Count];    // m'ish
        
        Console.WriteLine($"numero de containers: {containers.Count}");
        Console.WriteLine($"quantidade de tipos de bolas: {containers[0].Count}");
        
        // percorre cada container/linha
        for (int i = 0; i < containers.Count; i++)
        {
            int containerCapacity = 0;
            
            foreach(int qtdBolasDeUmTipo in containers[i])
            {
                containerCapacity = containerCapacity + qtdBolasDeUmTipo;
            }
            
            containersCapacities[i] = containerCapacity;

            // percorre tipo de bola/coluna
            for (int j = 0; j < containers[i].Count; j++)
            {
                EachBallTypeQuantities[j] += containers[i][j];
            }
        }
        
        Console.WriteLine("\n----------\nCapacidades dos conteiners:");
        for (int i = 0; i < containersCapacities.Length; i++)
        {
            Console.WriteLine($"{i + 1}: {containersCapacities[i]}");
        }
        Console.WriteLine("----------\n");
        
        Console.WriteLine("\n----------\nQuantidades de cada tipo de Bola:");
        for (int j = 0; j < EachBallTypeQuantities.Length; j++)
        {
            Console.WriteLine($"{j + 1}: {EachBallTypeQuantities[j]}");
        }
        Console.WriteLine("----------\n");
        
        // ordena os arrays
        bubbleSort(containersCapacities);
        bubbleSort(EachBallTypeQuantities);
        
        // se for posssvel o estado final da quantidade de cada tipo de bola para cada container
        if (containersCapacities.SequenceEqual(EachBallTypeQuantities))
            return "Possible";
        else
            return "Impossible";
       
       
        /* OLD 
        
        // SWAP 
        Console.WriteLine($"container[1][0] = {container[1][0]}");
        container[1][0]-=1;
        Console.WriteLine($"container[1][0] = {container[1][0]}");
        
        Console.WriteLine($"container[0][1] = {container[0][1]}");
        container[0][1]+=1;
        Console.WriteLine($"container[0][1] = {container[0][1]}");
        
        
        int containersUniformes = 0;
        int containersMisturados = 0;
        
        foreach (var container in containers)
        {
            if (container.Count != n)
                return "Impossible0";
            
            bool containerUniforme = false;
            int zeroCount=0;
            
            foreach (var qtdBolasDeUmTipo in container)
            {
                if (qtdBolasDeUmTipo == 0)
                {
                    zeroCount=zeroCount+1;
                }
                
                Console.Write(qtdBolasDeUmTipo + " ");  
            }
            
            // Se container so tiver bolas de um tipo
            if (zeroCount == container.Count-1)
            {
                containerUniforme = true;
                containersUniformes +=1;
            }
            else
            {
                containersMisturados+=1;
            }
            
            Console.WriteLine($"containerUniforme? {containerUniforme}");
        }
        
        Console.WriteLine($"\ncontainersUniformes: {containersUniformes}");
        Console.WriteLine($"containersMisturados: {containersMisturados}\n");
        
        if (containersMisturados % 2 == 0)
            return "Possible";
        else
            return "Impossible";
        
        
        
         /*foreach (var row in container)
        {
            foreach (var value in row)
            {
                Console.Write(value + " ");
            }
            
            Console.WriteLine();
        }
        
        return "0";
        */
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int q = Convert.ToInt32(Console.ReadLine().Trim());

        for (int qItr = 0; qItr < q; qItr++)
        {
            int n = Convert.ToInt32(Console.ReadLine().Trim());

            List<List<int>> containers = new List<List<int>>();

            for (int i = 0; i < n; i++)
            {
                containers.Add(Console.ReadLine().TrimEnd().Split(' ').ToList().Select(containersTemp => Convert.ToInt32(containersTemp)).ToList());
            }

            string result = Result.organizingContainers(containers);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
