

def verdict(task_completed_code: int, interactor_verdict: int, checker_verdict: int) -> int:
    # Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, 
    # если программа завершилась с ненулевым кодом, и вердикту чекера в противном случае.
    if interactor_verdict == 0:
        if task_completed_code != 0:
            return 3
        else:
            return checker_verdict

    elif interactor_verdict == 1:  # Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
        return checker_verdict

    elif interactor_verdict == 4:  # Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и 4 в противном случае.
        if task_completed_code != 0:
            return 3
        else:
            return 4

    elif interactor_verdict == 6:  # Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
        return 0

    elif interactor_verdict == 7:  # Если интерактор выдал вердикт 7, итоговый вердикт равен 1.
        return 1

    else:
        return interactor_verdict

task_completed_code: int = int(input())
interactor_verdict: int = int(input())
checker_verdict: int = int(input())
if -128 <= task_completed_code <= 127:
    if 0 <= interactor_verdict <= 7 and 0 <= checker_verdict <= 7:
        print(verdict(task_completed_code, interactor_verdict, checker_verdict))
    else: 
        print("Invalid interactor or checker verdict")
else:
    print("Invalid task completed code")