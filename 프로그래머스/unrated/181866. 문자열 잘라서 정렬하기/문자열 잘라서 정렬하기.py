def solution(myString):
    result_array = []
    for element in myString.split("x"):
        if element != "":
            result_array.append(element)
    result_array.sort()
    
    return result_array
