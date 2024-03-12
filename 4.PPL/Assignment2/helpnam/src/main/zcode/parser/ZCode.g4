grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: NEWLINE* declLst EOF;
declLst: decl declLst | decl;
decl: varDecl ignore| funDecl;

// KEYWORD
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

// OPERATOR
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
ASSIGN: '<-';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
COMPARE: '==';

// SEPERATOR
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';

// DECALARATION
varDecl: varDeclCase1 | varDeclCase2 | varDeclCase3;
varDeclCase1: VAR ID declare; // implicit
varDeclCase2: dataType ID (LBRACK dimenslist RBRACK)? declare?; // normal
varDeclCase3: DYNAMIC ID declare?; // dynamic
declare: ASSIGN expr;
dimenslist: NUMLIT COMMA dimenslist | NUMLIT;

ignore: NEWLINE+;
funDecl: FUNC ID LPAREN (paramLst | ) RPAREN (ignore | ignore? blockStmt | ignore? returnStmt);
paramLst: paramDecl COMMA paramLst | paramDecl;
paramDecl: dataType ID (LBRACK dimenslist RBRACK | );

// TYPE
dataType: NUMBER | BOOL | STRING;

// EXPRESSION
exprLst: expr COMMA exprLst | expr;
expr: expr1;
expr1: expr2 CONCAT expr2 | expr2; // string
expr2: expr3 (EQ | COMPARE | NEQ | LT | GT | LTE | GTE) expr3| expr3; // relational
expr3: expr3 (AND | OR) expr4 | expr4; // logical
expr4: expr4 (ADD | SUB) expr5 | expr5; // adding
expr5: expr5 (MUL | DIV | MOD) expr6 | expr6; // multiplying
expr6: NOT expr6 | expr7; // logical
expr7: (SUB | ADD) expr7 | operand; // sign
operand: subexpr | arrayEle | funccall | ID |literal;

subexpr: LPAREN expr RPAREN;
arrayEle: (ID | funccall) LBRACK exprLst RBRACK;
funccall: ID LPAREN exprLst? RPAREN;
arrayLit: LBRACK exprLst RBRACK;

literal: NUMLIT | TRUE | FALSE | STRLIT | arrayLit;

// STATEMENT
stmtLst: stmt stmtLst | stmt;

stmt:
	varDecl ignore
	| assignmentStmt
	| ifStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| funCallStmt
	| blockStmt;

assignmentStmt: ID (LBRACK exprLst RBRACK)? ASSIGN expr ignore;

ifStmt: IF LPAREN expr RPAREN ignore? stmt elifLst ;
elifLst: elifEle elifLst | elseClause | ;
elifEle: ELIF LPAREN expr RPAREN ignore? stmt;
elseClause: ELSE ignore? stmt ;

forStmt: FOR ID  UNTIL expr BY expr ignore? stmt;

breakStmt: BREAK ignore;

continueStmt: CONTINUE ignore ;

returnStmt: RETURN (expr |) ignore;

funCallStmt: ID LPAREN (exprLst |) RPAREN ignore;

blockStmt: BEGIN ignore (stmtLst |) END ignore;

// CHARACTER
WS: [ \t\r\f\b]+ -> skip; // skip spaces, tabs

// LITERAL
NUMLIT: DIGIT+ (DOT DIGIT*)? EXPONENT?;
BOOLIT: TRUE | FALSE;
STRLIT: ["] VALIDSTRING* ["] {self.text = self.text[1:-1];};
fragment VALIDSTRING: ~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"';

fragment LETTER: [a-zA-Z_];
fragment DIGIT: [0-9];
fragment EXPONENT: [eE][+-]? DIGIT+;
fragment ESC_SEQ: '\\' [bfrnt'\\];
fragment NOT_EOL: ~[\n\r\f];
fragment SQUOTE: '\'';
fragment DQUOTE: '"';
fragment CHARACTER: ESC_SEQ | NOT_EOL | SQUOTE DQUOTE | ~["];
fragment DOT: '.';
fragment HASTAG: '#';
// COMMENT
NEWLINE: [\n];
CMT: HASTAG HASTAG NOT_EOL* -> skip;
// IDENTIFIER
ID: LETTER (LETTER | DIGIT)*;

UNCLOSE_STRING:
	["] VALIDSTRING* ('\r\n' | '\n' | EOF) {
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:
	["] VALIDSTRING* ILLEGAL {
    raise IllegalEscape(self.text[1:])
};
fragment ILLEGAL: [\r] | '\\' ~[bfrnt'\\];

ERROR_CHAR: .{raise ErrorToken(self.text)};