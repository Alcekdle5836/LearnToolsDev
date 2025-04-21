class String
{
    public static void StringExample()
    {
        string str = "aabdefg";
        //Access
        Console.WriteLine(str.Length);      // 7
        Console.WriteLine(str[0]);          // a

        //Modify
        Console.WriteLine(str.Substring(1));        // abdefg
        Console.WriteLine(str.EndsWith("g"));       // True
        Console.WriteLine(str.StartsWith("b"));     // False
        Console.WriteLine(str.IndexOf('a'));        // 0
        Console.WriteLine(str.LastIndexOf('a'));    // 1
        Console.WriteLine(str.Replace("a",""));     // bdefg
        string[] splitResult = str.Split('b');
        foreach (string part in splitResult)
        {
            Console.WriteLine(part);                // aa defg
        }

        //Convert
        char[] arr = str.ToCharArray();
        foreach (char c in arr)
        {
            Console.WriteLine(c);           // a a b d e f g
        }

        arr[0] = '1';
        Console.WriteLine(int.Parse(arr[0].ToString()));    // 1
        Console.WriteLine(new string(arr));                 // 1abdefg
    }
}