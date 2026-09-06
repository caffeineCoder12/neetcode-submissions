class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int prev = intervals[0][1];
        int c = 0;
        for (int i = 1; i < intervals.length; i++){
            int next[] = intervals[i];
            if (prev > next[0]) {c++; } else prev = next[1];
        }
        return c;
    }
}
