import java.util.*;

class Solution {
    public String solution(int age) {
        // String answer = "";
        HashMap<Integer, Character> dic = new HashMap<Integer, Character>();
        int num = 0;
        char a = 'a';
        while(num<10){
            dic.put(num, a);
            a = (char) (a+1);
            num++;
        }
        
        String st = Integer.toString(age);
        String[] stls = st.split("");
        StringBuffer ans = new StringBuffer();
        for (String k : stls){
            int tmp = Integer.valueOf(k).intValue();
            ans.append(dic.get(tmp));
        }
        System.out.println(ans);
        return ans.toString();
    }
}