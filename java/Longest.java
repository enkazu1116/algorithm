package java;

import java.util.HashSet;
import java.util.Set;

public class Longest {

  public int countLongestConsecutive(int[] nums) {

    Set<Integer> set = new HashSet<>();

    for (int number : nums) {
      set.add(number);
    }

    int longest = 0;

    for (int num : set) {
      if (!set.contains(num - 1)) {
        int current = num;
        int length = 1;

        while (set.contains(current + 1)) {
          current++;
          length++;
        }

        longest = Math.max(longest, length);
      }
    }
    return longest;
  }

  public static void main(String[] args) {
    int[] nums = { 100, 3, 4, 2, 200, 1 };

    Longest longest = new Longest();
    int result = longest.countLongestConsecutive(nums);

    System.out.println(result);
  }
}