// 参考https://blog.csdn.net/Two_Water/article/details/53581978
import java.util.Random;

public class ThreeBoxes {
    public static void main (String[] args) {
        for (int i=0; i<5; i++) {
            calc_threeboxes();
            // System.out.println("----------------end----------------");
        }
    }

    public static void calc_threeboxes() {
        Random random   = new Random();
        int changeCount = 0;
        int keepCount   = 0;
        int maxCount = 1000000;
        for (int i=0; i<maxCount; i++) {
            int[] boxes = new int[3];

            // 随机放入一个盒子
            int rIndex      = random.nextInt(3);
            boxes[rIndex]   = 1;

            // 随机选择一个盒子
            int rSelect     = random.nextInt(3);
            // System.out.println("随机数" + rIndex + " " + rSelect);

            while (true) {
                // 随机删除一个盒子
                int rDelete = random.nextInt(3);

                // 不会打开有物品的盒子
                if (1 == boxes[rDelete]) {
                    continue;
                }

                // 不会打开已经被选择的盒子
                if (rDelete == rSelect) {
                    continue;
                }

                for (int n=0; n<3; n++) {
                    // 不换时的机率
                    if (n == rSelect) {
                        if (1 == boxes[n]) {
                            keepCount++;
                            break;
                        }
                        continue;
                    }
                    // 不能选择已经打开的盒子
                    if (rSelect == rDelete) {
                        continue;
                    }
                    if (1 == boxes[n]) {
                        changeCount++;
                        break;
                    }
                }
                break;
            }
        }
        System.out.println("改变的机率=" + (changeCount*100/maxCount) 
            + "% 不改变的机率=" + (keepCount*100/maxCount) + "%");
    }
}
