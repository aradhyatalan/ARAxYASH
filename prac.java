class Student{
    int id;
    String name;
    
    void insertRecord(int i, String n){
        id=i;
        name=n;
}
void displayInformation(){
    System.out.println(id+" "+name);
    }
}

class TestStudent2{
    public static void main(String args[]){
    Student s1=new Student();
    Student s2=new Student();
    s1.insertRecord(101,"abc");
    s2.insertRecord(102,"xyz");
    s1.displayInformation();
    s2.displayInformation();
    }
    }