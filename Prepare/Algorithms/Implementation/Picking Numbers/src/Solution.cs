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
     * Complete the 'pickingNumbers' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int pickingNumbers(List<int> a)    
    {
        // Cria dicionario de listas encadeadas como valores
        Dictionary<int, LinkedList<int>> dicionarioDeListas = new Dictionary<int, LinkedList<int>>();
        
        // Para cada inteiro no array
        foreach (int number1 in a)
        {
            // Se ja existir uma chave do inteiro
            if (dicionarioDeListas.ContainsKey(number1))
            {
                // Adiciona o inteiro como novo elemento da lista encadeada
                dicionarioDeListas[number1].AddLast(number1);
            }
            else
            {
                 // Senao cria uma nova lista encadeada e adiciona o inteiro a ela
                LinkedList<int> novaLista = new LinkedList<int>();
                novaLista.AddLast(number1);

                // Adiciona a nova lista a uma nova chave referente ao inteiro, no dicionario
                dicionarioDeListas.Add(number1, novaLista);
            }
        }
        
        // Exibe os subarrays resultantes
        Console.WriteLine("Subarrays resultantes iniciais:");
        
        foreach (var parChaveValor in dicionarioDeListas)
        {
            Console.WriteLine($"{parChaveValor.Key}: {string.Join(", ", parChaveValor.Value)}");
        }
        
        
        // Para no caso de elementos diferentes com valores iguais, nao readicionar elementos
        Dictionary<int, bool> inteirosJaPreenchidos = new Dictionary<int, bool>();
        foreach (int inteiro in a)
        {
            inteirosJaPreenchidos[inteiro] = false;
        }
        
                // ALGORITMO PRINCIPAL (cria redundancias, e.g [1,2,1] [1,1,2] [2,1,1] mas o tamanho do maior subarray sera o mesmo)
        
        // Para cada inteiro no array
        foreach (int inteiro in a)
        {
            // Se o subarray do inteiro ainda nao tiver sido preenchido
            if (inteirosJaPreenchidos[inteiro] == false)
            {
                // cria uma lista de todos outros valores que nao o inteiro
                List <int> b = new List<int>(a);
                b.RemoveAt(b.IndexOf(inteiro));
                Console.WriteLine($"inteiro: {inteiro} | outros inteiros: {string.Join(", ", b)}");
            
                // Para cada outro inteiro no array
                foreach (int outroInteiro in b)
                {
                    // Se diferenca entre eles for menor ou igual a 1 && nao for outro elemento com o mesmo valor, caso esse que ja esta na lista
                    if (Math.Abs(inteiro - outroInteiro) <= 1 && inteiro != outroInteiro)
                    {
                        // adiciona outroInteiro ao subarray do inteiro, no dicionario
                        dicionarioDeListas[inteiro].AddLast(outroInteiro);
                        Console.WriteLine($"{outroInteiro} adicionado!");
                        Console.Write($"A Lista: ");
                        foreach (int item in dicionarioDeListas[inteiro])
                        {
                            Console.Write($"{item} ");
                        }
                        Console.WriteLine();
                        
                        
                        // Manipulacao de nos da lista encadeada
                        LinkedListNode<int> node = dicionarioDeListas[inteiro].First;

                        while (node != null)
                        {
                            int valorAdicionado = node.Value;

                            LinkedListNode<int> outroNode = node.Next;
                            while (outroNode != null)
                            {
                                int outroValor = outroNode.Value;
                                int diferenca = Math.Abs(valorAdicionado - outroValor);
                                
                                // Se a diferenca entre o valor recem-adicionado e qualquer outro inteiro ja no subarray for maior que 1     
                                if (diferenca > 1)
                                {
                                    Console.WriteLine($"{valorAdicionado} - {outroValor} : {diferenca} | {outroValor} removido!");
                                    // remove o valor recem-adicionado
                                    dicionarioDeListas[inteiro].Remove(outroNode);
                                    
                                    Console.Write($"A Lista: ");
                                    foreach (int item in dicionarioDeListas[inteiro])
                                    {
                                        Console.Write($"{item} ");
                                    }
                                    Console.WriteLine();
                                }

                                outroNode = outroNode.Next;
                            }

                            node = node.Next;
                        }
                    }
                }
            }
            // subarray do inteiro: preenchido
            inteirosJaPreenchidos[inteiro] = true;
        }
        
        // Exibe os subarrays resultantes
        Console.WriteLine("Subarrays resultantes finais:");
        foreach (var parChaveValor in dicionarioDeListas)
        {
            Console.WriteLine($"{parChaveValor.Key}: {string.Join(", ", parChaveValor.Value)}");
        }
        
        // Retorna o tamanho do maior subarray
        return dicionarioDeListas.Values.Max(list => list.Count);
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> a = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(aTemp => Convert.ToInt32(aTemp)).ToList();

        int result = Result.pickingNumbers(a);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
