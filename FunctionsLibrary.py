#Class Definition
class FunctionsLibrary() :
    #Function 1
    def Subfields() : 
            subFieldsList = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            print("Sub-fields in AI are : ")
            for fieldItem in subFieldsList :
                print(fieldItem)

    #Function 2
    def OddOrEven(num) : 
        if(num%2==0) :
            print(num, " is Even number")
        else :
            print(num, " is Odd number") 

    #Function 3
    def MarriageEligibilityChecker(age,gender) :
        if(gender.lower()=="female" and age>=18) :
            print("Eligible to get married")
        elif(gender.lower()=="male" and age>=21) :
            print("Eligible to get married")
        else :
             print("Not Eligible to get married")

    #Function 4
    def MarkListCalculator(m1,m2,m3,m4,m5) :
       total = m1 + m2 + m3 + m4 + m5
       percentage = (total/500)*100 
       print("Total : ", total)
       print("Percentage : ", percentage) 

     #Function 5
    def CalculateArea(height,breadth) :
        return (height*breadth)/2   

    #Function 6
    def CalculatePerimeter(height1,height2,breadth) :
        return height1+height2+breadth