import java.util.ArrayList;
import java.util.Arrays;



public class BaseBallGame {

    public static int calPoint(String[] ops){
        int sum = 0;
        ArrayList<Integer> record  = new ArrayList<>() ;
        int rl = 0;
        for (int i = 0; i< ops.length; i++){

            switch (ops[i]){
                case "+" :
                    record.add(record.get(rl-1) + record.get(rl- 2));
                    sum += record.get(rl);
                    break;
                case ("D") :
                    record.add(2 * record.get(rl - 1));
                    sum += 2 * record.get(rl-1);
                    break;
                case ("C") :
                    sum -= record.get(rl-1);
                    record.remove(rl - 1);
                    break;

                 default :
                    int score = Integer.valueOf(ops[i]);
                    record.add(score);
                    sum += score;
                     break;
                }
            rl = record.size();
        }

        return  sum;
    }

    public static void main(String[] args) {
        Integer a = - 3;
        int b = -3;
        String[] test = {"5","-2","4","C","D","9","+","+"};
        int result = calPoint(test);
        int test2 = Integer.parseInt(2 + "0");
        System.out.println(result);


    }

}


