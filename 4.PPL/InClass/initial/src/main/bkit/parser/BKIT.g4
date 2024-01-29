grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : EOF ;

// ID: [a-z][a-z0-9]*;

// fragment INTPART: [0-9]+;
// fragment DECPART: '.'[0-9]+;
// fragment EXPPART: 'e'[-]?[0-9]+;
// REAL: INTPART DECPART | INTPART DECPART? EXPPART;

// fragment SingQ: ['];
// STRING: SingQ (~['] | SingQ SingQ)* SingQ;

// fragment Dot: [.];
// fragment First: [1-2];
// fragment SecondThird: [0-9];
// fragment Address: '0' | First SecondThird? SecondThird?;
// IPV4: Address Dot Address Dot Address Dot Address;

PHPINT: '0' | [1-9][0-9]*[0-9_]*[0-9]* {self.text = self.text.replace("_", "")};

SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .  {raise ErrorToken(self.text)};
