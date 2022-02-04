class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        Stack<Character> st = new Stack<>();
        
        for(int i = 0; i<n; i++)
        {
            char ch = s.charAt(i);
            
            if(ch == '[' || ch == '{'  ||  ch == '(')
                st.push(ch);
            
            if(ch == ']'  || ch == '}'  || ch == ')')
            {
                if(!st.isEmpty())
                {
                    char temp = st.pop();
                    if(!isMatch(temp, ch))
                    return false;
                }
                else{
                    return false;
                }
            }
            
        }
        
       if(st.isEmpty())
           return true;
        
        return false;
    }
    
    
    public boolean isMatch(char first , char second)
    {
        if(first == '{')
        {
            if(second == '}')
                return true;
            return false;
        }
        else if(first == '[')
        {
            if(second == ']')
                return true;
            return false;   
        }
        else{
            if(second == ')')
                return true;
            return false;
        }
    }
}