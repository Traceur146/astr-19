class Animal:
    def __init__(self, l_a, l_l, noe, tail, furry):
        self.l_a = l_a
        self.l_l = l_l
        self.noe = noe
        if tail == 'yes':
            self.tail = True
        else:
            self.tail = False

        if furry == 'yes':
            self.furry = True
        else:
            self.furry = False

    def member(self):
        print(f'The length of arm is {self.l_a} inches. \n' 
              f'The length of leg is {self.l_l} inches. \n'
              f'Number of eyes is {self.noe}. \n'
              f'Does it have a tail: {self.tail}. \n'
              f'Is it furry: {self.furry}.')


German_Shepherd = Animal(13.5, 13.5, 2, 'yes', 'yes')
German_Shepherd.member()

