class Solution {
    public int solution(int n) {
        int answer = 0;
//         int crr = 0;
//         double sq = Math.sqrt(n);
//         int num = (int) Math.ceil(sq);
//         for (int i =1;i<num;i++){
//             if (n%i==0){
//                 answer += 1;
                
//             }
//         }
//         if (sq==(n/sq) && (n%sq==0)){
//             crr=1;
//         }
//         return answer*2+crr;
        for (int i=1;i<n+1;i++){
            if(n%i==0){
                answer+=1;
            }
        }
        return answer;
    }
}