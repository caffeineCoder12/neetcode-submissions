class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        for (int[] i : intervals){
            for (int j : i) System.out.println(j + " ");
            System.out.println();
        }
        int prev[] = intervals[0];
        List<int[]> lst = new ArrayList<>();
        lst.add(prev); int c = 0;
        for (int i = 1; i < intervals.length; i++){
            int next[] = intervals[i];
            if (next[0] == prev[0] || prev[1] > next[0]) {c++; continue;} prev = next.clone();
        }
        return c;
    }
}
