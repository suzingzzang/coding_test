class Solution {
    public String solution(String src) {
        String answer = "";
        int count = 1;
        char prev = src.charAt(0);

        for (int i = 1; i < src.length(); i++) {
            char curr = src.charAt(i);
            if (curr == prev) {
                count++;
            } else {
                answer += (char)(count + '0');
                count = 1;
                prev = curr;
            }
        }
        answer += (char)(count + '0');
        String finalString = "";
        finalString += src.charAt(0);
        for (int j = 0; j < answer.length(); j++) {
            char c = answer.charAt(j);
            switch (c) {
                case '1':
                    finalString += 'A';
                    break;
                case '2':
                    finalString += 'B';
                    break;
                case '3':
                    finalString += 'C';
                    break;
                case '4':
                    finalString += 'D';
                    break;
                case '5':
                    finalString += 'E';
                    break;
                case '6':
                    finalString += 'F';
                    break;
            }
        }
        return finalString;
    }
}
