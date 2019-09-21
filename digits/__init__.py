from digits.hand_writting import HandWritting
if __name__ == '__main__':
    def print_menu():
        print('0 EXIT')
        print('1 손글씨 인식')
        print('2 손글씨인식 머신 러닝')
        print('3 손글씨인식 테스트')
        return input('CHOOSE ONE\n')
    while 1:
        menu = print_menu()
        print('MENU : %s' % menu)
        if menu == '0':
            print('EXIT')
            break
        elif menu == '1':
            m = HandWritting()
            m.read_file()
            break
        elif menu == '2':
            m = HandWritting()
            m.learning()
            break
        elif menu == '3':
            m = HandWritting()
            fname = './data/my2.png' ###########################--숫자 이미지 설정--################################
            print('테스트 ')
            print(m.test(fname))
            break
        """
        elif menu == '':
            m =
            m.
            break
        """