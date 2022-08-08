package twoPointers;

import java.util.Locale;

class ValidPalidrome {

    public  boolean isPalindrome(String s) {
        System.out.println(s);
        String si =  s.toLowerCase().replaceAll("[^a-z0-9]","");
        int lastI = si.length() -1;
        for(int i = 0; i<= (lastI/2); i ++){
            if (lastI == -1){
                return true;
            } else if(si.charAt(i)!= si.charAt(lastI-i)){
                return false;
            }
        }
        return true;

    }


/*

     public static String convertAllInLowerCase(String s){
        return s.toLowerCase();
    }
    public static String removeAllNonAphaNumeric(String s){
        String rgx = "[^a-z0-9]";
       return  s.replaceAll(rgx, "");
    }
*/

  /*  public static void main(String[] args) {
        String s = " " ;
//        s.toLowerCase();
//        System.out.println(removeAllNonAphaNumeric(s));
//        System.out.println(s.toLowerCase().replaceAll("[^a-z0-9]","")); ;
        System.out.println(isPalindrome(s));
    }*/

}
