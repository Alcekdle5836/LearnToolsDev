class FormattedString
{
    public static void FormattedStringExample()
    {
        string name = "Mark";
        var date = DateTime.Now;

        // Composite Formatting
        Console.WriteLine("Hello, {0}! Today is {1}, it's {2:HH:mm} now.",name, date.DayOfWeek, date);

        // String Interpolating
        Console.WriteLine($"Hello, {name}! Today is {date.DayOfWeek},it's {date:HH:mm} now");
    }
}