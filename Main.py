from Visualizer import Visualizer
from solver import Solver

def main():
    solver = Solver()
    visualizer = Visualizer(solver)
    solver.addVisualizer(visualizer)
    visualizer.start()


main()