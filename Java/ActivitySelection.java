public class ActivitySelection {
    public static void print(int[] s, int[] f, int n) {
        System.out.print(0 + " ");
        int j = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] >= f[j]) {
                System.out.print((i+1) + " ");
            }
            j++;
        }
    }

    public static void main(String[] args) {
        int[] s = {1,3,0,5,8,5};
        int[] f = {2,4,6,7,9,9};
        print(s, f, s.length);
    }
}
