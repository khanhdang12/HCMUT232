//ID: 2053105
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declarationList EOF;

//3.2 Program comment
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

//3.7 Literals
literal: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | arrayLit;

INTLIT: [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_","")} | '0';

FLOATLIT    : (INTLIT DECIMAL 
            | INTLIT EXPONENT 
            | DECIMAL EXPONENT 
            | INTLIT DECIMAL EXPONENT) 
            {self.text = self.text.replace("_","")}
            ;
fragment EXPONENT: [Ee][+-]?[0-9]+ ;
fragment DECIMAL: '.' [0-9]*;

BOOLEANLIT: TRUE | FALSE;

STRINGLIT: '"' (STRING_CHAR | ESCAPE)* '"' {
	content = str(self.text) 
	self.text = content[1:-1]
};
fragment STRING_CHAR: ~[\\"\n];
fragment ESCAPE: '\\b'
			   | '\\f'
			   | '\\r'
			   | '\\n'
			   | '\\t'
			   | '\\\''
			   | '\\\\'	
			   | '\'"'
			   | '\\"' 
               ;
fragment ESCERROR: '\\' ~[bfrnt\\] | '\'' ~'"';

arrayLit: LBRACE expressionList RBRACE;

//4Type system and values
typ: atomic_types | array_type | VOID | AUTO;

//4.1 Atomic types
atomic_types: BOOLEAN | INTEGER | FLOAT | STRING;

//4.2 Array type
array_type: ARRAY LBRACK intlist RBRACK OF atomic_types;
intlist: INTLIT COMMA intlist | INTLIT;

//4.3 Void type

//4.4 Auto type

//5. Declarations
declarationList: declaration declarationList | declaration;
declaration: variableDeclaration | functionDeclaration;

//5.1.1 Variable declarations
variableDeclaration: ID variableRes expression SEMI | idlist COLON typ SEMI;
idlist: ID COMMA idlist | ID;
variableRes: COLON typ EQUAL | COMMA ID variableRes expression COMMA;

//5.1.2 Parameters
parameterList: parameter COMMA parameterList | parameter;
parameter: INHERIT? OUT? ID COLON typ;

//5.2 Function declarations
functionDeclaration: ID COLON FUNCTION typ LPAREN parameterList? RPAREN (INHERIT ID)? blockStatement;

//6. Expressions
expression: stringExp;
stringExp: relationalExp DOUBLE_COLON relationalExp | relationalExp;
relationalExp: logical1Exp (EQUALS | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL | GREATER_THAN_EQUAL) logical1Exp | logical1Exp;
logical1Exp: logical1Exp (AND | OR) addingExp | addingExp;
addingExp: addingExp (ADD | SUB) multiplyingExp | multiplyingExp;
multiplyingExp: multiplyingExp (MUL | DIV | MOD) logical2Exp | logical2Exp;
logical2Exp: DIFF logical2Exp | signExp;
signExp: SUB signExp | operand;
operand: literal | ID | functionCall| indexOp | subExpr;
subExpr: LPAREN expression RPAREN;
indexOp: ID LBRACK expPrime RBRACK;
functionCall: ID LPAREN expressionList RPAREN;
expressionList: expPrime | ;
expPrime: expression COMMA expPrime | expression;

//7. Statements
statement   : assignmentStatement 
            | ifStatement 
            | forStatement 
            | whileStatement 
            | doWhileStatement 
            | breakStatement 
            | continueStatement 
            | returnStatement 
            | callStatement 
            | blockStatement
            ;

//7.1 Assignment statement
assignmentStatement: scalar_variable EQUAL expression SEMI;
scalar_variable :  ID | indexOp;

//7.2 If statement
ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;

//7.3 For statement
forStatement: FOR LPAREN scalar_variable EQUAL expression COMMA expression COMMA expression RPAREN statement;

//7.4 While statement
whileStatement: WHILE LPAREN expression RPAREN statement;

//7.5 Do while statement
doWhileStatement: DO blockStatement WHILE LPAREN expression RPAREN SEMI;

//7.6 Break statement
breakStatement: BREAK SEMI;

//7.7 Continue statement
continueStatement: CONTINUE SEMI;

//7.8 Return statement
returnStatement: RETURN expression? SEMI;

//7.9 Call statement
callStatement: ID LPAREN expressionList  RPAREN SEMI;

//7.10 Block statement
blockStatement: LBRACE blocklist RBRACE;
blocklist: blockcontent blocklist | ;
blockcontent: statement | variableDeclaration;

//3.4 Keywords
AUTO: 		'auto';
BREAK: 		'break';
BOOLEAN: 	'boolean';
DO: 		'do';
ELSE: 		'else';
FALSE: 		'false';
FLOAT: 		'float';
FOR: 		'for';
FUNCTION: 	'function';
IF: 		'if';
INTEGER: 	'integer';
RETURN: 	'return';
STRING: 	'string';
TRUE: 		'true';
WHILE: 		'while';
VOID: 		'void';
OUT: 		'out';
CONTINUE: 	'continue';
OF: 		'of';
INHERIT: 	'inherit';
ARRAY: 		'array';

//3.5 Operators
ADD: 				'+';
SUB: 				'-';
MUL: 				'*';
DIV: 				'/';
MOD: 				'%';
DIFF: 				'!';
AND: 				'&&';
OR: 				'||';
EQUALS: 			'==';
NOT_EQUAL: 			'!=';
LESS_THAN: 			'<';
LESS_THAN_EQUAL: 	'<=';
GREATER_THAN: 		'>';
GREATER_THAN_EQUAL:	'>=';
DOUBLE_COLON: 		'::';

//3.6 Seperators
LPAREN: 	'(';
RPAREN: 	')';
LBRACK: 	'[';
RBRACK: 	']';
LBRACE: 	'{';
RBRACE: 	'}';
DOT: 		'.';
COMMA: 		',';
SEMI: 		';';
COLON: 		':';
EQUAL: 		'=';

//3.3 Identifiers (It goes last in the so that it won't be confused by the program by keywords)
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//3.1 Character set
WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' (STRING_CHAR | ESCAPE)* (EOF | '\n'){
	content = str(self.text)
	esc = '\n'
	if content[-1] in esc:
		raise UncloseString(content[1:-1])
	else:
		raise UncloseString(content[1:])
};

ILLEGAL_ESCAPE: '"' (STRING_CHAR | ESCAPE)* ESCERROR {
	content = str(self.text) 
	raise IllegalEscape(content[1:])
};

ERROR_CHAR: .{raise ErrorToken(self.text)};
