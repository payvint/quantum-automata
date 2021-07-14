from core.Registry import Registry
from core.Automaton import Automaton
from core.states.Gate import Gate
from core.states.Exit import Exit
from core.states.Measurement import Measurement

mes = Measurement(2, ['0', '1'], [2, 1])
gate = Gate("X", 0, 2)
exit = Exit()
for i in range(10):
    print("\nTest", i)
    print()

    reg = Registry(1)
    automata = Automaton([mes, gate, exit], reg)
    automata.operate()

    print("\nMeasurement outcomes:", automata.getMeasurementOutcomes())
    print("Word:",automata.getWord())
    print()