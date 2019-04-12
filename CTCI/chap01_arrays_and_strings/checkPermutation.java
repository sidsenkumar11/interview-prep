class checkPermutation {
    public boolean isAnagram(String s, String t) {
        int n = 26;

       int array[] = new int[n];
        for(int i=0; i<n; i++){
            array[i] = 0;
        }

        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            int index = c - 'a';
            array[index] = array[index]+1;
        }

        for (int i=0; i<t.length(); i++){
            char c = t.charAt(i);
            int index = c - 'a';
            array[index]--;
        }

        for (int i=0; i<n; i++){
            if (array[i]!=0){
                return false;
            }
        }
         return true;
     }
}
