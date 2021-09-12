class Rectangle
{
double length;
double width;
public Rectangle() //default
{ length = 0.0; width = 0.0; }
public Rectangle(double l, double w) //parameterized
{ length = l; width = w; }
public Rectangle(double x) //Overloading
{length= width =x;}
public double getPerimeter()
{ return 2 * (length + width); }
}
class RectangleDemo
{
public static void main(String[] args)
{
Rectangle r1 = new Rectangle();
System.out.println("Perimeter of Rectangle is " +
r1.getPerimeter());
Rectangle r2 = new Rectangle(3.5, 4.2);
System.out.println("Perimeter of Rectangle is " +
r2.getPerimeter());
Rectangle r3=new Rectangle(4);
System.out.println("Perimeter of Rectangle is " +
r3.getPerimeter());
}
}