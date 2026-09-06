class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        int prev[] = intervals[0];
        res.add(prev);

        for (int i = 1; i < intervals.length; i++){
            int[] next = intervals[i];
            if (prev[1] >= next[0] && prev[1] <= next[1]){
                int temp[] = {prev[0], next[1]};
                res.remove(res.size() - 1);
                res.add(temp);
                prev = temp.clone();
            }
            else if (prev[0] <= next[0] && prev[1] >= next[1]) continue;
            else{
                res.add(next);
                prev = next.clone();
            }
        }
        return res.toArray(new int[0][]);
    }
}
