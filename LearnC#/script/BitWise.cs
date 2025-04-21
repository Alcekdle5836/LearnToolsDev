
/// <summary>
/// 位运算
/// </summary>
/// 

[Flags]  // 必须标记为 Flags，表示该枚举支持位运算
public enum FileStatus
{
    None  = 0b0000,  // 0
    Read  = 0b0001,  // 1
    Write = 0b0010,  // 2
    Save = 0b0100 // 4
}

class BitWise
{
    public static void BitwiseExample()
    {
        int a = 0b1100;    // 二进制 12 
        int b = 0b1010;    // 二进制 10

        // 按位与 &
        Console.WriteLine($"a & b = {a & b}");   // 0b1000 → 8

        // 按位或 |
        Console.WriteLine($"a | b = {a | b}");   // 0b1110 → 14

        // 异或 ^
        Console.WriteLine($"a ^ b = {a ^ b}");   // 0b0110 → 6

        // 位反 ~
        Console.WriteLine($"~a = {~a}");         // 按位取反（补码表示，结果可能为负数）

        // 左移 <<
        Console.WriteLine($"a << 2 = {a << 2}"); // 0b110000 → 48

        // 右移 >>
        Console.WriteLine($"a >> 1 = {a >> 1}"); // 0b0110 → 6
    }

    public static void ManageFilePermissions()
    {
        // 组合权限：读 + 写
        FileStatus userPermissions = FileStatus.Read | FileStatus.Write;        // 0001 | 0010 = 0011

        // 检查是否包含写权限
        bool canWrite = (userPermissions & FileStatus.Write) != 0;          // 0011 & 0010 = 0010
        Console.WriteLine($"可写权限：{canWrite}"); // 输出 True

        // 添加保存权限
        userPermissions |= FileStatus.Save;                                 // 0011 | 0100 = 0111
        Console.WriteLine($"新权限：{userPermissions}"); // 输出 Read, Write, Save

        // 移除写权限
        userPermissions &= ~FileStatus.Write;           // Write:0010, ~Write:1101, 0011 & 1101 = 0001
        Console.WriteLine($"移除写权限后：{userPermissions}"); // 输出 Read, Save
    }
}

