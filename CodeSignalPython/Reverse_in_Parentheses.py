# Arcade > Intro > 13
# Write a function that reverses characters in (possibly nested) parentheses in the input string
# Input strings will always be well-formed with matching ()s
# Ex input = "(bar)" => "rab"
# Ex input = "foo(bar(baz))blim" => "foobazrabblim"

def reverseInParentheses(s):
    for i in range(len(s)-1, -1, -1):
        if s[i] == "(":
            l = i
            for j in range(l, len(s), 1):
                if s[j] == ")":
                    r = j
                    break
            t = s[l+1:r]
            s = s[0:l] + t[::-1] + s[r+1:]
    return s
    