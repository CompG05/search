#!/bin/bash

mkdir -p reports/solutions/eight_queens
mkdir -p reports/solutions/sixteen_queens
mkdir -p reports/solutions/eight_puzzle
mkdir -p reports/solutions/fifteen_puzzle
mkdir -p reports/solutions/romania

echo "bidirectional - eight puzzle"
python psolver.py -i reports/states/eightpuzzle.csv -o reports/solutions/eight_puzzle/bidirectional.csv npuzzle bidirectional
echo "bidirectional - fifteen puzzle"
python psolver.py -i reports/states/fifteenpuzzle.csv -o reports/solutions/fifteen_puzzle/bidirectional.csv npuzzle bidirectional
echo "bidirectional - romania"
python psolver.py -i reports/states/romania.csv -o reports/solutions/romania/bidirectional.csv romania bidirectional

algorithms=("iterative_deepening" "uniform_cost" "greedy_best_first" "a_star" "depth_acyclic" "breadth_first")
for algorithm in "${algorithms[@]}"
do
  echo "$algorithm - eight queens"
  python psolver.py -i reports/states/eightqueens.csv -o reports/solutions/eight_queens/$algorithm.csv nqueens $algorithm
  echo "$algorithm - sixteen queens"
  python psolver.py -i reports/states/sixteenqueens.csv -o reports/solutions/sixteen_queens/$algorithm.csv nqueens $algorithm

  echo "$algorithm - eight puzzle"
  python psolver.py -i reports/states/eightpuzzle.csv -o reports/solutions/eight_puzzle/$algorithm.csv npuzzle $algorithm
  echo "$algorithm - fifteen puzzle"
  python psolver.py -i reports/states/fifteenpuzzle.csv -o reports/solutions/fifteen_puzzle/$algorithm.csv npuzzle $algorithm

  echo "$algorithm - romania"
  python psolver.py -i reports/states/romania.csv -o reports/solutions/romania/$algorithm.csv romania $algorithm
done
