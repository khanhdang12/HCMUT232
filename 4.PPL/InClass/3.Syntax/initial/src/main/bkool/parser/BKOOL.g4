grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : delcs EOF ;
delcs: delc delcs | delc;
delc: vardecl | funcdecl;

vardecl: ('int' | 'float') idlist SM ;
idlist: ID CM idlist | ID ;

funcdecl: ('int' | 'float') ID param_decl body;
param_decl: LB param_list? RB;
param_list: param SM param_list | param ;
param: ('int' | 'float') idlist;

body: '{' inside_body? '}';
inside_body: not_empty inside_body | not_empty ;
not_empty: vardecl | statement;

statement: (assign | call | ret) ';';
assign: ID '=' expr;
call: ID '(' expr_list? ')';
ret: 'return' expr;

expr_list: expr CM expr_list | expr ;
expr: expr1 '+' expr | expr1;
expr1: expr2 '-' expr2 | expr2;
expr2: expr2 ('*' | '/') expr3 | expr3;
expr3: subexpr | INTLIT | FLOATLIT | ID | call;
subexpr: '(' expr ')' ;


ID: [a-zA-Z]+ ;
INTLIT:[0-9]+;
FLOATLIT: INTLIT '.' INTLIT ;
SM: ';';
CM: ',';
LB: '(';
RB: ')';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
