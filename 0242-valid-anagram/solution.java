class Solution {
    public boolean isAnagram(String s, String t) {

        // Length different hai to anagram nahi ho sakta
        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26];

        // s ke characters ko count karo
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // t ke characters ko subtract karo
        for (int i = 0; i < t.length(); i++) {
            count[t.charAt(i) - 'a']--;
        }

        // Sab count 0 hone chahiye
        for (int num : count) {
            if (num != 0) {
                return false;
            }
        }

        return true;
    }
}