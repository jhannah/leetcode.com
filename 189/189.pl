use 5.40.0;
use Test::More;
use Data::Printer;

sub solution {
  my ($k, $nums) = @_;
  my $length = @$nums;
  my $start = $length - $k;
  my $end = $start + $length - 1;
  my @nums = (@$nums, @$nums);
  # say "$start, $end";
  # p @nums;
  # p @nums[$start..$end];
  return [ @nums[$start..$end] ];
}

is_deeply(solution(3, [1,2,3,4,5,6,7]), [5,6,7,1,2,3,4]);
is_deeply(solution(2, [-1,-100,3,99]),  [3,99,-1,-100]);

done_testing;
