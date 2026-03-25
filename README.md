# Autonomous Agent for Dynamic Maze Navigation

This project consists of the development of an autonomous agent in Python for the Artificial Intelligence course (Computer Engineering - IPVC).

The objective is to navigate a dynamic and competitive maze, maximizing the collection of rewards (values from 1 to 15) while competing against an opponent.

## Main Features

### 🚀 Optimal Navigation
Implementation of the A* algorithm with the Manhattan Heuristic to ensure the shortest possible path while avoiding obstacles (#).

### 🧠 Strategic Decision-Making
Use of a Utility Function ($Value / Distance$) that prioritizes targets with the best cost-benefit ratio.

### ⚔️ Competitive Awareness
The agent analyzes the opponent's position in real time, adjusting the priority of rewards that are at risk of being captured.

### ⚡ Efficiency
Capable of clearing complex maps in record time (e.g., 64 points in just 81 turns in Maze 01).
