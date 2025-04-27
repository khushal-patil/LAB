import scala.io.StdIn

object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, World!")
  }
}
object EvenOddCheck{
	def main(args: Array[String]):Unit = {
	    println("Enter any number:")
	    val number = StdIn.readInt()
	    println(s"$number")
		if(number%2==0){
			println(s"$number is even")
		}else {
			println(s"$number is odd")
		}
	}
}

object Factorial {
  def main(args: Array[String]): Unit = {
  
    println("Enter any number:")
    val num = StdIn.readInt()
    println(s"$num")
    var factorial = 1
    
    for (i <- 1 to num) {
      factorial *= i
    }
    println(s"The factorial of $num is $factorial")
  }
}

object ReverseString {
  def main(args: Array[String]): Unit = {
    val str: String = readLine("Enter something: ")
	println(s"You entered: $str")

    val reversed = str.reverse
    println(s"The reverse of '$str' is '$reversed'")
  }
}

object FindLargest {
  def main(args: Array[String]): Unit = {
    println("Enter numbers separated by spaces:")
    val input = readLine()
    val numbers = input.split(" ").map(_.toInt)

    println("You entered the following numbers:")
    numbers.foreach(println)

    val largest = numbers.max
    println(s"The largest number you entered is: $largest")
  }
}


object AddTwoNumbers {
  def main(args: Array[String]): Unit = {
    println("Enter the first number:")
    val num1 = StdIn.readInt()

    println("Enter the second number:")
    val num2 = StdIn.readInt()

    val sum = num1 + num2
    println(s"The sum of $num1 and $num2 is $sum")
  }
}


object SimpleCalculator {
  def main(args: Array[String]): Unit = {
    println("Enter the first number:")
    val num1 = StdIn.readDouble()
    println(s"$num1")
    println("Enter an operator (+, -, *, /):")
    val operator = StdIn.readChar()
    println(s"$operator")
    println("Enter the second number:")
    val num2 = StdIn.readDouble()
    println(s"$num2")

    val result = operator match {
      case '+' => num1 + num2
      case '-' => num1 - num2
      case '*' => num1 * num2
      case '/' => if (num2 != 0) num1 / num2 else "undefined (division by zero)"
      case _   => "Invalid operator"
    }
    println(s"The result is: $result")
  }
}
