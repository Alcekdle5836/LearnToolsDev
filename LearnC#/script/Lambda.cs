class Lambda
{
    public static void LINQExample()
    {
        int[] numbers = {1,2,3,4,5};
        var max = numbers.Max(x => x);
        var maxSquare = numbers.Max(x => x*x);

        var evenSquares = numbers
            .Where(n => n%2 == 0)
            .Select(n => n*n);
        Console.WriteLine(string.Join(", ", evenSquares)); // 输出 "4, 16"
    }

// 类型自动推断
    public static void LambdaExample()
    {
        int[] numbers = {1,2,3,4,5};
        // 参数类型自动推断为 int
        var sum = numbers.Aggregate((a, b) => a + b);
        Console.WriteLine(sum);

        // 显式指定参数类型（合法但冗余）
        var explicitSum = numbers.Aggregate((int a, int b) => a + b);
        Console.WriteLine(explicitSum);

        // 混合显式和隐式类型 → 错误！
        // var invalid = numbers.Aggregate((int a, b) => a + b); 
        // Console.WriteLine(explicitSum);
    }

// 多语句lambda
    public static void MultiLambda()
    {
        // 多行 Lambda（需显式 return）
        // 泛型委托，接收int并返回string
        Func<int, string> formatNumber = n =>
        {
            string sign = n >= 0 ? "正数" : "负数";
            return $"{sign}: {Math.Abs(n)}";
        };

        Console.WriteLine(formatNumber(-5)); // 输出 "负数: 5"
    }
}
