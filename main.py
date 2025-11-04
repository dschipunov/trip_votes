#!/usr/bin/python3

from action import ActionValueRandomizer
from inputs import InputData
from result import Results
from util import SEPARATOR_LINE
                

def main():
    print("Prepare the data...")

    # init action value
    av = ActionValueRandomizer()
    act_value = av.value()

    data1 = InputData.from_input()
    data2 = InputData.from_input()
    data3 = InputData.from_input()

    print(SEPARATOR_LINE)

    # create results
    results = Results(act_value)
    results.add_person(data1)
    results.add_person(data2)
    results.add_person(data3)

    # Pring debug data
    print(results)

    for value in results.values():
        print(f"{value.name}: {value.action}")


if __name__ == "__main__":
    main()