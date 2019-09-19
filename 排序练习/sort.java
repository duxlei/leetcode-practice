/**
 * 排序算法练习
 * @author duhg
 */
public class AlgorithmPractice {
   
    public static void main(String[] args) {
        AlgorithmPractice sort = new AlgorithmPractice();
        int[] arr = new int[] {6, 4, 3, 5, 9, 10, 7, 2, 1, 8};
        sort.boboSort(arr);
        sort.insertSort(arr);
        sort.selectSort(arr, 0, arr.length - 1);
        sort.quickSort(arr, 0, arr.length - 1);
        sort.print(arr);
    }

    /**
     * 冒泡排序
     */
    public void boboSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
        }
    }

    /**
     * 插入排序
     * 从第二个元素开始，向前比对，找到第一个比自己小的元素放置
     */
    public void insertSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int base = arr[i];
            for (int j = i - 1; j >= 0; j--) {
                if (base < arr[j]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                } else {
                    break;
                }
                arr[j] = base;
            }
        }
    }

    /**
     * 选择排序
     * 遍历一次找出最大和最小值放置对头和对尾，然后递归
     */
    public void selectSort(int[] arr, int left, int right) {
        if (left >= right)
            return;
        int maxIndex = left, minIndex = right;
        for (int i = left; i < right; i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        int temp = arr[left];
        arr[left] = arr[minIndex];
        arr[minIndex] = temp;
        temp = arr[right];
        arr[right] = arr[maxIndex];
        arr[maxIndex] = temp;
        selectSort(arr, left + 1, right - 1);
    }

    /**
     * 快速排序
     * 每次循环找出队列的最大值、最小值得索引为然后分别放到队列首位，然后左右指针向内移动递归
     */
    public void quickSort(int[] arr, int left, int right) {
        if (left >= right)
            return;

        int x = left;
        int y = right;
        int base = arr[left]; // 基准

        while (x < y) {
            while (arr[y] > base && x < y)
                y--;
            arr[x] = arr[y];

            while (arr[x] <= base && x < y)
                x++;
            arr[y] = arr[x];
        }
        arr[x] = base;

        // 递归排序左半边
        quickSort(arr, left, x - 1);
        // 递归排序右半边
        quickSort(arr, x + 1, right);
    }


    public void print(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
