//antlr4 -v 4.7.2 -Dlanguage=Python3 clong.g4 -visitor
grammar clong;

prog: head main;
//导入语句：忽略
head: (include)*;
include: '#include' '<' library '>';
//main语句
main: ('int' | 'void') 'main' '()' '{' body '}';
//main内语句
body: (func ';' | block)*;
//函数
func: (printf | gets | strlen | returnFunc);
//语句块
block:
	ifElse
	| whileFunc
	| forFunc
	| initParam
	| initArray
	| assign;
//printf函数
printf: 'printf' '(' ((stringm (',' exp)*) | paramName) ')';
//gets函数
gets: 'gets' '(' paramName ')';
//strlen函数
strlen: 'strlen' '(' paramName ')';
//return函数
returnFunc: 'return' (intm)?;
//if-else语句
ifElse: ifFunc (elseif)* (elseFunc)?;
ifFunc: 'if' '(' exp ')' '{' body '}';
elseif: 'else' 'if' '(' exp ')' '{' body '}';
elseFunc: 'else' '{' body '}';
//while语句
whileFunc: 'while' '(' exp ')' '{' body '}';
//for语句
forFunc:
	'for' '(' initFunc ';' exp ';' assignFunc ')' '{' body '}';
initFunc: (typeParam)? paramName ('=' exp)? (',' initFunc)? |;
assignFunc: paramName '=' exp (',' assignFunc)? |;
//初始化参数
initParam:
	typeParam paramName ('=' exp)? (',' paramName ('=' exp)?)* ';';
//初始化数组
initArray: typeParam paramName '[' intm ']' ';';
//参数,数组参数赋值
assign: (((paramName | array) '=')+ exp) ';';
//表达式
exp:
	charm
	| stringm
	| paramName
	| (op = '-')? (intm | doublem)
	| array
	| func
	| '(' exp ')'
	| exp op = (
		'+'
		| '-'
		| '*'
		| '/'
		| '%'
		| '>'
		| '<'
		| '>='
		| '<='
		| '=='
		| '!='
		| '&&'
		| '||'
	) exp
	| op = '!' exp;
//类型
typeParam: 'int' | 'char' | 'double';
//数组元素
array: paramName '[' exp ']';
//库
library: PAR '.h'?;
//变量名
paramName: PAR;
PAR: [a-zA-Z_][a-zA-Z0-9_]*;
//int值
intm: INT;
INT: '-'? [0-9]+;
//double值
doublem: DOUBLE;
DOUBLE: '-'? [0-9]+ '.' [0-9]+;
//字符
charm: CHAR;
CHAR: '\'' .'\'';
//字符串
stringm: STRING;
STRING: '"' .*? '"';
//跳过符号
LineComment: '//' .*? '\r'? '\n' -> skip;
BlockComment: '/*' .*? '*/' -> skip;
DELIMITER: [ \t\r\n]+ -> skip;