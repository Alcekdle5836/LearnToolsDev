class Dictionary
{
    public static void DictionaryExample()
    {
        // 1. Define
        Dictionary<int, string> dict = new Dictionary<int, string>();

        dict.Add(1, "One");
        dict.Add(2, "Two");
        Console.WriteLine(string.Join(", ", dict)); // [1, One], [2, Two]

        Dictionary<string, int> tempDict = new Dictionary<string, int>
        {
            {"apple", 10},
            {"banana", 20}
        };
        Console.WriteLine(string.Join(", ", tempDict)); // [apple, 10], [banana, 20]

        // 2. Add
        dict[3] = "Three";
        dict.Add(4, "Four");
        string[] keys = {"cat", "dog"};
        int[] values = {30, 40};
        for (int i = 0; i < keys.Length; i++)
        {
            tempDict.Add(keys[i], values[i]);
        }
        Console.WriteLine(string.Join(", ", tempDict)); // [apple, 10], [banana, 20], [cat, 30], [dog, 40]

        // 3. Access
        Console.WriteLine(dict[1]); // One
        Console.WriteLine(dict.ContainsKey(2)); // True
        Console.WriteLine(dict.ContainsValue("Five")); // False

        // 4. Modify
        dict[1] = "First";
        tempDict["apple"] = 100;
        Console.WriteLine(dict[1]); // First
        Console.WriteLine(tempDict["apple"]); // 100

        // 5. Delete
        dict.Remove(2);
        tempDict.Remove("banana");
        Console.WriteLine(dict.ContainsKey(2)); // False
        Console.WriteLine(tempDict.ContainsKey("banana")); // False

        dict.Clear();
        Console.WriteLine(dict.Count); // 0

        // 6. Iterate
        foreach (KeyValuePair<int, string> kvp in dict)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }

        foreach (var key in tempDict.Keys)
        {
            Console.WriteLine(key); // apple, cat, dog
        }

        // 7. Search
        if (tempDict.TryGetValue("cat", out int val))
        {
            Console.WriteLine(val); // 30
        }

        var result = tempDict.Where(kv => kv.Value > 15);
        Console.WriteLine(string.Join(", ", result)); // [apple, 100], [cat, 30], [dog, 40]
    }
}