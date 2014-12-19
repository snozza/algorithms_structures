from progression import Progression
from progression import ArithmeticProgression
from progression import GeometricProgression

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)