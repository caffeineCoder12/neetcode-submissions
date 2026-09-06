/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals.isEmpty()) return 0;
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        PriorityQueue<Interval> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.end, b.end));
        for (Interval i : intervals){
            if (pq.isEmpty()){
                pq.offer(i);
            }
            else if (pq.peek().end <= i.start){
                pq.poll();
                pq.offer(i);
            }
            else{
                pq.offer(i);
            }
        }//cart125
        
        return pq.size();
    }
}
