class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        for (int k : num_list){
            if(k%2 == 1){
                answer[1]++;
            }else{
                answer[0]++;
            }
        }
        return answer;
    }
}