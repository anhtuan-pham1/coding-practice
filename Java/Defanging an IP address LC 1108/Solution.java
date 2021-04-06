class Solution {

    public static void main(String[] args) {
        String a = defangIPaddr("255.100.50.0");
        System.out.println(a);
        String b = defangIPaddr1("255.100.50.0");
        System.out.println(b);
        }
    //Use loop
    public static String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < address.length(); i ++){
            if (address.charAt(i) == '.'){
                sb.append("[.]");
            }
            else{
                sb.append(address.charAt(i));
            }
        }
        return sb.toString();
    }
    //built in function
    public static String defangIPaddr1(String address) {
        return address.replace(".", "[.]");
    }
}
