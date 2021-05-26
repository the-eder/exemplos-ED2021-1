/* Java program to implement basic stack
operations */
class Stack {
	static final int MAX = 1000;
	int top;
	String a[] = new String[MAX]; // Maximum size of Stack

	boolean isEmpty()
	{
		return (top < 0);
	}
	Stack()
	{
		top = -1;
	}

	boolean push(String x)
	{
		if (top >= (MAX - 1)) {
			System.out.println("Stack Overflow");
			return false;
		}
		else {
			a[++top] = x;
			System.out.println(x + " pushed into stack");
			return true;
		}
	}

	String pop()
	{
		if (top < 0) {
			System.out.println("Stack Underflow");
			return "";
		}
		else {
			String x = a[top--];
			return x;
		}
	}

	String peek()
	{
		if (top < 0) {
			System.out.println("Stack Underflow");
			return "";
		}
		else {
			String x = a[top];
			return x;
		}
	}
}

// Driver code
class Main {
	public static void main(String args[])
	{
		Stack s = new Stack();
		s.push("Fulano 01");
		s.push("Fulano 02");
		s.push("Fulano 03");
		System.out.println(s.pop() + " Popped from stack");
	}
}
