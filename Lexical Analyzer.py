import re

source_code = r"""int main()
{
int x, y;
if (x < y)
printf(“x is less than y”);
else
y=5; /* Assign value of 5 to y */
return 0;
}"""
lexeme_list=["int", "main", "(", ")", "{", "x", "y", ",", ";", 
         "if", "<", "printf", "\"", "is", "less", "than", 
         "else", "=", "5", "Assign", "value", "of", "to"
         "return", "0", "}", "*", "/"]
token_dictionary= {
    "int" : "Keyword",
    "x" : "Identifier",
    "y" : "Identifier",
    "main" : "Identifier",
    "if" : "Identifier",
    "else" : "Identifier",
    "printf" : "Identifier",
    "return" : "Identifier",
    "is" : "Value",
    "less" : "Value",
    "than" : "Value",
    "Assign" : "Value",
    "value" : "Value",
    "of" : "Value",
    "5" : "Value",
    "0" : "Value",
    "to" : "Value",
    "(" : "LPAREN",
    ")" : "RPAREN", 
    "{" : "LBRACE",
    "}" : "RBRACE",
    "<" : "Operator",
    "=" : "Operator",
    "\"" : "Special_Symbol",
    "/" : "Special_Symbol",
    "," : "Special_Symbol",
    ";" : "Special_Symbol",
    "}" : "Special_Symbol",
    "*" : "Special_Symbol",
 }
lines = source_code.split('\n')#creates a list of separate lines by splitting upon the newline
print("\nS. No.   Lexeme      Token       Line No.")
i = 1 #S. No. iterator
j = 0 #line number iterator
for line in lines: #lets iterate upon each line in the list of lines
    j += 1
    list_of_words_from_line = line.split() #splits the line into words based on whitespace (that is the default for split())
    pattern = r'(\w+|[(){}",;</*=])'# \w+ == one or more word character
                                    # | == or
                                    # [xxxxx] takes in all symbols to be split
                                    # re then puts all these split up things into a list
    
    for word in list_of_words_from_line: #now lets go through the list of words in each unique line
        lexemes = re.findall(pattern, word) #create a list of actual lexemes for each line based on the regular expression
        for lexeme in lexemes:
            token = token_dictionary.get(lexeme) #this searches the dictionary and "gets" the corresponding value
            print(f"{i}.       {lexeme.ljust(11)} {token.ljust(15)}   {j}") #this is an f-string. I just learned what it is.
            #ljust() is a function that adjusts the spacing leftwards (the opposite is rjust())
            #its not necessary but cool
            i += 1