Laboratory work №1                                                                                                         
                                                                                                                     
Done by Кекишев Андрей Сергеевич, группа "М80-106БВ-25"                                                                  
                                                                                                         
The task:
    (M1) Make calculator, which takes a string of symbols (digits with operations
    in infix form) as an input and executes the following steps:                                                                                            
    1. It checks if a string is correct.                                                                                                                           
    2.1. If an input string is incorrect the calculator throw an exception.                                                                                         
    2.2. If an input string is correct the calculator counts the whole math expression.                                                                             
    3. It prints the result of calculation in terminal.                                                                                                         
    4. The calculation contains following methods (functions):                                                                                                                                                                                                                                            
            1) summation - it counts '+' and '-' operations and calls method 2).                                                                                      
            2) multiplicative_operations - it counts '*', '/', '//', '%' operations and calls method 3)                                                               
            3) exponentiation - it counts '**' operation                                                                                                         
            4) unary_operation - it is used to define sign of a number in the summation method                                                                        
      
The result:                                                                                                                                                                                                                                              
    The calculator is realised in Calculator class, which has the functionality corresponding to the task.                                                          
    In the process of making this work, it's turned out that a presumption is necessary to
    use this calculator comfortably.                                                                                                         
                                                                                                            
The presumption:                                                                                                                                                                                                                                                  
    1. An input string contains only                                                                                                         
        1) any digits in the decimal number system.                                                                                                         
        2) '+', '-', '*', '/', '//', '**' operations.                                                                                                         
        3) spaces in any quantity.                                                                                                         
        4) parentheses ('(' and ')'), which should be placed correctly. It means that
            '(' always has appropriate ')'. Also number of '(' is equivalent to ')', and ')'
            isn't placed before '('.                                                                                                         
    2.  Any merging of operations in an input string is prohibited.
    3.Any merging of parentheses and digits are also prohibited.                                                                                                         
    4. Division by zero is prohibited. It means that 0 to the negative degree is not allowed too.                                                                         
    5. 0**0 is not allowed.                                                                                                         
   