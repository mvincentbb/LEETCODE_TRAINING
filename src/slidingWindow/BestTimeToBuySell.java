package slidingWindow;



public class BestTimeToBuySell {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int min = Integer.MAX_VALUE;
        for(int val : prices){
            min = Math.min(min, val);
            ans = Math.max(ans,val -min);

        }
        return ans;

    }

    public int maxProfit2(int[] prices){
        int min = Integer.MAX_VALUE;
        int max = 0;

        for(int i =0; i<prices.length ; i++){
            if(prices[i]< min){
                min = prices[i];
            }else if(prices[i]-min > max){
                max = prices[i] - min;
            }
        }
        return max;
    }



}
