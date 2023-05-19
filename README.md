# Number_picking_game

A reinforcement learning agent of a number picking game using Q-learning.

**Rules of the game**: 

There are two players in this number-picking game. At first, each player has 100 points in total. For each round, two players should simultaneously name a number which is equal to or less than the total point you have. Whoever names a larger number scores. And then "your former total points deduct the number you name" becomes your total points for the next round. Whoever gets 4 scores first wins.<br>
      p.s. if two players name the same number in a round, they should re-enter the number for this round.
      
The project is based on Q-learning. It has following updates:

<ol>
<li>train the model by simulating opponent's move randomly</li>
<li>construct a simple reflex agent for opponent's move according to human's logic</li>
<li>add stochasticity to the simple reflex model to ensure the robustness of the model</li>
<li>let the model choose the largest k options while training and evaluating instead of sticking to the largest</li>
<li>Observing that the model tends to choose a large number in their first move. I guess it is because the current reward is based on the score difference instead of winning or not. Therefore, I change the reward to consider winning or not only</li>
<li>propose a bottom-up approach to cover the cases near the leaf. For example, train the model from the state of 3:3 first, then 2:3, 3:2</li>



</ol>
