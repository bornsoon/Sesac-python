import java.util.Scanner;
	
public class MainClass {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String a =sc.next();
    char[] aArray = a.toCharArray();
    for(int i=0; i<aArray.length; i++){
      if((aArray[i]>='a') && (aArray[i]<='z')){
        aArray[i]+=20;
      } else {
        aArray[i]-=20;
      }
    }
  }
}