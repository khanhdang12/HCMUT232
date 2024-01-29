// 2053105
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: NEWLINE* list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables ignore;

//TODO declared variable
variables: implicit_var | keyword_var | implicit_dynamic; 
keyword_var: typ ID (LSB dimenslist RSB)? decl?;
implicit_var: VAR ID decl; 
implicit_dynamic: DYNAMIC ID decl?;
decl: ASSIGNINIT expression;

dimenslist: NUMBER_LIT CM dimenslist | NUMBER_LIT;

//TODO declared function
function: FUNC ID LB parameters_list? RB  (ignore? return_statement | ignore? block_statement | ignore);
parameters_list: parameter CM parameters_list | parameter;
parameter: typ ID (LSB dimenslist RSB)?; 


//TODO Expression
list_expr: expression CM list_expr | expression;
expression: expression1 CONCAT expression1 | expression1;  
expression1: expression2 relational expression2 | expression2; 
expression2: expression2 logical expresisson3 | expresisson3;
expresisson3: expresisson3 adding expression4 | expression4;
expression4: expression4 multiplying expression5 | expression5;
expression5: NOT expression5 | expression6 ;
expression6: SUB expression6 | expression7;
expression7: subexpr | arrayele | funccall | ID | literal ;
relational: EQ | SAME | DIF | LT | GT | LTE | GTE;
logical: AND | OR;
adding: ADD | SUB;
multiplying: MUL | DIV | MOD;

subexpr: LB expression RB;
arrayele: (ID | funccall) LSB list_expr RSB ;
funccall: ID LB list_expr? RB;
array_lit: LSB list_expr? RSB ;

//TODO Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_lit;
typ: NUMBER | BOOL | STRING;

//TODO  Statements
statement_list: statement statement_list | ; 
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

declaration_statement: variables ignore;
assignment_statement : lhs ASSIGNINIT expression ignore;
lhs: ID (LSB list_expr RSB)?;

return_statement: RETURN (expression | ) ignore;
block_statement: BEGIN ignore statement_list END ignore;

if_statement: IF LB expression RB ignore? statement list_elif;
list_elif: elseif_stmt list_elif | else_stmt ;
else_stmt: ELSE ignore? statement | ;
elseif_stmt: ELIF LB expression RB ignore? statement ;

for_statement: FOR ID UNTIL expression BY expression ignore? statement;
break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;

call_statement: ID LB list_expr? RB ignore;


// kí tự bỏ qua
ignore: NEWLINE+;

// Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
// NOT AND OR
EQ: '=';
ASSIGNINIT: '<-';
DIF: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
SAME: '==';

// Seperators
LB: '('; 	RB: ')';
LSB: '['; 	RSB: ']';
CM: ',';

// Literals
NUMBER_LIT: INTPART DECPART? EXPPART?;

fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLEAN_LIT: TRUE | FALSE;

STRING_LIT: ["] VALIDSTRING* ["] {self.text = self.text[1:-1];};
fragment VALIDSTRING: ~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"'; 

// Newline and comment
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]* -> skip;

// ID
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [ \t\r]+ -> skip; // skip spaces, tabs

UNCLOSE_STRING: ["] VALIDSTRING* ('\r\n' | '\n' | EOF){
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: ["] VALIDSTRING* ILLEGAL {
    raise IllegalEscape(self.text[1:])
};
fragment ILLEGAL: [\r\f\\] | '\\' ~[bfrnt\\] | ['] ~["];

ERROR_CHAR: .{raise ErrorToken(self.text)};