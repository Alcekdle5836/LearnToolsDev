using System;

class TestClass
{
   static void Main(string[] args)
   {
      int x = 100;
      object obj = x;			// 装箱：值类型变为引用类型
      Console.WriteLine ("对象的值 = {0}", obj);
      int num = (int) obj;    // 拆箱：引用类型变为值类型，显式转换
      Console.WriteLine ("num: {0}", num);
   }
}