from HW3 import Calculator

x = Calculator()
print(x.postfix(' 2 ^        4'))
#'2.0 4.0 ^'
print(x.postfix('2'))
# '2.0'
print(x.postfix('2.1*5+3^2+1+4.45'))
# '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
print(x.postfix('    2 *       5.34        +       3      ^ 2    + 1+4   '))
# '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
print(x.postfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4'))
# '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
print(x.postfix('(2.5)'))
# '2.5'
print(x.postfix ('((2))'))
# '2.0'
print(x.postfix ('     -2 *  ((  5   +   3)    ^ 2+(1  +4))    '))
'-2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
print(x.postfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    '))
# '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
print(x.postfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    '))
# '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
print(x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    '))
# '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
print(x.postfix('2 *    5   +   3    ^ -2       +1  +4'))
# 'error message'
print(x.postfix('2    5'))
# 'error message'
print(x.postfix('25 +'))
# 'error message'
print(x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4    '))
# 'error message'
print(x.postfix('2*(5 +3)^ 2+)1  +4(    '))
# 'error message'