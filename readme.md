## Shadowrun matrix

This is a project where I try to build the role playing game shadowrun's matrix
with python.

The basic idea is to simulate twitter's trending topics, but
with shadowrun events.
Game masters will be able to upload event that happened beyond their games
to the matrix, and it will become popular as a artificial inteligence decides.

With this project, game masters will more easily create histories for their games,
and sharing among different masters and players will be more fun.
I think it will be cool see your inpact in the streets taking the hot topics in the matrix, making the game itself more exciting.

#### Parts of the project:

###### Interface:

There will be a site where users can upload content,
register and see what's hot in the sixth world.
This code will be developed using **flask**

###### Trending topics:

The system must avaliate how important is that event and how much
in the trend list it will rise
I plan to use a Neural network for this task, trained with
a dataset of twitter sentimento analysis

**NOTE**: I have no idea how to do this, i'm currently studying
neuralnets to have some idea

###### Generate content:

Random content will be generated to this database.
I plan to use GTP-2 for creating fake events, and then
passing them to the neuralnet avaliate it

###### Region based trend:

It's more cool if the hot topics are chosen by the user's region.
As shadowrun uses our world in the future, i can use their coordinates
to see what's trending there
