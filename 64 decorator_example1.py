def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print('DISTINCTION')
        result_function(marks)
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print('FAIL')
    else:
        print('PASS')
result([55, 63, 79, 82, 53])