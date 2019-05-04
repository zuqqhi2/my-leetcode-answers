# Check given brackets are same bracket type or not
# @param [String] open_bracket open bracket character
# @param [String] close_bracket close bracket character
# @return [Boolean] if given brackets are same type return true otherwise false
def is_same_type(open_bracket, close_bracket)
    if open_bracket == '(' and close_bracket == ')'
        return true
    elsif open_bracket == '{' and close_bracket == '}'
        return true
    elsif open_bracket == '[' and close_bracket == ']'
        return true
    else
        return false
    end
end

# Time Complexity: O(n)
# Space Complexity: O(1)
# @param {String} s
# @return {Boolean}
def is_valid(s)
    # Scan a given string using stack
    stack = []
    for i in 0..s.length-1
        # If open bracket is scanned, it pushes open bracket to the stack
        if s[i] == '(' or s[i] == '{' or s[i] == '['
            stack.push s[i]
        # If close bracket is scanned,
        # it checks close bracket is same type of pushed open bracket
        elsif s[i] == ')' or s[i] == '}' or s[i] == ']'
            open_bracket = stack.pop
            if !is_same_type(open_bracket, s[i])
                return false
            end
        end
    end

    # If stack still has element,
    # return false because there is remaining open bracket
    if stack.length >= 1
        return false
    else
        return true
    end
end
