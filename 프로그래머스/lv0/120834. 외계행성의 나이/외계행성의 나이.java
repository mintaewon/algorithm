import java.util.*;

class Solution {
    public String solution(int age) {
        String answer = "";
        HashMap<Integer, Character> dic = new HashMap<Integer, Character>();
        int num = 0;
        char a = 'a';
        while(num<10){
            dic.put(num, a);
            a = (char) (a+1);
            num++;
        }
        
        String st_age = Integer.toString(age);
        for (String k : st_age.split("")){
            int j = Integer.valueOf(k).intValue();
            answer += dic.get(j);
        }
        return answer;
    }
}