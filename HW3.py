#HW3
#Due Date: 11/03/2019, 11:59PM 
'''
Team members:

Collaboration Statement:             

'''

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.count == 0

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        x = Node(value)
        x.next = self.top
        self.top = x
        self.count = self.count + 1
     
    def pop(self):
        # YOUR CODE STARTS HERE
        x = self.top;
        if x != None :
            self.top = x.next
        else :
            self.top = None

        self.count = self.count - 1

        return x

    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.expr = None


    def isNumber(self, txt):
        # YOUR CODE STARTS HERE
        flag = True
        try:            
            float(txt)
        except ValueError:
            flag = False

        return flag    

    def postfix(self, txt):
        '''
            Required: postfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x.postfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x.postfix('2')
            '2.0'
            >>> x.postfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x.postfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x.postfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x.postfix('(2.5)')
            '2.5'
            >>> x.postfix ('((2))')
            '2.0'
            >>> x.postfix ('     -2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '-2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x.postfix('2 *    5   +   3    ^ -2       +1  +4')
            'error message'
            >>> x.postfix('2    5')
            'error message'
            >>> x.postfix('25 +')
            'error message'
            >>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            'error message'
            >>> x.postfix('2*(5 +3)^ 2+)1  +4(    ')
            'error message'
        '''
        if not isinstance(txt,str) or len(txt)<=0:
            print("Argument error in postfix")
            return None

        postStack = Stack()
        # YOUR CODE STARTS HERE

        
# 1. 수자가 나오면 그대로 출력한다.
# 2. (나오면 스택에 push한다.
# 3. * / 나오면 스택에 push한다.
# 4. + - 연산이 나오면 여는 괄호('('), 여는 괄호가 없다면 스택의 끝까지 출력하고 그 연산자를 스택에 push한다.
# 5. 닫는 괄호(')')가 나오면 여는 괄호('(')가 나올때까지 pop하여 출력한다.

        charStack = Stack()

        num = ''
        operator = '+-*/^'
        for c in txt :
            if c in '+-*/^()' :
                # push number string to stack
                num = num.strip()
                if len(num) > 0 and self.isNumber(num) :
                    postStack.push(num)
                elif len(num) > 0 :
                    return None   

                num = ''

                # operator
                if c in operator :                    
                    while charStack.isEmpty() == False and operator.find(c) <= operator.find(charStack.top.value) and charStack.top.value != '(':                                                
                        postStack.push(charStack.pop().value)

                    # Push current Operator on stack    
                    charStack.push(c)
                elif c == '(' :
                    # If the scanned character is an 
                    # ‘(‘, push it to the stack. 
                    charStack.push(c)
                elif c == ')' :
                    # If the scanned character is an 
                    # ‘)’, pop and output from the stack  
                    # until an ‘(‘ is encountered.     
                    while charStack.top.value != '(' :                        
                        postStack.push(charStack.pop().value)
                        
                    # Remove '(' from the stack 
                    charStack.pop()
                
            elif c in '0123456789. ' :
                # If the scanned character is an  
                # operand, add it to output. 
                num = num + c                
            else :
                return None;

        num = num.strip()
        if len(num) > 0 and self.isNumber(num) :
            postStack.push(num)
        elif len(num) > 0 :
            return None    

        while charStack.isEmpty() == False :                        
            postStack.push(charStack.pop().value)    

        return postStack    
        
    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.expr='    4  +      3 -2'
            >>> x.calculate
            5.0
            >>> x.expr='  -2  +3.5'
            >>> x.calculate
            1.5
            >>> x.expr='4+3.65-2 /2'
            >>> x.calculate
            6.65
            >>> x.expr=' 23 / 12 - 223 +      5.25 * 4    *      3423'
            >>> x.calculate
            71661.91666666667
            >>> x.expr='   2   - 3         *4'
            >>> x.calculate
            -10.0
            >>> x.expr=' 3 *   (        ( (10 - 2*3)))'
            >>> x.calculate
            12.0
            >>> x.expr=' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3'
            >>> x.calculate
            28.6
            >>> x.expr=' 2   *  ( 4 + 2 *   (5-3^2)+1)+4'
            >>> x.calculate
            -2.0
            >>> x.expr='2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2'
            >>> x.calculate
            1442.7777777777778
            >>> x.expr="4++ 3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr="4    3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*(2 - 3*2)) '
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*/(2 - 3*2) '
            >>> x.calculate
            'error message'
            >>> x.expr=')2(*10 - 3*(2 - 3*2) '
            >>> x.calculate
            'error message'
        '''

        if not isinstance(self.expr,str) or len(self.expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack=Stack()

        # YOUR CODE STARTS HERE



x = Calculator()
postStack =  x.postfix('1+2*3+(4+2)/2')
print(postStack)