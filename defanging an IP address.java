class Solution {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();
        char[] addrs = address.toCharArray();

        for(char a : addrs){
            if ( a == '.'){
                sb.append("[.]");
            }
            else{
                sb.append(a);
            }
        }
        return sb.toString();
    }
}