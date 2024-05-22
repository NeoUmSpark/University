while True:
    def test(n=int(input('Введите число: ')), txt='Результат: '):
        if n == 0 or n == 1:
            print(txt)
            return 1
        else:
            return n * test(n-1)


    print(test())
