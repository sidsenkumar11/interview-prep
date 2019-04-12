 import java.util.Arrays;
 import java.util.HashSet;
 import java.util.HashMap;
 import java.util.List;
 import java.util.Set;

class PalindromePermutation {
    public static boolean isPalindromePermutationOne(String s) {

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        boolean canP = true;

        for (char c: s.toCharArray()){
            if(map.containsKey(c)){
                map.put(c, map.get(c)+1);
            }else{
                map.put(c,1);
            }
        }

        int numOfOdd=0;
        for (Character k: map.keySet()){
            if(!(map.get(k)%2==0)){
                numOfOdd++;
            }
            if(numOfOdd==2){
                canP=false;
                break;
            }
        }
        return canP;
    }

    public static boolean isPalindromePermutationTwo(String s) {

       Set<Character> charSet = new HashSet<Character>();

       for(char c: s.toCharArray()){
           if(charSet.contains(c)){
               charSet.remove(c);
           }else{
               charSet.add(c);
           }
       }

       if(charSet.size()<2){
           return true;
       }else{
           return false;
       }
   }

   public static void main(String args[]){
      List<String> inputList = Arrays.asList("code", "aab", "carerac");
      for (String s: inputList){
        System.out.println("Input String: "+ s);
        System.out.print("Method1: "+ isPalindromePermutationOne(s) + "\t");
        System.out.println("Method2: "+ isPalindromePermutationTwo(s));
        System.out.println();
      }
   }
}
