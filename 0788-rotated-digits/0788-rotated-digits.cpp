class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {         
            string number = to_string(i);
            bool valid = true;
            bool changes = false;

            for (char c : number) {          
                if (c == '3' || c == '4' || c == '7') {
                    valid = false;            
                    break;
                }
                if (c == '2' || c == '5' || c == '6' || c == '9') {
                    changes = true;            
                }            
            }

            if (valid && changes) count++;
        }
        return count;
    }
};