from HW3 import Calculator

x = Calculator()


print('------- Postfix Test Case --------------')
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

print('------- Calculate Test Case --------------')
x.expr='    4  +      3 -2'
print(x.calculate)
# 5.0
x.expr='  -2  +3.5'
print(x.calculate)
# 1.5
x.expr='4+3.65-2 /2'
print(x.calculate)
# 6.65
x.expr=' 23 / 12 - 223 +      5.25 * 4    *      3423'
print(x.calculate)
# 71661.91666666667
x.expr='   2   - 3         *4'
print(x.calculate)
# -10.0
x.expr=' 3 *   (        ( (10 - 2*3)))'
print(x.calculate)
# 12.0
x.expr=' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3'
print(x.calculate)
# 28.6
x.expr=' 2   *  ( 4 + 2 *   (5-3^2)+1)+4'
print(x.calculate)
# -2.0
x.expr='2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2'
print(x.calculate)
# 1442.7777777777778
x.expr="4++ 3 +2"
print(x.calculate)
# 'error message'
x.expr="4    3 +2"
print(x.calculate)
# 'error message'
x.expr='(2)*10 - 3*(2 - 3*2)) '
print(x.calculate)
# 'error message'
x.expr='(2)*10 - 3*/(2 - 3*2) '
print(x.calculate)
# 'error message'
x.expr=')2(*10 - 3*(2 - 3*2) '
print(x.calculate)
# 'error message'

# print(x.postfix(' 2 * 5 + 3 ^ -2  +1 +4 '))

# x.expr = '2 + 3 * ( -2 +(-3) *(5^2 - 2*3^(-2) ) *(-4) ) * ( 2 /8 + 2*( 3 -1/ 3) ) - 2/ 3^2'
# print(x.calculate)