import enum


class Cmd(enum.Enum):
    PROG_HALT = 1
    PROG_HALT_D = 1006
    DECL_ID = 2
    DECL_ARRAY = 3
    DECL_D_ID = 1003
    DECL_D_ARRAY = 1004
    IDENTIFIER = 6
    IDENTIFIER_ARRAY = 7
    IDENTIFIER_NEST = 8
    VAL_ID = 1001
    VAL_NUM = 1002
    EXPR_VAL = 9
    EXPR_PLUS = 10
    EXPR_MINUS = 11
    CMD_ASSIGN = 4
    CMD_IF_ELSE = 5
    CMD_IF = 1005
    CMD_READ = 12
    CMD_WRITE = 13
    COND_EQ = 14
    COND_NEQ = 15
    COND_GE = 16
    COND_LE = 17
    COND_GEQ = 18
    COND_LEQ = 19
    CMDS_CMDS = 20
    CMDS_CMD = 21

