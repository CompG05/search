#!/bin/bash

algorithms=("a_star")
for algorithm in "${algorithms[@]}"
do
  "Running for $algorithm"
  python psolver.py -i reports/states/eightqueens.csv -o reports/solutions/eight_queens/$algorithm.csv nqueens $algorithm
  python psolver.py -i reports/states/sixteenqueens.csv -o reports/solutions/sixteen_queens/$algorithm.csv nqueens $algorithm

  python psolver.py -i reports/states/eightpuzzle.csv -o reports/solutions/eight_puzzle/$algorithm.csv npuzzle $algorithm
  # python psolver.py -i reports/states/fifteenpuzzle.csv -o reports/solutions/fifteen_puzzle/$algorithm.csv npuzzle $algorithm

  python psolver.py -i reports/states/romania.csv -o reports/solutions/romania/$algorithm.csv romania $algorithm
done

python psolver.py -i reports/states/eightpuzzle.csv -o reports/solutions/eight_puzzle/bidirectional.csv npuzzle bidirectional
# python psolver.py -i reports/states/fifteenpuzzle.csv -o reports/solutions/fifteen_puzzle/bidirectional.csv npuzzle bidirectional

python psolver.py -i reports/states/romania.csv -o reports/solutions/romania/bidirectional.csv romania bidirectional