class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> lst = new ArrayList<>();
        for (int[] i: intervals) lst.add(i);
        lst.add(newInterval);
        lst.sort((a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        System.out.println(lst.size());
        int []prev = lst.get(0);
        res.add(prev);
        int size = lst.size();
        for (int i = 1; i < size; i++){
            int[] next = lst.get(i);
            if (prev[1] >= next[0] && prev[1] <= next[1]){
                int temp[] = {prev[0], next[1]};
                prev = temp.clone();
                res.remove(res.size() - 1);
                res.add(temp);
            }
            else if (prev[0] <= next[0] && prev[1] >= next[1]) continue;
            else{
                res.add(next);
                prev = next.clone();
            }
            //lst.sort((a, b) -> Integer.compare(a[0], b[0]));
            /**for (int x[]: lst) {for (int j : x) System.out.print(j + " "); 
            System.out.println();}**/
        }
        return res.toArray(new int[0][]);
    }
}
