# TheGameThatLearns 
Small project created for an UConn Artificial Intelligence club event aimed at introducing children to coding and artificial intelligence.
The code was written by myself and was based on the YouTube video "The game that learns" by Vsauce2 https://www.youtube.com/watch?v=sw7UAZNgGg8

The main python file "TheGameThatLearns.py" contains a fully working version of the code and can be run as an executable.

The folder "SkeletonVersions" contains multiple different, incomplete versions of the code intended to be filled in by the
people attending the event. Each of the functions they use have been abstracted into a more intuitive form as to serve as
an easy introduction to coding. There are three versions of the skeleton code: "S", "SEasier", and "SHarder". As one may
expect, the "SHarder" file gives the student less starter code while "SEasier" includes more starter code.

The file "TheGameThatLearns.pdf" contains descriptions of the various functions and variables the students were intended to
use when attempting to complete the skeleton code. These functions have been abstracted in such a way that they should be 
intuitive for most first time coders. Included is also a short blueprint that outlines the structure the student should use
for their code and explains how basic python operations work (ie. if statements, while loops, ect.).

The "Intelligent" component of the game functions in a very simple way that is somewhat reminiscent of reinforcement learning. 
This particular game has a small set of board states, and has the property that the second player can always win so long as they
do not make any mistakes. Mistakes can easily be found if a move immediatly results in an AI loss, or if the next human player
move results in an AI loss. Eventually all incorrect moves are weeded out and the "Intelligent" computer player will never lose.
Thus this project is simple and trivial from an AI perspective, but fascinating to one who is beginning their programming adventure.
