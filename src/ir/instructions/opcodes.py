import sys
sys.path.append("../utils")
from enum import Enum

INST_OP_CODE = Enum(
	ADD="+",
	SUB="-",
	MULT="*",
	DIV="/",
	FLOOR_DIV="//",
	MOD="%",
	POW="**",
	LEFT_SHIFT="<<",
	RIGHT_SHIFT=">>",
	BIT_OR="|",
	BIT_XOR="^",
	BIT_AND="&",
	OR="or",
	AND="and",
	IS="is",
	NOT="not",
	IS_NOT="is not",
	INVERT="~",
	EQ="==",
	NOT_EQ="!=",
	LT="<",
	LTE="<=",
	GT=">",
	GTE=">=",
	IN="in",
	NOT_IN="not in",
	CALL="call",
	LOAD="load",
	STORE="store",
	RETURN="return"
)
