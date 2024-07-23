# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/4804983/beats-100-0ms-advanced-two-pointer-approach-java-c-python-rust/?envType=study-plan-v2&envId=top-interview-150

use 5.38.0;
use Test::More;

sub solution {
  my ($nums) = @_;
  my $i = -1;
  my $j = 1;
  while ($i++ < @$nums - 1) {
    if ($j == 1 or $nums->[$i] != $nums->[$j - 2]) {
      $nums->[$j] = $nums->[$i];
      $j++;
    }
  }
  return $j;
}

my $nums = [1,1,1,2,2,3];
is(solution($nums), 5);
is_deeply([@$nums[0..4]], [1,1,2,2,3]);

$nums = [0,0,1,1,1,1,2,3,3];
is(solution($nums), 7);
is_deeply([@$nums[0..6]], [0,0,1,1,2,3,3]);

done_testing;
