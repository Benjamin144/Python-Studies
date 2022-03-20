class Type1(object):  
   def Fizz_Buzz(self, n):  
      """  
   
      :type n: int  
      :rtype: List[str]  
      """  
      
      result = []  
      for i in range(1 , n+1):  
         if i % 3 == 0 and i % 5 == 0:  
            result.append(" Fizz_Buzz ")  
         elif i % 3 == 0:  
            result.append(" Fizz ")  
         elif i % 5 == 0:  
            result.append(" Buzz ")  
         else:  
            result.append(str(i))  
      return result  
object1 = Type1()  
print(object1.Fizz_Buzz(55)) 