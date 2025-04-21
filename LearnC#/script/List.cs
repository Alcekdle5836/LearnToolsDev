class List
{
    public static void ListExample()
    {
        // Define
        List<string> list = new List<string>();
        list.Add("This");
        list.Add("is");
        list.Add("a");
        list.Add("list");
        Console.WriteLine(string.Join(" ", list.ToArray()));        //This is a list

        List<string> temp2 = new List<string>{"This", "is", "a", "List" };
        Console.WriteLine(string.Join(" ", temp2.ToArray()));        // This is a List

        // Add
        string[] arr = {"with", "string", "array"};
        
        List<string> temp1 = new List<string>(arr);
        Console.WriteLine(string.Join(" ", temp1.ToArray()));       // with string array

        list.AddRange(arr);
        Console.WriteLine(string.Join(" ", list.ToArray()));        //This is a list with string array

        // Delete
        //Remove (T item)
        list.Remove("array");           //This is a list with string

        // RemoveAt(int index)
        list.RemoveAt(list.Count-1);    //This is a list with

        // RemoveRange(int index, int count)
        list.RemoveRange(4,1);          //This is a list

        // RemoveAll (Predicate<T> match)
        list.RemoveAll(x => x.Contains("is"));  //a

        list.Clear();

        // Search
        List<string> slist = new List<string>{"This", "is", "a","search"};
        slist.Contains("is");           // True

        //Exists (Predicate<T> match);
        slist.Exists(x => x.Contains("is") && x.Length == 3); // False
        //T? Find (Predicate<T> match)
        slist.Find(x => x.Contains("is"));          // This

        //List<T> FindAll (Predicate<T> match)
        slist.FindAll(x => x.Contains("is"));       // This is List
        slist.IndexOf("is"); //1
    }
}